# Task 1: Sum of a List of Integers
try:
    # Get user input for a list of integers
    input_str = input("Enter a list of integers, separated by spaces: ")
    my_list = list(map(int, input_str.split()))

    # Compute and print the sum
    total_sum = sum(my_list)
    print(f"The sum of the integers in the list is: {total_sum}")

except ValueError:
    print("Invalid input. Please enter only integers.")

# ---

# Task 2: Favorite Books Tuple
# Create a tuple of your five favorite books
favorite_books = ("The Alchemist", "Sapiens", "Dune", "1984", "The Lord of the Rings")

# Use a for loop to print each book name on a new line
print("\nMy Favorite Books:")
for book in favorite_books:
    print(book)

# ---

# Task 3: Person's Information Dictionary
# Create an empty dictionary
person_info = {}

# Ask the user for input and store it in the dictionary
print("\nEnter your personal information:")
person_info['name'] = input("Name: ")
person_info['age'] = int(input("Age: "))
person_info['favorite_color'] = input("Favorite color: ")

# Print the dictionary to the console
print("\nHere is the information you entered:")
print(person_info)

# ---

# Task 4: Common Elements in Two Sets
try:
    # Get user input for two sets of integers
    set1_input = input("\nEnter integers for the first set, separated by spaces: ")
    set1 = set(map(int, set1_input.split()))

    set2_input = input("Enter integers for the second set, separated by spaces: ")
    set2 = set(map(int, set2_input.split()))

    # Find the common elements and create a new set
    common_elements = set1.intersection(set2)

    # Print the new set
    print(f"The common elements in both sets are: {common_elements}")

except ValueError:
    print("Invalid input. Please enter only integers.")

# ---

# Task 5: List Comprehension for Odd-Length Words
# Store a list of words
words = ["python", "is", "a", "great", "language", "for", "coding"]

# Use list comprehension to create a new list with odd-length words
odd_length_words = [word for word in words if len(word) % 2 != 0]

# Print the new list
print(f"\nOriginal list of words: {words}")
print(f"Words with an odd number of characters: {odd_length_words}")