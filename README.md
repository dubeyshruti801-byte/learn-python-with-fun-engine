# learn-python-with-fun-engine
secure Python learning game engine with AST validation and sandboxed execution.
🚀 PyPlay Engine – Secure Python Learning Game
📌 Overview

PyPlay Engine is a modular Python-based learning system designed to help beginners practice Python fundamentals in a safe and interactive way.

The engine securely executes user-submitted Python code using sandboxing techniques, AST validation, and infinite loop detection.

This project focuses on building real software architecture while solving a real learning problem.

🎯 Features

Modular package structure (ui, engine, questions)

Secure exec() sandbox environment

Infinite loop detection using ast

Timeout protection using signal

Runtime error handling

Level-based question system

Score tracking system

Clean terminal-based user interface

🛡️ Security Implementation

The engine prevents unsafe execution by:

Parsing user code using ast

Detecting while True infinite loops

Using signal.alarm() to enforce execution time limits

Restricting global execution environment

Handling runtime exceptions safely

📂 Project Structure
Game engine-V1(Basic levels)/
│
├── ui/
│     └── main.py
│
├── engine/
│     ├── engine.py
│     ├── validation.py
│     └── __init__.py
│
├── questions/
│     ├── questionlevel1.py
│     └── __init__.py

▶️ How to Run

Clone the repository

Open terminal inside the project root directory

Run:

python -m ui.main


Make sure all folders contain __init__.py files.

🧠 Concepts Used

Python Packages & Modules

Relative and Absolute Imports

Abstract Syntax Tree (AST)

Sandboxed Code Execution

Timeout Handling with signal

Exception Handling

Modular Software Architecture

🚀 Future Improvements

GUI Version (Tkinter / PyQt)

Web Version (Flask / Django)

User Progress Tracking

Database Integration

Difficulty Levels

Leaderboard System

👨‍💻 Author
SHRUTI DUBEY
BCA Student | Python Developer

Your Name
BCA Student | Python Developer
LinkedIn: [Add Link]
GitHub: [Add Link]
