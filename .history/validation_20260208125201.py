import ast
FORBIDDEN =["eval","exec","import","__"]

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
             if node.func.attr == "split":
              continue

            

         return False, f"Function '{func_name}' not allowed ❌"

            
    #--------Controlled execution-------#
    
    def fake_print(*args):
         output.append("".join(map(str, args)))

    def fake_input(prompt=""):
         test_inputs.append(prompt)
         if expects.get("input_type"):
            return "5"
         return "1"
    
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
      op_map = {
       "Add": "addition",
       "Sub": "subtraction",
       "Mult": "multiplication",
       "Div": "division",
       "Mod": "modulus"
     }


      required_op= expects.get("operation")
      if required_op:
          ast_op= op_map.get("required_op")
          if ast_op not in  used_operators:
             return False, f" Reuired operation {required_op} not used. "
    
          

    


    return True, "Correct ✅"





