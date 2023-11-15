salary=int(input("Salary:"))
age=int(input("What is your age:"))
if(salary>=25000 or age<=25):
    loan=int(input("How much you required loan:"))
    if(loan>50000):
        print("Maximum Loan amount is 50000")
    else:
        print("You are eligible for ",loan, "loan amount")
else:
    print("You are not eligible for loan")