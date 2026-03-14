class AIEngine:
    def __init__(self):
        self.name = "Stormy Core v0.1"
        self.memory = []  # placeholder

    def think(self, user_message: str) -> str:
        # Very dumb version for now – later: call LLM, use tools, etc.
        self.memory.append(user_message)
        if "hello" in user_message.lower():
            return "Hey there! I'm Stormy. What can I help with?"
        if "time" in user_message.lower():
            from datetime import datetime
            return f"Current time is {datetime.now().strftime('%H:%M:%S')}"
        return f"You said: {user_message}\n(I'm still very basic – upgrade me!)"

    def process(self, message: str, context: dict = None) -> dict:
        response = self.think(message)
        return {
            "response": response,
            "model": self.name,
            "memory_length": len(self.memory)
        }
