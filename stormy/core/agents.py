class Agent:
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role

    def act(self, task: str) -> str:
        return f"[{self.name} as {self.role}]: Processing → {task}"
