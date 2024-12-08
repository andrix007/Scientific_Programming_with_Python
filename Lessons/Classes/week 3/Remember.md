## Arbitrary Argument List

In Python, an **arbitrary argument list** allows a function to accept any number of arguments. This can be done using `*args` for non-keyword arguments and `**kwargs` for keyword arguments.

### Using `*args`
When you prefix a function parameter with an asterisk (`*`), it collects all the positional arguments passed to the function into a tuple. This allows you to pass a variable number of non-keyword arguments to the function.

#### Example
```python
def my_function(*args):
    for arg in args:
        print(arg)

# Calling the function with a varying number of arguments
my_function(1, 2, 3)
my_function('apple', 'banana', 'cherry')
```

**Output:**
```
1
2
3
apple
banana
cherry
```

### Using `**kwargs`
When you prefix a function parameter with two asterisks (`**`), it collects all the keyword arguments passed to the function into a dictionary. This allows you to pass a variable number of keyword arguments to the function.

#### Example
```python
def my_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Calling the function with a varying number of keyword arguments
my_function(name="John", age=25, country="USA")
my_function(fruit="apple", color="red")
```

**Output:**
```
name: John
age: 25
country: USA
fruit: apple
color: red
```

### Combining `*args` and `**kwargs`
You can use both `*args` and `**kwargs` in the same function to accept both positional and keyword arguments.

#### Example
```python
def my_function(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

# Calling the function with both positional and keyword arguments
my_function(1, 2, 3, name="John", age=25)
```

**Output:**
```
Positional arguments: (1, 2, 3)
Keyword arguments: {'name': 'John', 'age': 25}
```

### Summary
- `*args`: Collects all the positional arguments passed to the function into a tuple.
- `**kwargs`: Collects all the keyword arguments passed to the function into a dictionary.
- You can use both `*args` and `**kwargs` in a function to accept a combination of positional and keyword arguments. This makes your functions flexible and capable of handling a varying number of inputs.