#PF-Prac-7
def seed_no(number,ref_no):
    #start writing your code here
    rem=0
    sum1=1
    num=number
    while number>0:
        rem=number%10
        sum1*=rem
        number=number//10
    if(sum1*num==ref_no):
        return True
    else:
        return False
    
    
number=123
ref_no=738
print(seed_no(number,ref_no))