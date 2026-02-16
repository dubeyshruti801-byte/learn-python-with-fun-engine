import ast
FORBIDDEN =["eval","exec","import","__"]

def validate_code(code, questions):
    expects= questions["expected_output"]
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
    
    #----------AST Rules----------#
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            func= getattr(node.func, "id", "") 
                
             #allows print
            if func == "print":
               continue
            #allow input only if question expects it
            if func =="input":
               if expects.get("requires_input") or expects.get("input_prompt"):
                continue
               else:
                return False, "Function 'input' not allowed ❌"
            
            if func == "list":
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
    
    
    #----------Validate output----------#

    var_info= expects.get("variable")

    if var_info:
        var_name= var_info["name"]
        var_type= var_info["type"]

        if var_name not in sandbox_locals:
          return False , f"Variable '{var_name}' not defined  ❌"
       
        if not isinstance(sandbox_locals[var_name],var_type):
          return False, f"'{var_name}' must be {var_type.__name__} ❌"
    
    expected_print = expects.get("print")

    if expected_print is not None:
      if not output or output[0] != expected_print:
        return False, "Output mismatch ❌"


    return True, "Correct ✅"
