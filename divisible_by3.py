# here starting point is 891 we get 1to 30 numbers which is divisible by 3

i=891
while i<931:
    i=i+1
    z=i-890
    if z%3==0:
        print(z)
        