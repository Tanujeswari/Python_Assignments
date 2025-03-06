'''
 it is easy to understand all the methods in a single program 
 That's why i wrote this program in single way
'''
from abc import ABC, abstractmethod

# Step 1: Abstract class with abstract and non-abstract methods
class Animal(ABC):
    
    @abstractmethod
    def make_sound(self):
        pass  
    
    def sleep(self):
        print("The animal is sleeping.") 
    
# Step 2: Create a subclass for the abstract class
class Dog(Animal):
    

    def make_sound(self):
        print("Woof! Woof!")
        
# Step 3: Create an instance for the child class in the child class and call abstract methods
class Test:
    def __init__(self):
        self.dog = Dog() 
        
    def call_abstract_method(self):
        self.dog.make_sound()  
        
# Step 4: Create an instance for the child class in the child class and call non-abstract methods
    def call_non_abstract_method(self):
        self.dog.sleep()  
        
# Create an instance of Test class
test = Test()

# Call abstract method through the instance
test.call_abstract_method() 

# Call non-abstract method through the instance
test.call_non_abstract_method()  
