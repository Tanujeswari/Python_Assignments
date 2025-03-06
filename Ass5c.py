class MyClass:
    static_variable = 10  

obj = MyClass()

obj.static_variable = 20

print(obj.static_variable)  
print(MyClass.static_variable)  
