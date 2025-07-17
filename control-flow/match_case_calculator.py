
first_number = int(input("Enter the first number :"))
second_number = int(input("Enter the second number :"))
operation = input("Choose the operation (+, -, *, /):")


match operation :
    case "+":
        summation = first_number + second_number
        print(f"The result is {summation}")
    case "-" :
        subtraction = first_number - second_number
        print(f"The result is {subtraction}")
    case "*" :
        multiplication = first_number * second_number
        print(f"The result is {multiplication}")
    case "/" :
        if second_number != 0:
            division = first_number / second_number
            print(f"The result is {division}.")
        else:
            print("Cant divide a number by zero!")
    case _:
        print("Unexpected error! try again!")
