# input
N1 = int(input())
N2 = int(input())
operator = input()

# logic and print
if operator == "+":
    result = N1 + N2
    result_type = "even" if result % 2 == 0 else "odd"
    print(f"{N1} + {N2} = {result} - {result_type}")
elif operator == "-":
    result = N1 - N2
    result_type = "even" if result % 2 == 0 else "odd"
    print(f"{N1} - {N2} = {result} - {result_type}")
elif operator == "*":
    result = N1 * N2
    result_type = "even" if result % 2 == 0 else "odd"
    print(f"{N1} * {N2} = {result} - {result_type}")
elif operator == "/":
    if N2 == 0:
        print(f"Cannot divide {N1} by zero")
    else:
        result = N1 / N2
        print(f"{N1} / {N2} = {result:.2f}")
elif operator == "%":
    if N2 == 0:
        print(f"Cannot divide {N1} by zero")
    else:
        result = N1 % N2
        print(f"{N1} % {N2} = {result}")
