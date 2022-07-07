import math

def menu():
    print('--MENU--')
    print('1- Standard')
    print('2- Scientific')


def show_standard_menu():
    print('\n1- Add')
    print('2- Subtract')
    print('3- Multiplication')
    print('4- Division')
    print('5- Square root of x')
    print('6- x**2')
    print('7- 1 div x')
    print('8- Percent\n')


def add(nr1, nr2):
    return nr1 + nr2


def subtract(nr1, nr2):
    return nr1 - nr2


def multiplication(nr1, nr2):
    return nr1 * nr2


def division(nr1, nr2):
    return nr1 / nr2


def square_root_of_x(nr1):
    return math.sqrt(nr1)


def pow(nr1):
    return nr1**2


def one_div_x(nr1):
    return 1/nr1


def percent(nr1, nr2):
    return (nr1 / nr2) * 100


def one_parameter(input_operation, nr1):
    resultat = 0

    if input_operation == '5':
        resultat = square_root_of_x(nr1)
        print(f"Square root of {nr1} is = ", resultat)

    elif input_operation == '6':
        resultat = pow(nr1)
        print(f"{nr1} raised to the power of 2 =", resultat)

    elif input_operation == '7':
        resultat = one_div_x(nr1)
        print(f"1/{nr1} =", resultat)


def two_parameters(input_operation, nr1, nr2):
    resultat = 0

    if input_operation == '1':
        resultat = add(nr1, nr2)
        print(f"{nr1} + {nr2} =", resultat)
    elif input_operation == '2':
        resultat = subtract(nr1, nr2)
        print(f"{nr1} - {nr2} =", resultat)
    elif input_operation == '3':
        resultat = multiplication(nr1, nr2)
        print(f"{nr1} * {nr2} =", resultat)
    elif input_operation == '4':
        resultat = division(nr1, nr2)
        print(f"{nr1} / {nr2} =", resultat)
    elif input_operation == '8':
        resultat = percent(nr1, nr2)
        print(f"({nr1} / {nr2}) * 100 =", resultat)


if __name__ == '__main__':

    input_operation_tp = [1, 2, 3, 4, 8]
    input_operation_op = [5, 6, 7]
    flag = True

    while flag:
        menu()

        input_option = input("Choose the menu: ")

        if input_option == '1':
            show_standard_menu()
            input_operation = input("Choose the operation: ")
            if int(input_operation) in input_operation_tp:
                input_nr1 = int(input("Enter the first number: "))
                input_nr2 = int(input("Enter the second number: "))
                two_parameters(input_operation, input_nr1, input_nr2)

            elif int(input_operation) in input_operation_op:
                input_nr1 = int(input("Enter the first number: "))
                one_parameter(input_operation, input_nr1)


        elif input_option == '2':
            #TODO Scientific calculator
            print('Not implemented!')

        flag = False


