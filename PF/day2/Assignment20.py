#PF-Assgn-20

def calculate_loan(account_number,salary,account_balance,loan_type,loan_amount_expected,customer_emi_expected):
    bank_emi_expected=0
    eligible_loan_amount=0
    account = str(account_number)
    flag=0
    
    if(len(account)==4 and account[0]=='1'):
        if(account_balance>=100000):
            if(salary>25000 and salary<=50000 and loan_type=="Car"):
                eligible_loan_amount = 500000
                bank_emi_expected=36
                if(loan_amount_expected<=eligible_loan_amount and customer_emi_expected<=bank_emi_expected):
                    
                    flag=1
                else:
                    flag=-1
            elif(salary>50000 and salary<=75000 and loan_type=="House"):
                eligible_loan_amount = 6000000
                bank_emi_expected=60
                if(loan_amount_expected<=eligible_loan_amount and customer_emi_expected<=bank_emi_expected):
                    
                    flag=1
                else:
                    flag=-1
            elif(salary>75000 and loan_type=="Business"):
                eligible_loan_amount = 7500000
                bank_emi_expected=84
                if(loan_amount_expected<=eligible_loan_amount and customer_emi_expected<=bank_emi_expected):
                    
                    flag=1
                else:
                    flag=-1
            else:
                print("Invalid loan type or salary")         
                
        else:
            print("Insufficient account balance")       
    else:
        print("Invalid account number")
    if(flag==1):
        print("Account number:", account_number)
        print("The customer can avail the amount of Rs.", eligible_loan_amount)
        print("Eligible EMIs :", bank_emi_expected)
        print("Requested loan amount:", loan_amount_expected)
        print("Requested EMI's:",customer_emi_expected)
    elif(flag==-1):
        print("The customer is not eligible for the loan")
                
calculate_loan(1001,40000,250000,"Car",300000,30)
