def divide(num1, num2):
    if num2 == 0:
        return None
    return num1 / num2

def exponentiate(base, exponent):
    return base ** exponent

def remainder(num1, num2):
    if num2 == 0:
        return None
    return num1 % num2

def summation(start, end):
    if end <= start:
        return None
    return sum(range(start, end + 1))

def main():
    while True:
        print("\nMenu:")
        print("[D] - Divide")
        print("[E] - Exponentiation")
        print("[R] - Remainder")
        print("[F] - Summation")
        print("[Q] - Quit")
        
        choice = input("Enter your choice: ").strip().upper()
        
        if choice == 'Q':
            print("Exiting the program.")
            break
        
        if choice == 'D':
            num1 = float(input("Enter the numerator: "))
            num2 = float(input("Enter the denominator: "))
            result = divide(num1, num2)
            if result is None:
                print("Error: Denominator cannot be zero.")
            else:
                print(f"Result: {result}")

        elif choice == 'E':
            base = float(input("Enter the base: "))
            exponent = float(input("Enter the exponent: "))
            result = exponentiate(base, exponent)
            print(f"Result: {result}")

        elif choice == 'R':
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = remainder(num1, num2)
            if result is None:
                print("Error: Denominator cannot be zero.")
            else:
                print(f"Result: {result}")

        elif choice == 'F':
            start = int(input("Enter the first number (start): "))
            end = int(input("Enter the second number (end): "))
            result = summation(start, end)
            if result is None:
                print("Error: The second number must be greater than the first number.")
            else:
                print(f"Result: {result}")

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()