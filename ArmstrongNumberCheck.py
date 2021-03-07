def ArmstrongNumberCheck(number):
    o=order(number)
    sum=0
    while(number !=0):
            sum=sum+pow(number%10,o)
            number=number//10
    return sum



def order(a):
    n=0
    while(a!=0):
        a=a//10
        n=n+1
    return n

no=eval(input("Enter a number to check whether i.e Armstrong number or not :"))
IsArmstrong=ArmstrongNumberCheck(no)
if(IsArmstrong==no):
    print("It's a armstrong number")
else :
    print("It's not an armstrong number")


    
    
