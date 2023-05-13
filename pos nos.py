n=(input("enter number"))
ch="y"
list=[]
while ch=="y":
    if int(n)>0:
        list.append(n)
        print(list)
    n=(input("enter"))
    ch=input("enter y to continue")