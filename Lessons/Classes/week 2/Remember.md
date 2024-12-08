```python
# List Stuff
inventory.extend(["The Whale", "Pride and Prejudice", "The Catcher in the Rye"])
index_1984 = inventory.index("1984")
count_1984 = inventory.count("1984")

# List Comprehension
l = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
transposed = [[row[i] for row in matrix] for i in range(4)]
del a[2:4]

# Tuples
singletonTuple = 'Constructor University', 
prices = tuple(item[1] for item in inventory)
price_count = prices.count(0.5)
product_names = tuple(item[0] for item in inventory)
banana_index = product_names.index("banana")
sorted(x, key=lambda x: x[0])
# Dictionaries
courseList = [('Python', '1'), ('Java','3'), ('Kotlin', '2'), ('C++', '1'), ('C', '3')]
courses = dict(courseList)
courses = dict(Python='1', Java='3', Kotlin='2',CPP='1', C='3')

# Dict Comprehension
squares = {x: x**2 for x in (2, 4, 6)}

# Zipping
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):

# Sets
a = {x for x in 'aeiou' if x not in 'ai'} 
physics101_students = {"David", "Eve"}
all_students = math101_students.union(physics101_students)
common_students = math101_students.intersection(physics101_students)
only_math_students = math101_students.difference(physics101_students)
exclusive_students = math101_students.symmetric_difference(physics101_students)
is_subset = math101_students.issubset(physics101_students)
backup_students = chem101_students.copy()

# Pandas (no priority)
data = [10, 20, 30, 40, 50]
series = pd.Series(data)
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 27, 22, 32],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}
df = pd.DataFrame(data)
'Name': np.random.choice(names, 50),
'Age': np.random.randint(20, 60, size=50),
# Drop the 'City' column
df = df.drop('City', axis=1)
df['Salary'] = [70000, 80000, 75000, 90000]
```

# Iterable Objects in Python

In Python, an **iterable** is any object that can be looped over (i.e., you can iterate over its elements one by one). Iterable objects are those that implement the `__iter__()` or `__getitem__()` methods. Here’s a list of common iterable objects in Python:

## 2. **Non-Sequence Collections**

- **Sets (`set`)**: An unordered collection of unique elements, e.g., `{1, 2, 3}`.
- **Dictionaries (`dict`)**: A collection of key-value pairs, e.g., `{"a": 1, "b": 2}`.
- **Frozen Sets (`frozenset`)**: An immutable version of a set, e.g., `frozenset([1, 2, 3])`.
  
## 4. **Custom Iterables**

- **Custom Objects**: Any object can be made iterable by defining an `__iter__()` method that returns an iterator or a `__getitem__()` method that supports indexing.

## 5. **Iterators**

- **Generators (`generator`)**: A function that yields items one at a time, e.g., `(x**2 for x in range(5))`.
- **Iterator Objects**: Any object with a `__next__()` method and an `__iter__()` method that returns `self`.

## 7. **Other Built-in Iterables**

- **Enumerate (`enumerate`)**: Provides a counter along with the iterable elements, e.g., `enumerate(['a', 'b', 'c'])`.
- **Zip (`zip`)**: Combines multiple iterables into tuples, e.g., `zip([1, 2], ['a', 'b'])`.
- **Map (`map`)**: Applies a function to every item of an iterable, e.g., `map(str.upper, ['a', 'b', 'c'])`.
- **Filter (`filter`)**: Filters items from an iterable, e.g., `filter(lambda x: x > 0, [-1, 0, 1, 2])`.