def fibonacci(n):
    if n<0:
        print("wrong input")
    elif n==0:
        return 0
    elif n==1 or n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
n=int(input("enter"))
print(fibonacci(n))