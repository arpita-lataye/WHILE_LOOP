# here we use continue statement means skip the if condition of continue 
# in bellow que 5 is skip 

i=1
while i<=10:
    i=i+1
    if (i==5):
        continue
    print(i)
else:
    print("rest of the code")