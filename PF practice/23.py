#PF-Prac-23
def divisible_by_sum(number):
    #start writing your code here
    str1=str(number)
    sum1=0
    for i in str1:
        sum1+=int(i)
    if(number%sum1==0):
        return True
    return False

    
number=42
print(divisible_by_sum(number))