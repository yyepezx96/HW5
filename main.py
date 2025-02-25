from calculator.commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

class CalculatorREPL:
    def __init__(self):
        self.commands = {
            'add': AddCommand(),
            'subtract': SubtractCommand(),
            'multiply': MultiplyCommand(),
            'divide': DivideCommand(),
        }

    def start(self):
        while True:
            print("Enter a command (add, subtract, multiply, divide) or 'exit' to quit:")

            user_input = input().strip().lower()

            if user_input == 'exit':
                print("Goodbye!")
                break

            # Command parsing: "command num1 num2"
            command_parts = user_input.split()
            if len(command_parts) == 3:
                command, num1, num2 = command_parts
                try:
                    num1, num2 = float(num1), float(num2)
                    if command in self.commands:
                        result = self.commands[command].execute(num1, num2)
                        print(f"Result: {result}")
                    else:
                        print("Invalid command. Try again.")
                except ValueError as e:
                    print(f"Error: {e}")
            else:
                print("Invalid input. Please provide a command and two numbers.")

if __name__ == "__main__":
    repl = CalculatorREPL()
    repl.start()

