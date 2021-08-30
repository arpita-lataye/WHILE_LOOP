i=1
s=0
n=int(input("enter the number:"))
while (i<=n):
    if (i%2==0):
        print(i)
        s+=1
    i+=1
print("sum of even number",s)
