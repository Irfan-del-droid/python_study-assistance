"""
Study Assistant Web Application
================================
Flask web application with embedded HTML, CSS, and JavaScript
to provide a web interface for the Study Assistant.
"""

from flask import Flask, request, jsonify, render_template_string
from study_assistant import StudyAssistant
import json

# Configure Flask - for local development (Vercel uses api/app.py)
app = Flask(__name__)
assistant = StudyAssistant()

# Embedded HTML template with CSS and JavaScript
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Study Assistant - AI Study Companion</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }

        .container {
            max-width: 900px;
            width: 100%;
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
            overflow: hidden;
            display: flex;
            flex-direction: column;
            height: 90vh;
            max-height: 800px;
        }

        .header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            text-align: center;
        }

        .header h1 {
            font-size: 2.5em;
            margin-bottom: 10px;
            font-weight: 600;
        }

        .header p {
            font-size: 1.1em;
            opacity: 0.9;
        }

        .chat-container {
            flex: 1;
            overflow-y: auto;
            padding: 30px;
            background: #f8f9fa;
            display: flex;
            flex-direction: column;
            gap: 15px;
        }

        .chat-container::-webkit-scrollbar {
            width: 8px;
        }

        .chat-container::-webkit-scrollbar-track {
            background: #f1f1f1;
        }

        .chat-container::-webkit-scrollbar-thumb {
            background: #888;
            border-radius: 4px;
        }

        .chat-container::-webkit-scrollbar-thumb:hover {
            background: #555;
        }

        .message {
            padding: 15px 20px;
            border-radius: 18px;
            max-width: 80%;
            word-wrap: break-word;
            line-height: 1.6;
            animation: fadeIn 0.3s ease-in;
            cursor: default;
            transition: transform 0.2s ease;
        }

        .message:hover {
            transform: translateX(2px);
        }

        @keyframes fadeIn {
            from {
                opacity: 0;
                transform: translateY(10px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .user-message {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            margin-left: auto;
            border-bottom-right-radius: 4px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }

        .assistant-message {
            background: white;
            color: #333;
            margin-right: auto;
            border-bottom-left-radius: 4px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
            border-left: 4px solid #667eea;
        }

        .assistant-message pre {
            white-space: pre-wrap;
            font-family: inherit;
            margin: 0;
        }

        .input-container {
            padding: 20px 30px;
            background: white;
            border-top: 1px solid #e0e0e0;
            display: flex;
            gap: 10px;
        }

        #userInput {
            flex: 1;
            padding: 15px 20px;
            border: 2px solid #e0e0e0;
            border-radius: 25px;
            font-size: 1em;
            outline: none;
            transition: all 0.3s ease;
            font-family: inherit;
        }

        #userInput:focus {
            border-color: #667eea;
            box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
            transform: translateY(-1px);
        }

        #userInput::placeholder {
            color: #999;
            transition: opacity 0.3s;
        }

        #userInput:focus::placeholder {
            opacity: 0.6;
        }

        #sendButton {
            padding: 15px 35px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 25px;
            font-size: 1em;
            cursor: pointer;
            transition: all 0.3s ease;
            font-weight: 600;
            position: relative;
            overflow: hidden;
            box-shadow: 0 4px 10px rgba(102, 126, 234, 0.3);
        }

        #sendButton::before {
            content: '';
            position: absolute;
            top: 50%;
            left: 50%;
            width: 0;
            height: 0;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.3);
            transform: translate(-50%, -50%);
            transition: width 0.6s, height 0.6s;
        }

        #sendButton:hover::before {
            width: 300px;
            height: 300px;
        }

        #sendButton:hover {
            transform: translateY(-3px);
            box-shadow: 0 6px 20px rgba(102, 126, 234, 0.5);
        }

        #sendButton:active {
            transform: translateY(-1px);
            box-shadow: 0 3px 10px rgba(102, 126, 234, 0.4);
        }

        #sendButton:disabled {
            opacity: 0.6;
            cursor: not-allowed;
            transform: none;
            box-shadow: none;
        }

        .loading {
            display: none;
            padding: 10px 20px;
            margin-right: auto;
            background: white;
            border-radius: 18px;
            border-bottom-left-radius: 4px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }

        .loading-dots {
            display: flex;
            gap: 5px;
        }

        .loading-dots span {
            width: 8px;
            height: 8px;
            background: #667eea;
            border-radius: 50%;
            animation: bounce 1.4s infinite ease-in-out;
        }

        .loading-dots span:nth-child(1) {
            animation-delay: -0.32s;
        }

        .loading-dots span:nth-child(2) {
            animation-delay: -0.16s;
        }

        @keyframes bounce {
            0%, 80%, 100% {
                transform: scale(0);
            }
            40% {
                transform: scale(1);
            }
        }

        @keyframes shake {
            0%, 100% { transform: translateX(0); }
            25% { transform: translateX(-10px); }
            75% { transform: translateX(10px); }
        }

        .message-enter {
            animation: slideIn 0.4s ease-out;
        }

        @keyframes slideIn {
            from {
                opacity: 0;
                transform: translateY(20px) scale(0.95);
            }
            to {
                opacity: 1;
                transform: translateY(0) scale(1);
            }
        }

        .welcome-message {
            text-align: center;
            padding: 40px 20px;
            color: #666;
        }

        .welcome-message h2 {
            color: #667eea;
            margin-bottom: 15px;
            font-size: 1.8em;
        }

        .welcome-message p {
            font-size: 1.1em;
            line-height: 1.8;
        }

        .suggestions {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin-top: 20px;
            justify-content: center;
        }

        .suggestion-chip {
            padding: 12px 24px;
            background: white;
            border: 2px solid #667eea;
            border-radius: 25px;
            cursor: pointer;
            transition: all 0.3s ease;
            font-size: 0.95em;
            color: #667eea;
            font-weight: 500;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
            user-select: none;
        }

        .suggestion-chip:hover {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            transform: translateY(-3px) scale(1.02);
            box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
            border-color: transparent;
        }

        .suggestion-chip:active {
            transform: translateY(-1px) scale(0.98);
        }

        @media (max-width: 768px) {
            .container {
                height: 100vh;
                max-height: 100vh;
                border-radius: 0;
            }

            .header h1 {
                font-size: 1.8em;
            }

            .message {
                max-width: 90%;
            }

            .input-container {
                padding: 15px 20px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📚 Study Assistant</h1>
            <p>Your AI Study Companion - Ask me anything about studying!</p>
        </div>
        
        <div class="chat-container" id="chatContainer">
            <div class="welcome-message">
                <h2>Hello! I'm StudyBot 👋</h2>
                <p>I can help you with:</p>
                <div class="suggestions">
                    <div class="suggestion-chip" onclick="sendSuggestion('How should I study for mathematics?')">Math Tips</div>
                    <div class="suggestion-chip" onclick="sendSuggestion('I have an exam next week')">Exam Prep</div>
                    <div class="suggestion-chip" onclick="sendSuggestion('Time management strategies')">Time Management</div>
                    <div class="suggestion-chip" onclick="sendSuggestion('I feel unmotivated')">Motivation</div>
                    <div class="suggestion-chip" onclick="sendSuggestion('Study methods and techniques')">Study Methods</div>
                </div>
            </div>
            <div class="loading" id="loadingIndicator">
                <div class="loading-dots">
                    <span></span>
                    <span></span>
                    <span></span>
                </div>
            </div>
        </div>
        
        <div class="input-container">
            <input type="text" id="userInput" placeholder="Ask me anything about studying..." onkeypress="handleKeyPress(event)">
            <button id="sendButton" onclick="sendMessage()">Send</button>
        </div>
    </div>

    <script>
        const chatContainer = document.getElementById('chatContainer');
        const userInput = document.getElementById('userInput');
        const sendButton = document.getElementById('sendButton');
        const loadingIndicator = document.getElementById('loadingIndicator');

        function addMessage(text, isUser) {
            const messageDiv = document.createElement('div');
            messageDiv.className = isUser ? 'message user-message' : 'message assistant-message';
            
            // Convert newlines to <br> and preserve formatting
            // Also handle bullet points and special characters
            let formattedText = text.replace(/\\n/g, '\n');
            formattedText = formattedText.replace(/\n/g, '<br>');
            // Format bullet points if they exist
            formattedText = formattedText.replace(/•/g, '<span style="margin-right: 8px;">•</span>');
            
            messageDiv.innerHTML = formattedText;
            messageDiv.classList.add('message-enter');
            
            // Add smooth scroll animation
            chatContainer.insertBefore(messageDiv, loadingIndicator);
            setTimeout(() => {
                chatContainer.scrollTo({
                    top: chatContainer.scrollHeight,
                    behavior: 'smooth'
                });
            }, 50);
        }

        function showLoading() {
            loadingIndicator.style.display = 'block';
            sendButton.disabled = true;
            chatContainer.scrollTop = chatContainer.scrollHeight;
        }

        function hideLoading() {
            loadingIndicator.style.display = 'none';
            sendButton.disabled = false;
        }

        async function sendMessage() {
            const message = userInput.value.trim();
            if (!message) {
                // Add shake animation if empty
                userInput.style.animation = 'shake 0.5s';
                setTimeout(() => {
                    userInput.style.animation = '';
                }, 500);
                return;
            }

            // Remove welcome message if it exists with fade out
            const welcomeMsg = chatContainer.querySelector('.welcome-message');
            if (welcomeMsg) {
                welcomeMsg.style.transition = 'opacity 0.3s';
                welcomeMsg.style.opacity = '0';
                setTimeout(() => {
                    welcomeMsg.remove();
                }, 300);
            }

            addMessage(message, true);
            userInput.value = '';
            userInput.focus();
            showLoading();

            try {
                // Use relative path for Vercel compatibility
                const apiUrl = window.location.pathname === '/' ? '/chat' : '/chat';
                const response = await fetch(apiUrl, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ message: message })
                });

                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }

                const data = await response.json();
                hideLoading();
                addMessage(data.response, false);
            } catch (error) {
                hideLoading();
                addMessage('Sorry, there was an error processing your request. Please try again.', false);
                console.error('Error:', error);
            }
        }

        function sendSuggestion(suggestion) {
            userInput.value = suggestion;
            sendMessage();
        }

        function handleKeyPress(event) {
            if (event.key === 'Enter') {
                sendMessage();
            }
        }

        // Focus input on load
        window.addEventListener('load', () => {
            userInput.focus();
        });
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    """Render the main chat interface."""
    return render_template_string(HTML_TEMPLATE)

@app.route('/chat', methods=['POST'])
def chat():
    """Handle chat messages from the frontend."""
    try:
        data = request.get_json()
        user_message = data.get('message', '')
        
        if not user_message:
            return jsonify({'response': 'Please enter a message.'}), 400
        
        # Process the query using the Study Assistant
        response = assistant.process_query(user_message)
        
        return jsonify({'response': response})
    
    except Exception as e:
        return jsonify({'response': f'An error occurred: {str(e)}'}), 500

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint."""
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    print("=" * 70)
    print("Study Assistant Web Application")
    print("=" * 70)
    print("\nStarting server...")
    print("Open your browser and navigate to: http://localhost:5000")
    print("\nPress Ctrl+C to stop the server.\n")
    app.run(debug=True, host='0.0.0.0', port=5000)