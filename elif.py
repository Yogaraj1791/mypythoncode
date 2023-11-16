##elif example## elif will not allow to run next line once elif condition satisfied##
score=int(input("Enter your score:"))
if(score<35):
    print("Poor student")
elif(score>35 and score<70):
    print("avarage student")
elif(score>70 and score<100):
    print("Good student")
else:
    print("Invalid score")