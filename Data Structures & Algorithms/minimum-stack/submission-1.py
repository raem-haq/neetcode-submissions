class MinStack:
    def __init__(self):
        self.elementstack = []
        self.mintracker = []

    def push(self, val: int) -> None:
        self.elementstack.append(val)
        if self.mintracker:
            self.mintracker.append(min(self.mintracker[-1], val))
        else:
            self.mintracker.append(val)
        
    def pop(self) -> None:
        self.elementstack.pop()
        self.mintracker.pop()

    def top(self) -> int:
        return self.elementstack[-1]
        

    def getMin(self) -> int:
        return self.mintracker[-1]
        
