dadd = ['add', 'addition', 'ADD', 'Add', 'Addition', 'ADDITION', '+', '1']
dsub = ['sub', 'subtraction', 'SUB', 'Sub', 'Subtraction', 'SUBTRACTION', '-', '2']
dmply = ['mply', 'multiply', 'Multiply', 'Mply', 'MULTIPLY', '*', 'MPLY', '3']
div = ['Divison', 'division', 'DIVISION', 'Div', 'div', 'DIV', '/', 'Divide', 'DIVIDE', 'divide', '4']
dsqr = ['squared', 'square', 'square of', '^2', 'SQUARE', 'SQUARED', 'Squared', 'sqr', 'SQR', 'Sqr', '5']
dcb = ['cube', 'CUBED', 'Cube', 'Cubed', 'cubed', '^3', '6']
dsqrt = ['square root', 'Square Root', 'SQUARE ROOT', 'SQUAREROOT', 'Squareroot', 'squareroot', 'sqrt', 'SQRT', 'Sqrt',
         '7']
dcbt = ['cube root', 'Cube Root', 'CUBE ROOT', 'CUBEROOT', 'Cuberoot', 'cuberoot', 'cbrt', 'CBRT', 'CBRT', '8']
dpwr = ['pwr', 'PWR', 'Pwr', 'Power', 'power', 'POWER', '^', '9']
dfac = ['factorial', 'Factorial', 'FACTORIAL', '!', '10', 'fac']
dquad = ['Quadratic Equation', 'QUADRATIC EQUATION', 'quadratic equation', 'quadratic', 'Quadratic',
         'QUADRATIC', '11']
print("Welcome in this proram you will be able to make basic calculations on two digits.")
choice = input("Select out of these following operations:\n(1)ADDITION\n(2)SUBTRACTION\n(3)MULTIPLICATION\n(4)DIVISION\n(5)SQUARE\n(6)CUBE\n(7)SQUARE ROOT\n(8)CUBE ROOT\n(9)POWER\n(10)FACTORIAL\n(11)QUADRATIC EQUATION\n\t\t")


def addition():
    print("Enter two values on which you want to perform addition. ")
    x = float(input("Enter first value: "))
    y = float(input("Enter second value: "))
    print("%d + %d = " % (x, y), x + y)


def subtraction():
    print("Enter two values on which you want to perform subtraction. ")
    x = float(input("Enter first value: "))
    y = float(input("Enter second value: "))
    print("%d - %d = " % (x, y), x - y)


def multiplication():
    print("Enter two values on which you want to perform multiplication. ")
    x = float(input("Enter first value: "))
    y = float(input("Enter second value: "))
    print("%d x %d = " % (x, y), x * y)


def division():
    print("Enter two values on which you want to perform divsion. ")
    x = float(input("Enter first value: "))
    y = float(input("Enter second value: "))
    print("%d divided by %d gives: " % (x, y), x / y)


def square():
    x = float(input("Enter a number to know its square: "))
    print("The square of %d is: " % x, x ** 2)


def cube():
    x = float(input("Enter a number to know its cube: "))
    print("The square of %d is: " % x, x ** 3)


def sqrt():
    x = float(input("Enter a number to know its square root: "))
    print("The square root of %d is: " % x, x ** 0.5)


oneby3 = 1 / 3


def cbrt():
    x = float(input("Enter a number to know its cube root: "))
    print("The cube root of %d is: " % x, x ** oneby3)


def power():
    x = float(input("Enter a number: "))
    y = float(input("You want this number raised to the power of no?\n"))
    print("%d^%d =: " % (x, y), x ** y)


def factorial():
    x = int(input("Enter a number to calculate its factorial: "))
    if x == 0:
        print("The factorial of %d is: 1" % x)
    elif x < 0:
        print("Factorial for negative numbers does not exist.")
    else:
        fac = 1
        for i in range(1, x + 1):
            fac = fac * i
        print("%x! = " % x, fac)


def quadratic():
    print("A quadratic equation is in the form of AX^2+BX+C=0")
    a = int(input("Enter the value of A: "))
    b = int(input("Enter the value of B: "))
    c = int(input("Enter the value of C: "))
    if a == 0:
        print("The roots for this equation do not exist.")
    determinant = ((b*b)-(4*a*c))**0.5
    if determinant == 0:
        root1 = (-b / 2 * a)
        print("This equation have only one root which is: ", root1)
    elif determinant > 0:
        print("This roots of this equation are imaginary.")
    else:
        root1 = ((-b + determinant) / 2 * a)
        root2 = ((-b - determinant) / 2 * a)
        print("The two roots of this equation are: \nx1=%d , x2=%d" % (root1, root2))


if choice in dadd or choice == 1:
    addition()
elif choice in dsub or choice == 2:
    subtraction()
elif choice in dmply or choice == 3:
    multiplication()
elif choice in div or choice == 4:
    division()
elif choice in dsqr or choice == 5:
    square()
elif choice in dcb or choice == 6:
    cube()
elif choice in dsqrt or choice == 7:
    sqrt()
elif choice in dcbt or choice == 8:
    cbrt()
elif choice in dpwr or choice == 9:
    power()
elif choice in dfac or choice == 10:
    factorial()
elif choice in dquad or choice == 11:
    quadratic()