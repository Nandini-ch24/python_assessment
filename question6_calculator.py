def calculator(a, b, choice):
    if choice == '+':
        return a + b;
    elif choice == '-':
        return a - b;
    elif choice == '*':
        return a * b;
    elif choice == '/':
        if b != 0:
            return a/b;
        else:
            return "cannot divided by zero";
    else:
        return "Invalid operator";
a=float(input("Enter first number: "));
b=float(input("Enter second number: "));
choice=input("Enter operator (+, -, *, /): ");
result = calculator(a, b, choice);
print("Result: ", result);