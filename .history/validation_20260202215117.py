import ast
FORBIDDEN =["eval","exec","import","__"]

def validate_code(code, expected_output):
    #Forbidden key
    for word in  FORBIDDEN:
        if word in code:
            return False, "Forbidden keyword used ❌"