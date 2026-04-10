class Calculator:
    # Addition
    def add(self,a,b):
        return a+b
    
    # Subtraction
    def subs(self,a,b):
        return a-b
    
    # Division
    def divide(self,a,b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a/b