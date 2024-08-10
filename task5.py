#check the number is even or odd?
print('check the number is(even or odd):')
num1 = int(input("enter your number:"))
def even_odd_check():
    if (num1 % 2) == 0:
        print(f'{num1} is even.')
    else:
        print(f'{num1} is odd.')
even_odd_check()

#check the prime number?
print('check the number is prime or not?')
num2 = int(input('enter your number:'))
def check_prime_number():
 if num2 > 1:
    for i in range(2,num2):
        if (num2 % i) == 0:
            print(f'{num2} is not a prime number.')
            break
        else:
            print(f'{num2} is a prime number.')
            break
 else:
    print(f'{num2} is not a prime number.')
check_prime_number()

#check factorial?
print('check factorial!')
num3 = int(input('enter your number:'))
fact = 1
if num3 >= 1:
    for i in range(1,num3+1):
        fact = fact*i
print(f'{num3} is the factorial {fact}')