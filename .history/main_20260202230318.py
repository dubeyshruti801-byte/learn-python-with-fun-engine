from questionBank import questions
from validation import validate_code


score= 0
      
print("Learn python with Fun 🚀")
print("BASIC LEVEL 1 STARTED 🎯\n")

for q in questions:
    print(f"Q{q['id']}: {q['prompt']}")
    user_code= input("Write your python code: \n")

    correct , feedback= validate_code
      