def factorial(number):
    fact=1
    while(number >1):
             fact = number*fact
             number =number-1
    return fact

number=eval(input("Enter a number to know the factorial = "))
fact=factorial(number)
print("factorial of {0} is = {1}".format(number,fact))
            



    
