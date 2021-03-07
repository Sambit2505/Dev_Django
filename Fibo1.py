def fiboNacci (n):
        a=0
        b=1
        if (n==0):
            return 0
        elif (n==1):
            return 1
        else:
            for i in range(2,n):
                    c=a+b
                    a=b
                    b=c
            return c

result=fiboNacci(5)
print("result= ",result)
