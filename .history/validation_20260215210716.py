import ast
import signal
import os
FORBIDDEN =["eval","exec","import","__"]
op_map = {
     "Add": "addition",
     "Sub": "subtraction",
     "Mult": "multiplication",
     "Div": "division",
     "FloorDiv":"floordivision",
     "Mod": "modulus",
     "Pow":"power"
    }
ALIASES = {
    "add": "addition",
    "addition": "addition",
    "+": "addition",

    "sub": "subtraction",
    "subtract": "subtraction",
    "subtraction": "subtraction",
    "-": "subtraction",

    "multiply": "multiplication",
    "multiplication": "multiplication",
    "*": "multiplication",
    "mul":"multiplication",

    "divide": "division",
    "division": "division",
    "/": "division",
    "div" : "division",

    "mod": "modulus",
    "%": "modulus",
    "modulus": "modulus",

    "comparison": "comparison"

}


def validate_code(code, questions):
    test_cases= questions.get("test_case", [])
    variables_loaded = set()
    variables_used= set()
    has_condition= False
    has_collection= False
    has_loop= False
    has_function_def = False
    has_function_call = False
    has_return = False
    while_true_detected = False

    expects= questions["expects"]
    ''' METHOD_MAP = {
    "list": ["append", "extend", "insert", "pop", "remove", "clear"],
    "set": ["add", "remove", "clear", "pop"],
    "dict": ["get", "keys", "values", "items", "update"],
    "tuple": []
      }

    collection_type = expects.get("collection_type")
    SAFE_METHODS = METHOD_MAP.get(collection_type, [])'''
    SAFE_METHODS = ["append", "extend", "insert", "pop", "remove", "items","split"]
    output= []
    sandbox_locals= {}
    test_inputs= []
    used_operators= set()
    input_buffer= []
    input_index= 0
    input_called= False
    loop_types_used = set()
    
    def timeout_handler(signum, frame):
       raise TimeoutError("Infinite loop detected ❌")

    #-------Basic sanity------#
    if not isinstance(code, str):
     return False, "Code must be a string ❌"

    #Forbidden key
    for word in  FORBIDDEN:
        if word in code:
            return False, "Forbidden keyword used ❌"
        
    #2.AST parse
    try:
        tree = ast.parse(code)
    except SyntaxError:
        return False, "synatx Error ❌"
    
    #----------AST Rules----------#
    func_name = None

    for node in ast.walk(tree):
        #Track variables
        if isinstance(node, ast.Name):
           if isinstance(node.ctx, ast.Store):
               variables_used.add(node.id)
           elif isinstance(node.ctx, ast.Load):
              variables_loaded.add(node.id)

        #Track loop
        if isinstance(node,(ast.For, ast.While)):
           has_loop= True
        
        #Track condition
        if isinstance(node, ast.If):
           has_condition = True

        #Track collection
        if isinstance(node, (ast.List, ast.Tuple, ast.Dict, ast.Set,
                              ast.ListComp, ast.DictComp, ast.SetComp)):
           has_collection= True

        #detect operators
        if isinstance(node, (ast.BinOp, ast.AugAssign, ast.UnaryOp)):
           op_name = type(node.op).__name__
           normalized= op_map.get(op_name, op_name)
           used_operators.add(normalized)
         
        if isinstance(node, ast.Compare):
          used_operators.add("comparison")
       
        if isinstance(node, ast.For):
            loop_types_used.add("for")

        if isinstance(node, ast.While):
            loop_types_used.add("while")
            if isinstance(node.test, ast.Constant) and node.test.value == True:
                while_true_detected = True
        
        # Detect function definition
        if isinstance(node, ast.FunctionDef):
           has_function_def = True

       # Detect return statement
        if isinstance(node, ast.Return):
          has_return = True

       # Detect function calls (user defined)
        if isinstance(node, ast.Call):
           if isinstance(node.func, ast.Name):
              if node.func.id not in {"print", "input", "list", "dict", "set", "tuple", "int", "float", "map", "range", "str"}:
               has_function_call = True


        if isinstance(node, ast.Call):

          # Normal functions
            if isinstance(node.func, ast.Name):
              func_name = node.func.id

              if func_name == "print":
                continue

              if func_name == "input":
                if expects.get("requires_input"):
                    input_called = True
                    continue
                else:
                    return False, "Function 'input' not allowed ❌"

              if func_name in {"split","list", "tuple", "dict", "set", "int", "float", "map", "range", "str"}:
                continue

        # Method calls
            elif isinstance(node.func, ast.Attribute):
              func_name = node.func.attr

              if func_name in SAFE_METHODS:
                 has_collection = True
                 continue

              return False, f"Function '{func_name}' not allowed ❌"
            
    #--------Controlled execution-------#
    
    def fake_print(*args):
         output.append("".join(map(str, args)))

    
    def fake_input(prompt=""):
      nonlocal input_index

      # 🔥 Single-line mode (for input().split())
      if expects.get("input_mode") == "single_line":
         if input_index == 0:
            input_index = len(input_buffer)
            return " ".join(input_buffer)
         return ""

      # 🔥 Multi-line mode (default behavior)
      if input_index < len(input_buffer):
        value = input_buffer[input_index]
        input_index += 1
        return value

      return ""


    safe_globals={
         "print": fake_print,
         "input": fake_input
        }

    for case in test_cases:
     output.clear()
     input_index = 0
     sandbox_locals = {}

     raw_input = case.get("input") or []

     if isinstance(raw_input, dict):
        input_buffer = []
        for k, v in raw_input.items():
            input_buffer.append(str(k))
            input_buffer.append(str(v))
     elif isinstance(raw_input, list):
        input_buffer = [str(x).strip() for x in raw_input]
     else:
        input_buffer = str(raw_input).strip().split()

     if os.name != "nt":
        signal.signal(signal.SIGALRM, timeout_handler)
        signal.alarm(2)

     try:
         exec(code, safe_globals, sandbox_locals)
     except TimeoutError:
         return False, "Infinite loop detected ❌"
     except Exception:
         return False, "Runtime Error ❌"

     if os.name != "nt":
        signal.alarm(0)

     # -------- OUTPUT HANDLING -------- #

     expected_raw = case.get("expected_output")
     full_output = "\n".join(output).strip()

     try:
        expected_output = ast.literal_eval(expected_raw)
     except:
        expected_output = expected_raw

     # 1️⃣ STATE-BASED QUESTIONS
     if expects.get("state_based"):
        if str(expected_output) not in full_output:
            return False, f"Output mismatch ❌ Expected: {expected_output}, Got: {full_output}"
        continue

     # 2️⃣ FUNCTION-BASED QUESTIONS
     if expects.get("requires_function"):
        lines = [line.strip() for line in output if line.strip()]
        last_line = lines[-1] if lines else ""

        try:
            student_output = ast.literal_eval(last_line)
        except:
            student_output = last_line
     if expects.get("coerce_output_to_string"):
         student_output = str(student_output)
         expected_output = str(expected_output)

         if student_output != expected_output:
            return False, f"Output mismatch ❌ Expected: {expected_output}, Got: {student_output}"
        continue

      # 3️⃣ NORMAL QUESTIONS
     try:
        student_output = ast.literal_eval(full_output)
     except:
        student_output = full_output

     if student_output != expected_output:
        return False, f"Output mismatch ❌ Expected: {expected_output}, Got: {student_output}"


    #----------Input Validation----------#
    if expects.get("requires_input"):
        if not input_called:
         return False, "Inupt not taken ❌"
       
   #-----------Print validation----------#
    if expects.get("requires_print"):
       if not output:
          return False, "Nothing printed ❌"
    
   #----------Collection Validation---------#
    if expects.get("requires_collection"):
       if not has_collection:
         return False
       
    #-----------Loop validation----------#
    if expects.get("requires_loop"):
        required_loop = expects.get("loop_type")
        if required_loop:
          if required_loop not in loop_types_used:
             return False, f"{required_loop} loop required ❌"
        else:
             if not has_loop:
               return False, "Loop not used ❌"


    #---------Condition Validation---------#
    if expects.get("requires_condition"):
       if not has_condition:
          return False, "Condition not used ❌"
    
    #---------Variable flow validation---------#
    if expects.get("variable_flow"):
       if len(variables_used.intersection(variables_loaded)) == 0:
          return False, "No variable usage flow detected ❌"
       
    #--------operation validation--------#
    if expects.get("requires_operation"):
      required_op= expects.get("operation_type")
      if required_op:
        required_op = ALIASES.get(required_op.lower(), required_op.lower())

        if required_op not in used_operators:
            return False, f"Required operation {required_op} not used ❌"
        
    # -------- Function Validation --------
    if expects.get("requires_function"):
         if not has_function_def:
          return False, "Function not defined ❌"

    if expects.get("function_must_return"):
        if not has_return:
          return False, "Function must return a value ❌"

    # -------- State Based Validation --------
    if expects.get("state_based"):
        if not while_true_detected:
          return False, "while True loop required ❌"
        
    return True, "Correct ✅"





