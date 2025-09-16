# 1. Use Python functions for addition, subtraction, multiplication, and division.
def add(x, y):
    
    return x + y

def subtract(x, y):
    
    return x - y

def multiply(x, y):
    
    return x * y

def divide(x, y):
    
    if y == 0:
       
        raise ZeroDivisionError("Cannot divide by zero.")
    return x / y


while True:
    print("\n" + "="*25)
    print("   Python Calculator 🧮")
    print("="*25)
    print("Select an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("Enter 'exit' to quit")

   
    choice = input("Enter choice (1/2/3/4/exit): ")

    
    if choice.lower() == 'exit':
        print("Exiting the calculator. Goodbye! 👋")
        break

    
    if choice in ('1', '2', '3', '4'):
        
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if choice == '1':
                result = add(num1, num2)
               
                print(f" Result: {num1} + {num2} = {result}")

            elif choice == '2':
                result = subtract(num1, num2)
                print(f" Result: {num1} - {num2} = {result}")

            elif choice == '3':
                result = multiply(num1, num2)
                print(f" Result: {num1} * {num2} = {result}")

            elif choice == '4':
                result = divide(num1, num2)
                print(f" Result: {num1} / {num2} = {result}")

        except ValueError:
            
            print(" Invalid input. Please enter numbers only.")
        except ZeroDivisionError as e:
            
            print(f" Error: {e}")
        except Exception as e:
            
            print(f"An unexpected error occurred: {e}")
    else:
        print(" Invalid choice. Please select a valid option.")