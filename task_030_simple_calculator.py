n1 = float(input("Enter first number: "))
sym = input("Enter operator (+, -, *, /): ")
n2 = float(input("Enter second number: "))

match sym:
    case "+":
        print(f"Result: {n1 + n2}")
    case "-":
        print(f"Result: {n1 - n2}")
    case "*":
        print(f"Result: {n1 * n2}")
    case "/":
        print(f"Result: {n1 / n2}" if n2 != 0 else "Error: Division by zero")
    case _:
        print("Invalid operator")
