#PF-Prac-24
def find_gcd(num1,num2):
    #start writing your code here
    if(num1>num2):
        if(num2<=0):
            return num1
        else:
            c=num1%num2
            num1=num2
            num2=c
            return find_gcd(num1, num2)
    
    elif(num2>num1):
        if(num1<=0):
            return num2
        else:
            c=num2%num1
            num2=num1
            num1=c
            return find_gcd(num1, num2)

num1=45
num2=1135
print(find_gcd(num1,num2))