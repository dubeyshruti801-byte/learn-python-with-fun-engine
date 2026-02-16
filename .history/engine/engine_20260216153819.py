from validation import validate_code

class PythonGameEngine:

    def __init__(self, levels):
        self.levels = levels
        self.score = 0

    def submit(self, code, question):
        correct, feedback = validate_code(code, question)

        if correct:
            self.score += 2
        else:
            self.score -= 1

        return {
            "correct": correct,
            "feedback": feedback,
            "score": self.score
        }

    def get_levels(self):
        return self.levels
