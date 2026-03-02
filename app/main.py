from fastapi import FastAPI
from pydantic import BaseModel
from app.database.mongodb import users_collection
from fastapi import HTTPException
from app.questions.questionlevel1 import questions1
from app.questions.questionlevel2 import questions2
from app.questions.questionlevel3 import questions3
from app.questions.questionlevel4 import question4
from app.questions.questionlevel5 import question5
from app.engine.engine import PythonGameEngine

app = FastAPI()

levels = [
    ("LEVEL 1 — PRINT BASICS", questions1),
    ("LEVEL 2 — INPUT & VARIABLES", questions2),
    ("LEVEL 3 — OPERATORS", questions3),
    ("LEVEL 4 — LOOPS & COLLECTIONS", question4),
    ("LEVEL 5 — FUNCTIONS & STATE LOGIC", question5)
]

engine = PythonGameEngine(levels)

@app.get("/")
def home():
   return{"message":"Learn Python With Fun API is running 🚀"}

class StartGame(BaseModel):
    username: str
@app.post("/start")
async def start_game(data: StartGame):
    existing_user = await users_collection.find_one({"username": data.username})

    if existing_user:
        return {"message": "User already exists"}

    user_data = {
        "username": data.username,
        "current_level": 1,
        "current_question_index": 0,
        "questions_cleared": 0,
        "levels_cleared": 0,
        "score": 0
    }

    await users_collection.insert_one(user_data)

    return {"message": "Game started", 
            "username": data.username}


@app.get("/question/{username}")
async def get_current_question(username: str):

    user = await users_collection.find_one({"username": username})

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    level_index = user["current_level"] - 1
    question_index = user["current_question_index"]
    
    # 2️⃣ Check if game already completed
    if user.get("game_completed"):
        return {
            "message": "Game completed 🎉",
            "info": "Use /restart to play again"
        }

    level_questions = levels[level_index][1]

    if question_index >= len(level_questions):
        return {"message": "Level completed 🎉"}

    question = level_questions[question_index]

    return {
        "id": question["id"],
        "prompt": question["prompt"],
        "instruction": question.get("instruction", [])
    }


class CodeSubmission(BaseModel):
   username: str
   code: str

@app.post("/submit")
async def submit_code(data: CodeSubmission):

    # 1️⃣ Get user
    user = await users_collection.find_one({"username": data.username})

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # 2️⃣ Check if already completed
    if user.get("game_completed"):
        return {
            "message": "Game already completed 🎉",
            "info": "Use /restart to play again"
        }

    level_index = user["current_level"] - 1
    question_index = user["current_question_index"]

    level_questions = levels[level_index][1]
    question = level_questions[question_index]

    result = engine.submit(data.code, question)

    # Safe defaults
    new_level = user["current_level"]
    new_question_index = question_index
    level_completed = False

    if result["correct"]:

        new_question_index += 1

        # ✅ LEVEL COMPLETED
        if new_question_index >= len(level_questions):
            level_completed = True
            new_level += 1
            new_question_index = 0

            # ✅ GAME COMPLETED
            if new_level > len(levels):
                await users_collection.update_one(
                    {"username": data.username},
                    {
                        "$set": {
                            "game_completed": True
                        },
                        "$inc": {
                            "questions_cleared": 1,
                            "score": 10
                        }
                    }
                )

                return {
                    "message": "Congratulations! You completed the entire game 🎉",
                    "final_score": user["score"] + 10
                }

        # Update DB normally
        await users_collection.update_one(
            {"username": data.username},
            {
                "$set": {
                    "current_level": new_level,
                    "current_question_index": new_question_index
                },
                "$inc": {
                    "questions_cleared": 1,
                    "score": 10
                }
            }
        )

    updated_user = await users_collection.find_one({"username": data.username})

    response = {
        "correct": result["correct"],
        "feedback": result["feedback"],
        "current_level": updated_user["current_level"],
        "score": updated_user["score"]
    }

    # ✅ Add level completed message if needed
    if level_completed:
        response["message"] = "Level completed 🎯 Moving to next level!"

    return response

@app.get("/progress/{username}")
async def get_progress(username: str):

    user = await users_collection.find_one({"username": username})

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return {
        "current_level": user["current_level"],
        "questions_cleared": user["questions_cleared"],
        "score": user["score"]
    }

@app.post("/restart/{username}")
async def restart_game(username: str):

    user = await users_collection.find_one({"username": username})

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    await users_collection.update_one(
        {"username": username},
        {
            "$set": {
                "current_level": 1,
                "current_question_index": 0,
                "questions_cleared": 0,
                "score": 0,
                "game_completed": False
            }
        }
    )

    return {"message": "Game restarted successfully 🔄"}
