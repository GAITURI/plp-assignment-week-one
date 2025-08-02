# This is a simple Python program that acts as a basic calculator.
# It takes two numbers and an operator as input from the user.

def simple_calculator():
    """
    Performs a simple mathematical operation based on user input.
    """
    try:
        # Prompt the user for the first number and convert the input to a float.
        num1 = float(input("Enter the first number: "))
        
        # Prompt the user for the second number and convert the input to a float.
        num2 = float(input("Enter the second number: "))
        
        # Prompt the user for the mathematical operation.
        operator = input("Enter the operation (+, -, *, /): ")

        # Initialize the result variable.
        result = 0
        
        # Use a series of if/elif/else statements to determine which operation to perform.
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            # Handle the case of division by zero to prevent an error.
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                return
            result = num1 / num2
        else:
            # If the user enters an invalid operator, print an error message.
            print(f"Error: Invalid operator '{operator}'. Please use one of +, -, *, /.")
            return

        # Print the final result in the requested format.
        # The f-string formats the output nicely, showing the original numbers and the operator.
        print(f"{num1} {operator} {num2} = {result}")

    except ValueError:
        # This block catches errors if the user enters non-numeric input for the numbers.
        print("Error: Invalid input. Please enter numbers for the operands.")

# Call the function to run the program.
simple_calculator()
