from questionlevel1 import questions1
from questionlevel2 import questions2
from questionlevel3 import questions3
from questionlevel4 import question4
from questionlevel5 import question5
from validation import validate_code

All_questions=  que question5
score= 0

def get_multiline_code():
    print("Enter your Python code (type END on new line to submit):")
    lines = []

    while True:
        line = input()
        if line.strip() == "END":
            break
        lines.append(line)

    return "\n".join(lines)
    
print("Learn python with Fun 🚀")
print("BASIC LEVEL 1 STARTED 🎯\n")

for q in All_questions:
    print(f"Q{q['id']}: {q['prompt']}")
    user_code= get_multiline_code()

    correct , feedback= validate_code(user_code , q)
    print(feedback)

    if correct:
        score += 2
    else:
        score -= 1
    
    print(f"Current Score: {score}\n")

print("Game Over 🥅")
print(f"Final Score: {score}")
      