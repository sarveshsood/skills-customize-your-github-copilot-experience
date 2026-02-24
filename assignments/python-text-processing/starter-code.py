# Python Text Processing Assignment
# Starter code for working with strings, file I/O, and text manipulation

# TODO: Task 1 - String Manipulation Basics
def string_basics():
    # Example string operations
    text = "Hello, World!"
    print(f"Original: {text}")
    print(f"Upper: {text.upper()}")
    print(f"Split: {text.split()}")
    # Add more string operations here

# TODO: Task 2 - File Input/Output Operations
def file_operations():
    # Example file operations
    try:
        # Writing to a file
        with open('sample.txt', 'w') as f:
            f.write("This is a sample text file.\n")
            f.write("It contains multiple lines.\n")

        # Reading from a file
        with open('sample.txt', 'r') as f:
            content = f.read()
            print("File content:")
            print(content)
    except Exception as e:
        print(f"Error: {e}")

# TODO: Task 3 - Text Processing Application
def text_processor():
    # Example text processing
    sample_text = """
    This is a sample text for processing.
    It contains words, sentences, and punctuation.
    Email: example@email.com
    Phone: 123-456-7890
    """

    # Basic word count
    words = sample_text.split()
    print(f"Word count: {len(words)}")

    # TODO: Add more advanced text processing features
    # - Find patterns (emails, phones)
    # - Generate statistics
    # - Save results to file

if __name__ == "__main__":
    print("=== String Basics ===")
    string_basics()

    print("\n=== File Operations ===")
    file_operations()

    print("\n=== Text Processor ===")
    text_processor()