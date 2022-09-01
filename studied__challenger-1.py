

playing = True


while playing:
    user__choice = int(input("Choose a number: \n "))
    user__another__choice = int(input("Choose another one:\n "))

    operation = input(
        "Choose an operation: \n  Options are: +, -, * or /.\n  Write 'exit' to finish\n ")

    def plus():
        operation = user__choice+user__another__choice
        print(operation)

    def minus():
        operation = user__choice - user__another__choice
        print(operation)

    def multiply():
        operation = user__choice*user__another__choice
        print(operation)

    def divide():
        operation = user__choice/user__another__choice
        print(operation)

    if operation == '+':
        plus()
    elif operation == '-':
        minus()
    elif operation == "*":
        multiply()
    elif operation == "/":
        divide()
    elif operation == "exit":
        playing = False

    else:
        playing = False
