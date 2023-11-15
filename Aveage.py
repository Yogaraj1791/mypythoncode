Tamil=int(input("Tamil Mark?"))
English=int(input("English mark?"))
Maths=int(input("Maths Mark?"))
Science=int(input("Scince Marks?"))
Social=int(input("Social marks?"))
operation=Tamil+English+Maths+Science+Social
avarage=operation/5
if(avarage<35):
    print("Additional class is required since your avarage mark is",avarage)
else:
    print("You are good to go since your avarage mark is",avarage)
                
                