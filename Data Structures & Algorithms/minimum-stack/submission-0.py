class MinStack:

    def __init__(self):
        self.stack = []
        self.prefix = []
        

    def push(self, val: int) -> None:
        if self.prefix:
            self.prefix.append(min(self.stack[-1], self.prefix[-1]))
        else:
            self.prefix.append(float("infinity"))
        
        self.stack.append(val)

        

    def pop(self) -> None:
        self.stack.pop(-1)
        self.prefix.pop(-1)
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return min(self.prefix[-1], self.stack[-1])
        
