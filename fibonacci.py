n=int(input("number of fibonacci numbers needed in series"))
a=0
b=1
for i in range(n):
    print(a,end=",")
    a,b=b,b+a
    
    
