## Avarage mark##
Tamil=int(input("Tamil Mark?"))
English=int(input("English mark?"))
Maths=int(input("Maths Mark?"))
Science=int(input("Scince Marks?"))
Social=int(input("Social marks?"))
operation=Tamil+English+Maths+Science+Social
avarage=operation/5
if(Tamil<35 or English<35 or Maths<35 or Science<35 or Social<35):
    print("Additional class is required for below 35 mark subject","and your percentage", avarage, "%")

else:
    print("You are Good to go",avarage)
                
                