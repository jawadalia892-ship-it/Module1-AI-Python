"""
Simple Python Calculator - Mini Project
Supports: Addition, Subtraction, Multiplication, Division,
          Power, and Modulus
"""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def power(a, b):
    return a ** b

def modulus(a, b):
    if b == 0:
        return "Error: Modulus by zero is not allowed."
    return a % b


def get_number(prompt):
    """Keep asking until the user enters a valid number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a number.\n")


def main():
    print("=" * 40)
    print("        PYTHON CALCULATOR")
    print("=" * 40)

    operations = {
        "1": ("Addition (+)", add),
        "2": ("Subtraction (-)", subtract),
        "3": ("Multiplication (*)", multiply),
        "4": ("Division (/)", divide),
        "5": ("Power (^)", power),
        "6": ("Modulus (%)", modulus),
    }

    while True:
        print("\nChoose an operation:")
        for key, (label, _) in operations.items():
            print(f"  {key}. {label}")
        print("  7. Exit")

        choice = input("\nEnter choice (1-7): ").strip()

        if choice == "7":
            print("\nThank you for using the calculator. Goodbye!")
            break

        if choice not in operations:
            print("Invalid choice! Please select a valid option.\n")
            continue

        label, func = operations[choice]
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        result = func(num1, num2)
        print(f"\nResult ({label}): {result}")


if __name__ == "__main__":
    main()
