# Calculator 

# add
def add(n1, n2):
    return n1 + n2

# substract
def sub(n1, n2):
    return n1- n2

# multiply
def multiply(n1, n2):
    return n1 * n2

# divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": sub,
    "*": multiply,
    "/": divide

}

num1 = int(input("What's the first number?: "))

for symbol in operations:
    print(symbol)
should_continue = True

while should_continue:
    operation_symbol = input("Pick an operation from the line above: ")

    num2 = int(input("What's the second number?: "))

    calculation_function = operations[operation_symbol];
    answer = calculation_function(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue clalculating with {answer} or type 'n' to start from the beginning: ") == 'y':
        num1 = answer
    else:
        should_continue = False;