import ast
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
    expects= questions["expects"]
    SAFE_METHODS = ["append", "extend", "insert", "pop", "remove", "items"]
    output= []
    sandbox_locals= {}
    test_inputs= []
    used_operators= set()
    input_buffer= []
    input_index= 0
    input_called= False
    loop_types_used = set()
 
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

        if isinstance(node, ast.Call):

           if isinstance(node.func, ast.Name):
            func_name = node.func.id
           elif isinstance(node, ast.Attribute):
            func_name = node.func.attr
           else:
            func_name = ""

              if func_name == "print":
               continue

            #allow input only if question expects it
            if func_name =="input":
               if expects.get("requires_input"):
                input_called = True
                continue
               else:
                return False, "Function 'input' not allowed ❌"
            
            if func_name in ["list","tuple","dict","set"]:
               has_collection = True
               continue
            if func_name in ["int","float"]:
               continue

            if func_name == "map":
               continue

            if func_name == "range":
               continue

            if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
             if node.func.attr == "split":
              has_collection= True
              continue
             elif node.func.attr in SAFE_METHODS:
                has_collection= True
                continue

           return False, f"Function '{func_name}' not allowed ❌"

            
    #--------Controlled execution-------#
    
    def fake_print(*args):
         output.append("".join(map(str, args)))

    
    def fake_input(prompt=""):
     nonlocal input_index

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
       
       sandbox_locals = {}   # ← RESET HERE

       raw_input = case.get("input") or []

       if isinstance(raw_input, dict):
         input_buffer = []
         for k, v in raw_input.items():
           input_buffer.append(str(k))
           input_buffer.append(str(v))
       elif isinstance(raw_input, list):
         input_buffer = [str(x).strip() for x in raw_input]
       
       else:
       # split space separated values
         input_buffer = str(raw_input).strip().split()


       try:
        exec(code, safe_globals, sandbox_locals)
       except Exception:
        return False, "Runtime Error ❌"
       
       expected_raw = case.get("expected_output") or []

       # Join printed output into one string
       actual_raw = "\n".join(output)

       actual_raw = "\n".join(output).strip()
       expected_raw = case.get("expected_output")

       try:
        student_output = ast.literal_eval(actual_raw)
       except:
        student_output = actual_raw

       try:
        expected_output = ast.literal_eval(expected_raw)
       except:
        expected_output = expected_raw

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
       if expects.get("loop_type") not in loop_types_used:
         return False

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
      

    return True, "Correct ✅"





