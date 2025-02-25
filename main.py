from calculator import Calculator

def main():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        operation = input("Enter operation (add, subtract, multiply, divide): ")

        calc = Calculator()

        if operation == 'add':
            result = calc.add(a, b)
        elif operation == 'subtract':
            result = calc.subtract(a, b)
        elif operation == 'multiply':
            result = calc.multiply(a, b)
        elif operation == 'divide':
            if b == 0:
                result = "Cannot divide by zero."
            else:
                result = calc.divide(a, b)
        else:
            result = "Unknown operation."

        print(f"The result is: {result}")

    except ValueError:
        print("Invalid number input.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

