#PF-Assgn-28

def find_max(num1, num2):
    max_num=-1
    # Write your logic here
    list_num=[]
    if(num1>=num2):
        max_num=-1
    else:
        for i in range(num1,num2+1):
            num=i
            sum1,remainder=0,0
            while num>0:
                remainder=num%10
                sum1=sum1+remainder
                num=num//10
            if(sum1%3==0 and len(str(i))==2 and i%5==0):
                list_num.append(i)
    if(len(list_num)>0):
        for i in list_num:
            if i>max_num:
                max_num=i
    else:
        max_num=-1
    return max_num

#Provide different values for num1 and num2 and test your program.
max_num=find_max(10,100)
print(max_num)