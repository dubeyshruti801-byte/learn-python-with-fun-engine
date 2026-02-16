import ast
FORBIDDEN =["eval","exec","import","__"]

def validate_code(code, expected_output):
    #1.Forbidden key
    for word in  FORBIDDEN:
        if word in code:
            return False, "Forbidden keyword used ❌"
        
    #2.AST parse
    try:
        tree = ast.parse(code)
    except SyntaxError:
        return False, "synatx Error ❌"
    #3.allow only prints
    for node in ast.walk(tree):
        if isinstance(node, ast.l):
            if not getattr(node.func, "id", "") == "print":
                return False, "Only print() allowed ❌"
            
    output= []
    def fake_print(*args):
     output.append("".join(map(str, args)))

    try:
      exec(code, {"print:", {fake_print}})
    except Exception:
     return False, "Runtime Error ❌"
    
    if not output or output[0] != expected_output:
       return False, "Output mismatch ❌"
    

    return True, "Correct ✅"
