import ast
FORBIDDEN =["eval","exec","import","__"]

def validate_code(code, questions):
    output= []
    sandbox_locals= {}
    
    if not isinstance(code, str):
     return False, "Code must be a string ❌"

    #1.Forbidden key
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
        if isinstance(node, ast.Call):
            func_name= getattr(node.func, "id", "") 
                
             #allows print
            if func_name == "print":
               continue
            #allow input only if question expects it
            if func_name =="input" and "input_prompt" in questions["expected_output"]:
               continue

            return False, f"Function '{func_name}' not allowed ❌"

            
    #--------Controlled execution-------#
        def fake_print(*args):
         output.append("".join(map(str, args)))

        def fake_input(prompt=""):
         output.append(prompt)
         return questions["expected_output"].get("input_prompt",[""])[0]
    
    safe_globals={
         "print": fake_print,
        "input": fake_input
        }
       

    try:
        exec(code, safe_globals, sandbox_locals)
    except Exception:
      return False, "Runtime Error ❌"
    
    expects= questions["expected_output"]
    #----------Validate output----------#

    var_info= expects.get("variable")

    if var_info:
        var_name= var_info["name"]
        

    if var_name not in sandbox_locals:
          return False , f"Variable '{var_name}' not defined  ❌"
       
       if not isinstance(sandbox_locals[var_name],var_type):
          return False, f"'{var_name}' must be {var_type.__name__} ❌"
    

       if not output or output[0] != questions["expected_output"]:
         return False, "Output mismatch ❌"
    

    return True, "Correct ✅"
