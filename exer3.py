# Exercise 3: Arithmetic Operations
# A program that asks the user for two positive integers, x (must be even integer) and y (must be odd
# integer), and performs the following operations on those integers:
#     1. Summation (computes the summation of squares of all even integers from 1 to x)
#     2. Box (prints NxN box pattern using *)
#     3. Average (computes the average of odd integers from 1 to x)

# Programmed by: John Robertson C. Despi | CMSC 12 B-3L

def summation(x):
    """
    Computes the summation of squares of all even integers from 1 to x.

    :param x: a positive integer
    :return: summation of squares of all even integers from 1 to x

    """
    sum = 0
    for i in range(1, x + 1):
        if is_Even(i):
            sum += (i * i)
    return sum


def box(N):
    """
    Prints NxN box pattern using *.

    :param N: Box size.
    :return: None
    """
    print()
    for i in range(N):
        for j in range(N):
            print('*', end='')
        print()


def average(x):
    count = 0
    sum = 0
    for i in range(1, x + 1):
        if is_Odd(i):
            sum += i
            count += 1
    return sum / count


def menu():
    """
    A function that prints the menu and prompts the user for what their choice is.

    :return: Integer choice inputted by user.
    """
    while True:
        print("\nPlease Choose from the following:\n"
              "1. Summation\n"
              "2. Box\n"
              "3. Average\n"
              "0. Exit")
        choice = int(input("Enter your choice: "))

        return choice


def is_Even(x):
    """
    A boolean function that checks if x is an even integer or not.

    :param x: integer value to check.
    :return: Boolean value indicating whether x is even.

    """
    if x % 2 == 0:
        even = True
    else:
        even = False
    return even


def is_Odd(y):
    """
    A boolean function that checks if y is an odd integer or not.

    :param y: integer value to check.
    :return: Boolean value indicating whether y is odd.
    """
    if is_Even(y):
        odd = False
    else:
        odd = True
    return odd


def is_Negative(x):
    """
    A boolean function that checks if x is negative.

    :param x: integer value to check.
    :return: Boolean value indicating whether x is negative.
    """
    if x < 0:
        return True
    return False


def get_Input():
    """
    A function for asking positive even int x and positive odd int y from the user with error checking.

    :return: x and y integer values inputted by the user.
    """
    while True:
        x = int(input("Enter value for x: "))
        y = int(input("Enter value for y: "))

        if is_Negative(x) or is_Negative(y):
            print("x and y must be both POSITIVE integers!\n")

        elif is_Odd(x):
            print("x must be EVEN integer!\n")
            if is_Even(y):
                print("y must be ODD integer!\n")

        elif is_Even(y):
            print("y must be ODD integer!\n")

        else:
            break

    return x, y


x, y = get_Input()

# Calling the functions.
while True:
    choice = menu()  # Print menu and get choice.
    if choice == 0:
        print("\nGoodbye! Have a great day!")
        break
    elif choice == 1:
        sums = summation(x)
        print(f"\nThe sum of the squares of all even integers from 1 to {x} is {sums}")
    elif choice == 2:
        box(y)
    elif choice == 3:
        avg = average(x)
        print(f"\nThe average of odd integers from 1 to {x} is {avg}")
    else:
        print("Invalid Choice")
