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

def validate_code(code, questions):
    expects= questions["expects"]
    output= []
    sandbox_locals= {}
    test_inputs= []
    used_operators= set()

    
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
        #detect operators
        if isinstance(node, ast.BinOp):
           op_name = type(node.op).__name__
           used_operators.add(op_map.get(op_name, op_name))
        if isinstance(node, ast.AugAssign):
           op_name = type(node.op).__name__
           used_operators.add(op_map.get(op_name, op_name))
        if isinstance(node, ast.UnaryOp):
           op_name = type(node.op).__name__
           used_operators.add(op_map.get(op_name, op_name))



         
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
                continue
               else:
                return False, "Function 'input' not allowed ❌"
            
         if func_name == "list":
               continue

         if func_name == "int":
               continue

         if func_name == "float":
               continue

         if isinstance(node.func, ast.Attribute):
             if node.func == "split":
              continue
         
         if func_name in ["list","int","float","split"]:
               continue

            

         return False, f"Function '{func_name}' not allowed ❌"

            
    #--------Controlled execution-------#
    
    def fake_print(*args):
         output.append("".join(map(str, args)))

    def fake_input(prompt=""):
         test_inputs.append(prompt)
         if expects.get("input_type") == int:
          return "5"
         elif expects.get("input_type") == list:
          return "1 2 3 4 5 6 7 8 9 10"
         return "text"

    
    safe_globals={
         "print": fake_print,
         "input": fake_input
        }
       
    try:
        exec(code, safe_globals, sandbox_locals)
    except Exception:
      return False, "Runtime Error ❌"
    
    
    #----------Input Validation----------#
    required_inputs=expects.get("input_count")
    if required_inputs is not None:
       if len(test_inputs) < required_inputs:
          return False, f"reuired atleast '{required_inputs}' inputs ❌"
       
   #-----------Print validation----------#
    if expects.get("requires_print"):
       if not output:
          return False, "Nothing printed ❌"
       
    #--------operation validation--------#
    if expects.get("requires_operation"):
      required_op= expects.get("operation")
      if required_op:
       if required_op.lower() not in used_operators:
        return False, f"Required operation {required_op} not used ❌"
      symbol_map= {
         "addition": "+",
         "subtraction" : "-",
         "multiplication": "*",
         "division": "/",
         "floordivision": "//",
         "mod":"%",
         "power":"**"
      }


     
    
          

    


    return True, "Correct ✅"





