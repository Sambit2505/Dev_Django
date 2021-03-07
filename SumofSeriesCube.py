def SumofSeriesCube(n):
                sum=0
                for i in range(1,n+1):
                            sum=sum+(i*i*i)
                return sum

n=eval(input("Enter a number till which you want to get the sum of series: "))
result=SumofSeriesCube(n)
print("Sum of the series {0}".format(result))
