str1=input("enter string")
res={}
for keys in str1:
    res[keys]=res.get(keys,0)+1
print("count"+str(res))