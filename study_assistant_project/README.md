# Study Assistant - Rule-Based AI System

A Python-based rule-based AI assistant that helps students with study-related queries using pattern matching and conditional logic.

## Project Overview

This project demonstrates a complete rule-based AI system that:
- Recognizes different types of study-related queries
- Provides personalized advice based on user inputs
- Uses keyword matching and pattern recognition
- Handles multiple conversation topics

## Files

- `study_assistant.py` - Main implementation with the rule-based AI logic
- `app.py` - Flask web application with embedded HTML, CSS, and JavaScript
- `test_study_assistant.py` - Test script with 6 sample interactions
- `PROJECT_REPORT.md` - Complete project documentation
- `README.md` - This file

## How to Run

### Interactive Mode (Command Line)
Run the assistant in interactive chat mode:
```bash
python study_assistant.py
```

Type your questions and press Enter. Type 'quit' or 'exit' to end the conversation.

### Test Mode
Run the automated test suite:
```bash
python test_study_assistant.py
```

This will execute 6 test cases and display the results.

## Features

The Study Assistant can help with:
- Subject-specific study tips (Math, Science, Language, History, Programming)
- Time management strategies
- Exam preparation advice
- Study methods and techniques
- Motivation and encouragement

## Example Queries

- "How should I study for mathematics?"
- "I have an exam next week, how should I prepare?"
- "I'm feeling unmotivated"
- "What's the best way to manage my study time?"
- "Can you help me with programming?"

## Requirements

- Python 3.x
- Flask 3.0.0+ (for web application)
- Werkzeug 3.0.1+

Install dependencies:
```bash
pip install -r requirements.txt
```

## Project Structure

The system uses a hierarchical rule-based approach:
1. Input normalization
2. Keyword pattern matching
3. Rule evaluation (in priority order)
4. Response generation
5. Conversation history tracking

For detailed information, see `PROJECT_REPORT.md`.


