from questions.questionlevel1 import questions1
from questions.questionlevel2 import questions2
from questions.questionlevel3 import questions3
from questions.questionlevel4 import question4
from questions.questionlevel5 import question5
from engine.engine import PythonGameEngine
levels = [
    ("LEVEL 1 — PRINT BASICS", questions1),
    ("LEVEL 2 — INPUT & VARIABLES", questions2),
    ("LEVEL 3 — OPERATORS", questions3),
    ("LEVEL 4 — LOOPS & COLLECTIONS", question4),
    ("LEVEL 5 — FUNCTIONS & STATE LOGIC", question5)
]

engine = PythonGameEngine(levels)

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

for level_name, level_questions in engine.get_levels():

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

      correct , feedback= engine.submit(user_code , q)
      print(feedback)

      if correct:
         score += 2
      else:
         score -= 1
    
      print(f"Current Score: {score}\n")

print("Game Over 🥅")
print(f"Final Score: {score}")
      