'''
Student Name: Shlok Satish Nagare.
Roll No.: 39
Div: O
Assignment no: 3
Assignment type: claculator
'''

while(1):
    print("1. Addition \n2. Subtraction \n3. Multiplication \n4. Division \n5. power \n6. Factorial \n7. Exit")
    print("\t\tThis program shows the Basic Calculations.\n\n")
    choice = int(input("Enter your choice = \t"))


    if choice==1:
        a=int(input("Enter first number : \n"))
        b=int(input("Enter second number : \n"))
        print("Addition of %d and %d = " %(a,b),a+b)
    if choice==2:
        a=int(input("Enter first number : \n"))
        b=int(input("Enter second number : \n"))
        print("Subtraction of %d and %d = "%(a,b),a-b)
    if choice==3:
        a=int(input("Enter first number : \n"))
        b=int(input("Enter second number : \n"))
        print("Multiplication of %d and %d = " %(a,b),a*b)
    if choice==4:
        a=int(input("Enter first number : \n"))
        b=int(input("Enter second number : \n"))
        print("Division of %d and %d = " %(a,b),a/b)
    if choice==5:
        a=int(input("Enter first number : \n"))
        b=int(input("Enter second number : \n"))
        print("Power of %d and %d = " %a %b,a+b)
    if choice==6:
        pass
    if choice==7:

        exit()