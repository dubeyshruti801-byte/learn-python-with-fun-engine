import ast
FORBIDDEN =["eval","exec","import","__"]

def validate_code(code, expected_output):
    #Forbi