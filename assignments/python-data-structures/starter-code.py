# Python Data Structures Assignment
# Starter code for working with lists, dictionaries, sets, and tuples

# TODO: Task 1 - Lists and Tuples
def lists_and_tuples():
    # Lists - mutable ordered collections
    my_list = [1, 2, 3, 4, 5]
    print("Original list:", my_list)

    # List operations
    my_list.append(6)
    my_list.insert(0, 0)
    my_list.remove(3)
    print("Modified list:", my_list)

    # List comprehension
    squares = [x**2 for x in my_list]
    print("Squares:", squares)

    # Tuples - immutable ordered collections
    my_tuple = (1, 2, 3, "hello", "world")
    print("Tuple:", my_tuple)

    # Tuple unpacking
    a, b, c, *rest = my_tuple
    print(f"Unpacked: a={a}, b={b}, c={c}, rest={rest}")

# TODO: Task 2 - Dictionaries
def dictionaries():
    # Dictionary - key-value pairs
    my_dict = {
        "name": "Alice",
        "age": 25,
        "city": "New York"
    }
    print("Dictionary:", my_dict)

    # Dictionary operations
    my_dict["email"] = "alice@example.com"
    my_dict["age"] = 26
    print("Updated dict:", my_dict)

    # Dictionary methods
    print("Keys:", list(my_dict.keys()))
    print("Values:", list(my_dict.values()))
    print("Items:", list(my_dict.items()))

    # Dictionary comprehension
    squared_dict = {x: x**2 for x in range(1, 6)}
    print("Squared dict:", squared_dict)

# TODO: Task 3 - Sets
def sets():
    # Sets - unique unordered collections
    my_set = {1, 2, 3, 4, 5, 5, 4}  # Duplicates removed
    print("Set:", my_set)

    # Set operations
    my_set.add(6)
    my_set.discard(2)
    print("Modified set:", my_set)

    # Set operations with another set
    other_set = {4, 5, 6, 7, 8}
    print("Union:", my_set | other_set)
    print("Intersection:", my_set & other_set)
    print("Difference:", my_set - other_set)

    # Set comprehension
    even_squares = {x**2 for x in range(1, 11) if x**2 % 2 == 0}
    print("Even squares set:", even_squares)

# TODO: Task 4 - Data Structure Integration
def data_integration():
    # Combine all data structures
    students = [
        {
            "name": "Alice",
            "grades": [85, 92, 78],
            "courses": {"math", "science", "english"}
        },
        {
            "name": "Bob",
            "grades": [88, 79, 95],
            "courses": {"math", "history", "english"}
        }
    ]

    # Example operations
    all_courses = set()
    for student in students:
        all_courses.update(student["courses"])

    print("All unique courses:", all_courses)

    # Calculate average grades
    for student in students:
        avg_grade = sum(student["grades"]) / len(student["grades"])
        print(f"{student['name']}'s average grade: {avg_grade:.2f}")

if __name__ == "__main__":
    print("=== Lists and Tuples ===")
    lists_and_tuples()

    print("\n=== Dictionaries ===")
    dictionaries()

    print("\n=== Sets ===")
    sets()

    print("\n=== Data Structure Integration ===")
    data_integration()