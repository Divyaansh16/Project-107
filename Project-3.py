lower=int(input("Enter the lower range limit: "))
upper=int(input("Enter the upper range limit: "))
n=int(input("Enter te number to be divide by: "))
for i in range(lower,upper+1):
    if(i%n==0):
        print(i)