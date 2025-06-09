def add(n1 ,n2):
    return n1 + n2
def sub(n1 ,n2):
    return n1 - n2
def multi(n1 ,n2):
    return n1 * n2
def div(n1 ,n2):
    return n1 / n2

calculater = {
    "+" : add,
    "-" : sub,
    "*" : multi,
    "/" : div
}

def new_process():
    continue_process = True
    num1 = float(input("Enter the first number: "))

    while continue_process:
        for i in calculater:
            print(i)
        symbol = input("Pick the operation: ")
        num2 = float(input("Enter the second number: "))
        answer = calculater[symbol](num1,num2)
        print(f"{num1} {symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculation with {answer}, or type 'n' to start a new calulation")

        if choice == 'y':
            num1 = answer
        else:
            continue_process = False
            new_process()

new_process()