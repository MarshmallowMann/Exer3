def summation(x):
    sum = 0
    for i in range(1, x + 1):
        if is_Even(i):
            sum += (i * i)
    return sum


def box(N):
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


def menu(x, y, choice):
    while True:
        print("\nPlease Choose from the following:\n"
              "1. Summation\n"
              "2. Box\n"
              "3. Average\n"
              "0. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 0:
            print("Goodbye! Have a great day!")
            break
        elif choice == 1:
            sum = summation(x)
            print(f"\nThe sum of the squares of all even integers from 1 to {x} is {sum}")
        elif choice == 2:
            box(y)
        elif choice == 3:
            avg = average(x)
            print(f"\nThe average of odd integers from 1 to {x} is {avg}")
        else:
            print("Invalid Choice")


def is_Even(x):
    if x % 2 == 0:
        even = True
    else:
        even = False
    return even


def is_Odd(y):
    if is_Even(y):
        odd = False
    else:
        odd = True
    return odd


def is_Negative(x):
    if x < 0:
        return True
    return False


def get_Input(x, y):
    while True:
        x = int(input("Enter value for x: "))
        y = int(input("Enter value for y: "))

        if is_Negative(x) or is_Negative(y):
            print("x and y must be both POSITIVE integers!\n")

        elif is_Odd(x):
            print("x must be EVEN integer!\n")

        elif is_Even(y):
            print("y must be ODD integer!\n")
        else:
            break

    return x, y


x, y, choice = 0, 0, 0
x, y = get_Input(x, y)
menu(x, y, choice)
