🚀 Learn Python With Fun – Game Engine (FastAPI Version)

A secure, level-based Python learning game engine with FastAPI backend and MongoDB integration.

📌 Overview

Learn Python With Fun is a structured Python learning platform that allows users to solve coding challenges level-by-level in a controlled environment.

The system includes:

A secure execution engine with AST validation

Backend built using FastAPI

MongoDB-based user progress tracking

Controlled progression system

Replayable practice mode

This project demonstrates real backend architecture, API design, and database-driven state management.

🏗️ Tech Stack

Python

FastAPI

MongoDB (MongoDB Atlas)

Motor (Async MongoDB Driver)

AST (Abstract Syntax Tree)

Secure sandboxed execution

Swagger UI (Auto-generated API docs)

🎯 Core Features
🧠 Secure Code Execution

AST parsing and validation

Infinite loop detection

Restricted execution environment

Runtime error handling

🎮 Game Engine Logic

Level-based progression

Question-by-question validation

Score tracking

Level completion detection

Game completion state

Replay system (/restart endpoint)

🌐 FastAPI Backend

/start – Start new game

/question/{username} – Get current question

/submit – Submit solution (backend-controlled progression)

/progress/{username} – View user progress

/restart – Restart completed game

🗄️ MongoDB Integration

Stores:

username

current_level

current_question_index

questions_cleared

levels_cleared

score

game_completed

Backend fully controls progression logic

Prevents skipping levels

Prevents duplicate submissions

📂 Project Structure
app/
│
├── engine/
│     ├── engine.py
│     ├── validation.py
│
├── questions/
│     ├── questionlevel1.py
│     ├── questionlevel2.py
│     ├── questionlevel3.py
│     ├── questionlevel4.py
│     ├── questionlevel5.py
│
├── database/
│     └── mongodb.py
│
├── main.py
│
requirements.txt

▶️ How To Run Locally

Clone repository

Create virtual environment

python -m venv venv
venv\Scripts\activate


Install dependencies

pip install -r requirements.txt


Create .env file:

MONGODB_URL=your_mongodb_connection_string


Run server:

uvicorn app.main:app --reload


Open Swagger UI:

http://127.0.0.1:8000/docs

🛡️ Security Implementation

The engine prevents unsafe execution by:

Parsing user code using AST

Detecting infinite loops

Restricting execution scope

Enforcing execution timeout

Catching runtime errors safely

🧠 Concepts Demonstrated

REST API Design

Async Programming (FastAPI + Motor)

Database-driven state management

Secure code execution

Backend-controlled progression

Clean modular architecture

Version control & branch management

🚀 Future Improvements

Frontend UI (React / Next.js)

Authentication (JWT)

Leaderboard system

Best score tracking

Docker deployment

Cloud hosting (Render / Railway / AWS)

👩‍💻 Author

Shruti Dubey
BCA Student | Python Backend Developer
