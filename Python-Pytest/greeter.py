class Greeter:
    def __init__(self,name):
        self.name = name
        
    def say_hello(self):
        return f"Hello, {self.name}"