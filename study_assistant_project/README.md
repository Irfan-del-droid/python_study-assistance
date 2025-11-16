# Study Assistant - Rule-Based AI System

A Python-based rule-based AI assistant that helps students with study-related queries using pattern matching and conditional logic.

## Project Overview

This project demonstrates a complete rule-based AI system that:
- Recognizes different types of study-related queries
- Provides personalized advice based on user inputs
- Uses keyword matching and pattern recognition
- Handles multiple conversation topics

## Project Structure

```
study_assistant_project/
├── api/                    # Vercel serverless functions (deployment)
│   ├── app.py             # Flask app for Vercel
│   └── study_assistant.py # Core logic for Vercel
├── src/                    # Source code for local development
│   ├── app.py             # Flask web application
│   ├── study_assistant.py # Rule-based AI logic
│   └── test_study_assistant.py # Test suite
├── docs/                   # Documentation
│   └── PROJECT_REPORT.md  # Complete project documentation
├── requirements.txt        # Python dependencies
├── vercel.json            # Vercel deployment configuration
├── .vercelignore          # Files to exclude from Vercel
└── README.md              # This file
```

## Files

- `src/study_assistant.py` - Main implementation with the rule-based AI logic
- `src/app.py` - Flask web application with embedded HTML, CSS, and JavaScript (local dev)
- `api/app.py` - Flask application configured for Vercel deployment
- `src/test_study_assistant.py` - Test script with 6 sample interactions
- `docs/PROJECT_REPORT.md` - Complete project documentation

## How to Run

### Web Application (Recommended)
Run the Flask web application:
```bash
# First, install dependencies
pip install -r requirements.txt

# Navigate to src directory
cd src

# Then run the web app
python app.py
```

Open your browser and navigate to `http://localhost:5000` to access the interactive web interface with a modern UI.

### Deploy to Vercel

This app is ready for deployment to Vercel:

1. **Install Vercel CLI** (optional, for local testing):
   ```bash
   npm install -g vercel
   ```

2. **Deploy to Vercel**:
   ```bash
   vercel
   ```

   Or connect your GitHub repository to Vercel for automatic deployments.

3. **Files for Vercel deployment**:
   - `vercel.json` - Vercel configuration (routes all requests to `/api/app.py`)
   - `api/app.py` - Flask application (Vercel serverless function)
   - `api/study_assistant.py` - Study Assistant core logic
   - `requirements.txt` - Python dependencies
   - `.vercelignore` - Files to exclude from deployment

**Important**: The Flask app is located in the `api/` directory as required by Vercel's Python runtime. Use `src/app.py` for local development.

The application is configured to work seamlessly on Vercel's serverless platform with all HTML, CSS, and JavaScript embedded in the Python code.

### Interactive Mode (Command Line)
Run the assistant in interactive chat mode:
```bash
cd src
python study_assistant.py
```

Type your questions and press Enter. Type 'quit' or 'exit' to end the conversation.

### Test Mode
Run the automated test suite:
```bash
cd src
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

