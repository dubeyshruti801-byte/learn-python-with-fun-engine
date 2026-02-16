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
    "modulus": "modulus"
}
def normalize_output(raw_output):
              """
              Docstring for normalize_output
              convert printed output into a clean list of string.
              handles:
              -list, tuple, set, dict, space separated, newline separates

              :param raw_output: Description
              """
              if raw_output is None:
                 return []
              

              #--------------------------#
              # List , Tuple, Set 
              #--------------------------#
              
              if (
                 (raw_output.startswith("[") and raw_output.endswith("]")) or
                 (raw_output.startswith("(") and raw_output.endswith(")")) or
                 (raw_output.startswith("{") and raw_output.endswith("}")) and ":" not in raw_output
                
             ):
                 raw_output= raw_output[1:-1].strip()
                 if raw_output == "":
                    return []
                 items= raw_output.split(",")

                 return [item.strip().strip("'").strip('"') for item in items]    

              #----------------------------#
              #       Dictionary         
              #----------------------------#

              if raw_output.startswith("{") and raw_output.endswith("}") and ":" in raw_output:
                 raw_output= raw_output[1:-1].strip()

                 if raw_output == "":
                    return []
                 pairs= raw_output.split(",")

                 cleaned= []
                 for pair in pairs:
                    if ":" in pair:
                       key, value =pair.split(":",1)
                       key= key.strip().strip("'").strip('"')
                       value= value.strip().strip("'").strip('"')
                       cleaned.append(f"{key} : {value}")
                  
                 return cleaned
              #----------------------------#
              #   Newline separated
              #----------------------------#
              if "\n" in raw_output:
                 return [line.strip() for line in raw_output.split("\n") if line.strip()]
              
              #----------------------------#
              #   Space  separated
              #----------------------------#
              if "" in raw_output:
                 return [item.strip() for item in raw_output.split("") if item.strip()]
              
              #----------------------------#
              #   Single Value
              #----------------------------#
              return [raw_output]



def validate_code(code, questions):
    test_cases= questions.get("test_case", [])
    variables_loaded = set()
    variables_used= set()
    has_loop= False
    has_condition= False
    has_collection= False
    expects= questions["expects"]
    output= []
    sandbox_locals= {}
    test_inputs= []
    used_operators= set()
    input_buffer= []
    input_index= 0
    input_called= False

    
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
         
        if isinstance(node, ast.Call):

         if isinstance(node.func, ast.Name):
          func_name = node.func.id
         elif isinstance(node.func, ast.Attribute):
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

         if isinstance(node.func, ast.Attribute):
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
           value= input_buffer[input_index]
           input_index += 1
           return value
        return ""

    safe_globals={
         "print": fake_print,
         "input": fake_input
        }
    SAFE_METHODS = ["append", "extend", "insert", "pop", "remove"]

    
    for case in test_cases:
       output.clear()
       input_index = 0

       raw_input= case.get("input") or ""
       raw_input = case.get("input") or []

       if isinstance(raw_input, list):
        input_buffer = [str(x).strip() for x in raw_input]
       else:
        input_buffer = [x.strip() for x in str(raw_input).replace(",", " ").split()]

       try:
        exec(code, safe_globals, sandbox_locals)
       except Exception:
        return False, "Runtime Error ❌"
       
       expected_raw = case.get("expected_output", [])

      # Join printed output into one string
       actual_raw = "\n".join(output)

normalized_output = normalize_output(actual_raw)
normalized_expected = [str(x).strip() for x in expected_raw]

# Special handling for sets (unordered)
if expects.get("collection_type") == "set":
    if set(normalized_output) != set(normalized_expected):
        return False, f"Output mismatch ❌ Expected: {normalized_expected}, Got: {normalized_output}"
else:
    if normalized_output != normalized_expected:
        return False, f"Output mismatch ❌ Expected: {normalized_expected}, Got: {normalized_output}"


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
          return False, f"Collection {expects.get('collection_type')} not used ❌"
       
    #-----------Loop validation----------#
    if expects.get("requires_loop"):
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
      required_op= expects.get("operation")
      if required_op:
        required_op = ALIASES.get(required_op.lower(), required_op.lower())

        if required_op not in used_operators:
            return False, f"Required operation {required_op} not used ❌"
      

    return True, "Correct ✅"





