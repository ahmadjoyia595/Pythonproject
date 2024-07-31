print("Wellcome to calculator")
def add(x,y):
   return x + y
def substract(x,y):
   return x - y    
def multiply(x,y):
    return x * y
def divide(x,y):
    return x / y
def power(x,y):
    return x**y
while True:
    print("select operation")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. power")
    choice=(1/2/3/4/5)
    choice= int(input("enter your choice(1/2/3/4/5):"))
    num1 =  float(input("enter your first number:"))
    num2 =  float(input("enter your second number:"))

    if choice == 1:
            print(f"{num1} + {num2} = {add(num1,num2)}")
    elif choice == 2:
            print(f"{num1} + {num2} = {substract(num1,num2)}")
    elif choice == 3:
            print(f"{num1} x {num2} = {multiply(num1,num2)}")
    elif choice == 4:
            print(f"{num1} / {num2} = {divide(num1,num2)}")
    elif choice == 5:
            print(f"{num1} ** {num2} = {power(num1,num2)}")
    else:
            print("invalid choice")