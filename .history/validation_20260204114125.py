import ast
FORBIDDEN =["eval","exec","import","__"]

def validate_code(code, questions):
    output= []
    sandbox_locals= {}
    #1.Forbidden key
    for word in  FORBIDDEN:
        if word in code:
            return False, "Forbidden keyword used ❌"
        
    #2.AST parse
    try:
        tree = ast.parse(code)
    except SyntaxError:
        return False, "synatx Error ❌"
    

    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            func_name= getattr(node.func, "id", "") 
                
             #allows print
            if func_name == "print":
               continue
            #allow input only if question expects it
            if func_name =="input" and "inputs" in questions["expected_output"]:
               continue

            return False, f"Function "

            
    
    def fake_print(*args):
     output.append("".join(map(str, args)))

    try:
      exec(code, {"print": fake_print})
    except Exception:
     return False, "Runtime Error ❌"
    
    if not output or output[0] != expected_output:
       return False, "Output mismatch ❌"
    

    return True, "Correct ✅"
