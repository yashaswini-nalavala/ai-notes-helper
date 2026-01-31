# AI Notes Helper

## Problem Statement
Students often struggle to quickly understand long notes or study material.
This project helps students generate concise summaries from raw notes.

## Solution
AI Notes Helper is a simple web-based application that summarizes student notes
using prompt-based AI workflow.

## Architecture Diagram (Simple)
User → Web Interface → Backend (Flask) → AI Logic → Summary Output

## Tech Stack
- Python
- Flask
- HTML
- GitHub

## AI Tools Used
- Prompt engineering
- Simulated AI logic (no API dependency)

## Prompt Strategy Summary
Prompts are designed to:
- Extract key ideas
- Simplify content
- Use student-friendly language

Prompt file location:
`prompts/summary.txt`

## Setup Instructions (Build Reproducibility)
1. Clone the repository
2. Install dependencies:
--> pip install flask
3. Run the application:
--> python app.py
4. Open browser:
[AI Notes Helper](http://127.0.0.1:5000)


## Final Output
The application displays a summarized version of the input notes.

## AI Integration Note
Due to API limitations, AI responses are simulated.
The project focuses on AI workflow, prompt design, and system architecture.
Real AI APIs can be integrated in future versions.
