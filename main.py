from art import logo


def add(n1, n2):
    """This function takes two values and adds them"""
    return n1 + n2


def subtract(n1, n2):
    """This function takes two values and subtracts them"""
    return n1 - n2


def multiply(n1, n2):
    """This function takes two values and multiplies them"""
    return n1 * n2


def division(n1, n2):
    """This function takes two values and divides them"""
    return n1 / n2


def continue_with_the_previous_value(value_total):
    auxiliar = value_total
    new_total_intern = 0

    user_question = input(
        f"Type 'y' to continue calculating with {auxiliar}, or type 'n' to start a new calculation: ").lower()

    while user_question == "y":
        print("+\n-\n*\n/")
        user_inter_oper = input("Pick an operation: ")
        next_intern_number = float(input("What's the next number?: "))

        for operationIntern in operations:
            if operationIntern == user_inter_oper:
                new_total_intern = operations[operationIntern](auxiliar, next_intern_number)
                print(f"{auxiliar} {user_inter_oper} {next_intern_number} = {new_total_intern}")

        auxiliar = new_total_intern
        user_question = input(
            f"Type 'y' to continue calculating with {auxiliar}, or type 'n' to start a new calculation: ").lower()

    print("\n" * 200)


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": division
}

total = 0
while True:
    print(logo)

    first_number = float(input("What's the first number?: "))
    print("+\n-\n*\n/")
    user_operation = input("Pick an operation: ")
    next_number = float(input("What's the next number?: "))

    for operation in operations:
        if operation == user_operation:
            total = operations[operation](first_number, next_number)
            print(f"{first_number} {user_operation} {next_number} = {total}")

    continue_with_the_previous_value(total)
