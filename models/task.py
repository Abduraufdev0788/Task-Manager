from datetime import datetime
import manager import Manager

class Task:
    def __init__(self, title: str, description: str, created_at,deadline=None, complated=False):
        self.title = title
        self.description = description
        self.created_at = datetime.now()
        self.deadline = deadline
        self.complated = complated
    

    

