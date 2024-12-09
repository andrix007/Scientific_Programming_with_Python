# OOP

```python
class MyClass:
    # Class variable (shared by all instances of the class)
    class_variable = "I am a class variable"
    
    # Constructor (Initializer method)
    def __init__(self, instance_variable):
        # Instance variable (unique to each instance)
        self.instance_variable = instance_variable
        print(f"Object created with instance variable: {self.instance_variable}")

    # Instance method (works with instance-specific data)
    def instance_method(self):
        print(f"This is an instance method and the instance variable is: {self.instance_variable}")
    
    # Class method (works with the class variable)
    @classmethod
    def class_method(cls):
        print(f"This is a class method and the class variable is: {cls.class_variable}")

    # Static method (works independently of class and instance variables)
    @staticmethod
    def static_method():
        print("This is a static method and does not access class or instance variables.")

# Example of how to create an instance of MyClass and use its methods
obj = MyClass("Sample Value")  # Calls the __init__ method
obj.instance_method()          # Calls an instance method
MyClass.class_method()         # Calls the class method
MyClass.static_method()        # Calls the static method
```

```python
# multiple init methods and the effect of order of definitions (last one counts)
class Box:

    def __init__(self, l, w, h):
        self.length = l
        self.width = w
        self.height = h
    def __init__(self, l, w, h, n):
        self.length = l
        self.width = w
        self.height = h
        self.name = n
```

