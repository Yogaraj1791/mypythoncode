## How many odd and even numbers between 1 to 10##
e_count=0
o_count=0
for i in range(1,10):
    if(i%2==0):
        e_count=e_count+1
    else:
        o_count=o_count+1
print(e_count)
print(o_count)
