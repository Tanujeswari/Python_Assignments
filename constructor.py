class SuperClass:
    def __init__(self, arg1=None, arg2=None):
        # Constructor with arguments (Public)
        if arg1 and arg2:
            print(f"SuperClass Constructor with two arguments called: {arg1} and {arg2}")
        elif arg1:
            print(f"SuperClass Constructor with one argument called: {arg1}")
        else:
            print("SuperClass Default Constructor called")

class ChildClass(SuperClass):
    def __init__(self, arg1=None):
        # Calling the superclass constructor using `super()`
        super().__init__(arg1)  # One-argument constructor of the superclass
        if arg1:
            print(f"ChildClass Constructor with one argument called: {arg1}")
        else:
            print("ChildClass Default Constructor called")

# Calling constructors from the child class
child1 = ChildClass()   # Calls default constructor of SuperClass through ChildClass
child2 = ChildClass("Argument 1")  # Calls constructor with an argument of SuperClass
