import random
import re
from datetime import datetime

class AIKnowledgeChatbot:
    def __init__(self):
        self.name = "AI Tutor Bot"
        self.context = []
        
        # AI knowledge base from the PDF
        self.ai_knowledge = {
            'definition': {
                'patterns': [r'\bwhat is ai\b', r'\bdefine ai\b', r'\bai definition\b'],
                'responses': [
                    "AI (Artificial Intelligence) is a subfield of computer science that focuses on creating intelligent agents capable of performing tasks that typically require human-level intelligence, such as problem-solving, speech recognition, and decision-making.",
                    "Artificial Intelligence refers to man-made thinking power - systems that can sense, reason, act, and adapt to their environment."
                ]
            },
            'types': {
                'patterns': [r'\btypes of ai\b', r'\bai types\b', r'\bkinds of ai\b'],
                'responses': [
                    "There are three main types of AI:\n1. Narrow AI (ANI) - designed for specific tasks\n2. General AI (AGI) - can understand, learn, and apply intelligence across various tasks\n3. Superintelligent AI (ASI) - surpasses human intelligence in all fields"
                ]
            },
            'applications': {
                'patterns': [r'\bapplications\b', r'\bwhere.*used\b', r'\bexamples\b'],
                'responses': [
                    "AI applications include:\n• Natural Language Processing (NLP) - virtual assistants like Siri and Alexa\n• Image and Video Analysis - facial recognition, medical imaging\n• Robotics and Automation\n• Recommendation Systems\n• Healthcare - disease diagnosis, drug discovery\n• Financial Services - fraud detection, trading\n• Smart Homes and IoT\n• Gaming"
                ]
            },
            'machine_learning': {
                'patterns': [r'\bmachine learning\b', r'\bml\b', r'\blearn.*data\b'],
                'responses': [
                    "Machine Learning is the backbone of AI where algorithms learn from data without being explicitly programmed. It includes:\n• Supervised Learning - learning from labeled data\n• Unsupervised Learning - finding patterns in unlabeled data\n• Semi-supervised Learning - using limited labeled data\n• Reinforcement Learning - learning through trial and error"
                ]
            },
            'agents': {
                'patterns': [r'\bagent\b', r'\bintelligent agent\b', r'\brational agent\b'],
                'responses': [
                    "An intelligent agent perceives its environment through sensors and acts upon it through actuators. Types include:\n• Simple Reflex Agents\n• Model-Based Reflex Agents\n• Goal-Based Agents\n• Utility-Based Agents\n• Learning Agents"
                ]
            },
            'advantages': {
                'patterns': [r'\badvantage\b', r'\bbenefit\b', r'\bpros\b'],
                'responses': [
                    "Key advantages of AI:\n• High accuracy with fewer errors\n• High-speed processing and decision-making\n• High reliability and consistency\n• Useful for risky tasks (bomb defusing, ocean exploration)\n• Can work as digital assistants\n• Works as public utilities (self-driving cars, facial recognition)"
                ]
            },
            'disadvantages': {
                'patterns': [r'\bdisadvantage\b', r'\bdrawback\b', r'\bcons\b', r'\blimitation\b'],
                'responses': [
                    "AI limitations include:\n• High cost of implementation and maintenance\n• Cannot think outside the box\n• No feelings or emotions\n• Increased dependency on machines\n• No original creativity\n• Risk of job displacement"
                ]
            },
            'history': {
                'patterns': [r'\bhistory\b', r'\bturing\b', r'\b1950\b'],
                'responses': [
                    "AI development timeline:\n• 1950 - Alan Turing proposed the Turing test\n• 1956 - Birth of AI at Dartmouth Conference\n• 1966 - First chatbot ELIZA\n• 1972 - First intelligent robot WABOT-1\n• 1980s-1990s - Expert systems era\n• 1997 - IBM Deep Blue beats chess champion\n• 2011-present - Deep learning revolution with big data"
                ]
            }
        }
        
        self.default_responses = [
            "That's an interesting question about AI! Could you be more specific?",
            "I'm here to help you learn about Artificial Intelligence. What aspect would you like to explore?",
            "I can explain AI concepts, applications, machine learning, agents, and more. What interests you?",
            "Could you rephrase that? I'm specialized in AI fundamentals.",
        ]
    
    def get_response(self, user_input):
        """Generate a response based on user input"""
        user_input_lower = user_input.lower().strip()
        
        # Store context
        self.context.append(user_input_lower)
        
        # Check for pattern matches in knowledge base
        for topic, data in self.ai_knowledge.items():
            for pattern in data['patterns']:
                if re.search(pattern, user_input_lower):
                    return random.choice(data['responses'])
        
        # Default response if no pattern matches
        return random.choice(self.default_responses)
    
    def chat(self):
        """Main chat loop"""
        print(f"{self.name}: Hello! I'm an AI Tutor Bot with knowledge about Artificial Intelligence.")
        print(f"{self.name}: I can help you understand AI concepts, types, applications, machine learning, agents, and more.")
        print(f"{self.name}: Type 'quit' or 'exit' to end our conversation.\n")
        
        while True:
            user_input = input("You: ").strip()
            
            if not user_input:
                print(f"{self.name}: Please ask me something about AI!\n")
                continue
            
            if user_input.lower() in ['quit', 'exit', 'bye', 'goodbye']:
                print(f"{self.name}: Thank you for learning about AI with me! Goodbye!\n")
                break
            
            response = self.get_response(user_input)
            print(f"{self.name}: {response}\n")


# Run the chatbot
if __name__ == "__main__":
    bot = AIKnowledgeChatbot()
    bot.chat()