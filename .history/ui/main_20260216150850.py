from questions import questionlevel1 []
from questions import questionslevel2
from questions import questionslevel3[]
from questionlevel4 import question4
from questionlevel5 import question5
from validation import validate_code

levels = [
    ("LEVEL 1 — PRINT BASICS", questions1),
    ("LEVEL 2 — INPUT & VARIABLES", questions2),
    ("LEVEL 3 — OPERATORS", questions3),
    ("LEVEL 4 — LOOPS & COLLECTIONS", question4),
    ("LEVEL 5 — FUNCTIONS & STATE LOGIC", question5)
]

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


print("\n" + "="*50)   
print("Learn python with Fun 🚀")
print("="*50 + "\n")

for level_name, level_questions in levels:

    print("\n" + "="*50)
    print(f"{level_name} STARTED 🎯")
    print("="*50 + "\n")

    for q in level_questions:
      print("\n" + "=" * 50)
      print(f"Q{q['id']}: {q['prompt']}")

      if "instruction" in q and q["instruction"]:
        print("\n📘 Instructions:")
        for line in q["instruction"]:
            print(f"- {line}")
        
      print("=" * 50)


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
      