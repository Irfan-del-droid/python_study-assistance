"""
Study Assistant - A Rule-Based AI System
=========================================
This is a rule-based AI assistant that helps students with study-related queries.
It uses pattern matching and conditional logic to provide personalized responses.
"""

import re
from typing import List, Dict, Tuple


class StudyAssistant:
    """
    A rule-based AI system that provides study advice based on user inputs.
    """
    
    def __init__(self):
        """Initialize the Study Assistant with predefined rules and responses."""
        self.name = "StudyBot"
        self.conversation_history = []
        
        # Define keywords for different categories
        self.subject_keywords = {
            'math': ['math', 'mathematics', 'algebra', 'calculus', 'geometry', 'statistics'],
            'science': ['science', 'physics', 'chemistry', 'biology', 'experiment'],
            'language': ['english', 'language', 'grammar', 'writing', 'essay', 'vocabulary'],
            'history': ['history', 'historical', 'past', 'ancient', 'civilization'],
            'programming': ['programming', 'code', 'coding', 'python', 'java', 'javascript', 'algorithm']
        }
        
        self.time_keywords = ['time', 'schedule', 'when', 'how long', 'duration', 'hours']
        self.motivation_keywords = ['motivated', 'motivation', 'tired', 'lazy', 'procrastinate', 'difficult', 'hard']
        self.exam_keywords = ['exam', 'test', 'quiz', 'exam preparation', 'study for exam']
        self.method_keywords = ['how to study', 'study method', 'technique', 'strategy', 'approach', 'way']
        self.greeting_keywords = ['hello', 'hi', 'hey', 'greetings', 'good morning', 'good afternoon']
        self.help_keywords = ['help', 'what can you do', 'capabilities', 'assist']
        
    def normalize_input(self, user_input: str) -> str:
        """Convert input to lowercase and remove extra spaces."""
        return ' '.join(user_input.lower().split())
    
    def check_keywords(self, text: str, keyword_list: List[str]) -> bool:
        """Check if any keyword from the list appears in the text."""
        return any(keyword in text for keyword in keyword_list)
    
    def identify_subject(self, text: str) -> str:
        """Identify the subject mentioned in the user's query."""
        for subject, keywords in self.subject_keywords.items():
            if self.check_keywords(text, keywords):
                return subject
        return None
    
    def get_subject_advice(self, subject: str) -> str:
        """Return study advice specific to a subject."""
        advice = {
            'math': (
                "For Mathematics, I recommend:\n"
                "• Practice problems daily - math is about repetition\n"
                "• Understand concepts before memorizing formulas\n"
                "• Work through examples step-by-step\n"
                "• Review mistakes and understand why they happened\n"
                "• Use visual aids like graphs and diagrams when possible"
            ),
            'science': (
                "For Science subjects, I suggest:\n"
                "• Read the material before class to prepare\n"
                "• Take detailed notes during lectures\n"
                "• Create concept maps to connect ideas\n"
                "• Perform hands-on experiments when possible\n"
                "• Review diagrams and visual representations regularly"
            ),
            'language': (
                "For Language studies, try:\n"
                "• Read extensively to improve vocabulary\n"
                "• Practice writing daily, even just a paragraph\n"
                "• Use flashcards for vocabulary building\n"
                "• Engage in conversations or discussions\n"
                "• Review grammar rules with examples"
            ),
            'history': (
                "For History, I recommend:\n"
                "• Create timelines to visualize events\n"
                "• Focus on cause-and-effect relationships\n"
                "• Use mnemonic devices to remember dates\n"
                "• Connect historical events to current events\n"
                "• Summarize each chapter in your own words"
            ),
            'programming': (
                "For Programming, I suggest:\n"
                "• Code every day, even if just for 30 minutes\n"
                "• Build projects to apply what you learn\n"
                "• Read and understand others' code\n"
                "• Practice problem-solving on coding platforms\n"
                "• Debug systematically and learn from errors"
            )
        }
        return advice.get(subject, "I can help with study strategies for any subject!")
    
    def get_time_management_advice(self) -> str:
        """Provide time management and scheduling advice."""
        return (
            "For effective time management:\n"
            "• Use the Pomodoro Technique: 25 minutes study, 5 minutes break\n"
            "• Create a weekly schedule and stick to it\n"
            "• Prioritize difficult subjects when you're most alert\n"
            "• Break large tasks into smaller, manageable chunks\n"
            "• Review your schedule weekly and adjust as needed\n"
            "• Aim for 2-3 hours of focused study per day for each major subject"
        )
    
    def get_motivation_advice(self) -> str:
        """Provide motivation and encouragement."""
        return (
            "When you're feeling unmotivated:\n"
            "• Remember your goals and why you started\n"
            "• Start with just 5 minutes - momentum builds\n"
            "• Reward yourself after completing study sessions\n"
            "• Study with a friend or join a study group\n"
            "• Take care of your physical health: sleep, exercise, nutrition\n"
            "• Break tasks into smaller steps to avoid feeling overwhelmed\n"
            "• Remember: progress, not perfection!"
        )
    
    def get_exam_preparation_advice(self) -> str:
        """Provide exam preparation strategies."""
        return (
            "For exam preparation:\n"
            "• Start studying at least 2 weeks before the exam\n"
            "• Create a study schedule covering all topics\n"
            "• Review past exams and practice questions\n"
            "• Teach the material to someone else (Feynman Technique)\n"
            "• Use active recall: test yourself without looking at notes\n"
            "• Get adequate sleep the night before\n"
            "• Stay calm and confident - you've prepared for this!"
        )
    
    def get_study_method_advice(self) -> str:
        """Provide general study methods and techniques."""
        return (
            "Effective study methods include:\n"
            "• Active Recall: Test yourself without looking at notes\n"
            "• Spaced Repetition: Review material at increasing intervals\n"
            "• Interleaving: Mix different subjects/topics in one session\n"
            "• Elaboration: Explain concepts in your own words\n"
            "• Dual Coding: Combine words with visual representations\n"
            "• Retrieval Practice: Regularly test your knowledge\n"
            "• The Feynman Technique: Teach concepts to someone else"
        )
    
    def get_greeting_response(self) -> str:
        """Respond to greetings."""
        return (
            f"Hello! I'm {self.name}, your Study Assistant.\n"
            "I can help you with:\n"
            "• Subject-specific study tips\n"
            "• Time management strategies\n"
            "• Exam preparation advice\n"
            "• Study methods and techniques\n"
            "• Motivation and encouragement\n\n"
            "What would you like help with today?"
        )
    
    def get_help_response(self) -> str:
        """Provide help information."""
        return (
            "I can assist you with various study-related topics:\n\n"
            "Subject Help: Ask about studying math, science, language, history, or programming\n"
            "Time Management: Ask about schedules, study duration, or time planning\n"
            "Motivation: Share if you're feeling unmotivated or struggling\n"
            "Exam Prep: Get advice on preparing for exams and tests\n"
            "Study Methods: Learn about effective study techniques\n\n"
            "Just ask me a question in natural language, and I'll help!"
        )
    
    def process_query(self, user_input: str) -> str:
        """
        Main processing function that applies rules to determine the response.
        This is the core rule-based logic of the AI system.
        """
        normalized_input = self.normalize_input(user_input)
        self.conversation_history.append(("user", user_input))
        
        # Rule 1: Check for greetings
        if self.check_keywords(normalized_input, self.greeting_keywords):
            response = self.get_greeting_response()
            self.conversation_history.append(("assistant", response))
            return response
        
        # Rule 2: Check for exam-related queries
        if self.check_keywords(normalized_input, self.exam_keywords):
            subject = self.identify_subject(normalized_input)
            response = self.get_exam_preparation_advice()
            if subject:
                response += f"\n\n{self.get_subject_advice(subject)}"
            self.conversation_history.append(("assistant", response))
            return response
        
        # Rule 3: Check for subject-specific queries (before generic help)
        subject = self.identify_subject(normalized_input)
        if subject:
            response = self.get_subject_advice(subject)
            self.conversation_history.append(("assistant", response))
            return response
        
        # Rule 4: Check for time management queries
        if self.check_keywords(normalized_input, self.time_keywords):
            response = self.get_time_management_advice()
            self.conversation_history.append(("assistant", response))
            return response
        
        # Rule 5: Check for motivation-related queries
        if self.check_keywords(normalized_input, self.motivation_keywords):
            response = self.get_motivation_advice()
            self.conversation_history.append(("assistant", response))
            return response
        
        # Rule 6: Check for study method queries
        if self.check_keywords(normalized_input, self.method_keywords):
            response = self.get_study_method_advice()
            self.conversation_history.append(("assistant", response))
            return response
        
        # Rule 7: Check for help requests (after checking for specific topics)
        if self.check_keywords(normalized_input, self.help_keywords):
            response = self.get_help_response()
            self.conversation_history.append(("assistant", response))
            return response
        
        # Rule 8: Default response for unrecognized queries
        response = (
            "I understand you're asking about studying, but I'm not sure I caught that.\n"
            "Could you try rephrasing? I can help with:\n"
            "• Study tips for specific subjects (math, science, language, history, programming)\n"
            "• Time management and scheduling\n"
            "• Exam preparation\n"
            "• Study methods and techniques\n"
            "• Motivation and encouragement\n\n"
            "Or type 'help' to see what I can do!"
        )
        self.conversation_history.append(("assistant", response))
        return response
    
    def chat(self):
        """Interactive chat interface for the Study Assistant."""
        print("=" * 60)
        print("Welcome to Study Assistant - Your AI Study Companion!")
        print("=" * 60)
        print("Type 'quit' or 'exit' to end the conversation.\n")
        
        while True:
            user_input = input("You: ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'bye']:
                print(f"\n{self.name}: Goodbye! Good luck with your studies!")
                break
            
            if not user_input:
                continue
            
            response = self.process_query(user_input)
            print(f"\n{self.name}: {response}\n")
            print("-" * 60)


def main():
    """Main function to run the Study Assistant."""
    assistant = StudyAssistant()
    assistant.chat()


if __name__ == "__main__":
    main()

