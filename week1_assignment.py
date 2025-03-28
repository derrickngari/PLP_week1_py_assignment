def main():
    while (True):
        num1 = int(input("Enter first Number: "))
        num2 = int(input("Enter Second Number: "))
        results = 0

        operation = input("Choose an operation (+, -, *, /): ")

        if (operation == '+'):
            results = num1 + num2
        elif (operation == '-'):
            results = num1 - num2
        elif (operation == '*'):
            results = num1 * num2
        elif (operation == '/'):
            results = num1 / num2
        else:
            print("Invalid Operation")
            break

        print(f"{num1} {operation} {num2} = {results}")

main()