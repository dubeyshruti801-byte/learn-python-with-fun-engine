import ast
FORBIDDEN =["eval","exec","import","__"]

def validate_code(code, questions):
    expects= questions["expected_output"]
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
           used_operators.add(type(node.op).__name__)

        # function calls
        if isinstance(node, ast.Call):
            func_name= getattr(node.func, "id", "") 
                
             #allows print
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
    if expects.get("input_count") is not None:
       if len(test_inputs) < except.get

    


    return True, "Correct ✅"





