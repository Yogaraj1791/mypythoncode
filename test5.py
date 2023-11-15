b=int(input())
a=[]
print("enter 7 numbers:")
for i in range(b):
    num=int(input("enter number" +str(i+1)))
    a.append(num)
print(a)

sum=0
for i in a:
    sum=sum+i
print(sum)

