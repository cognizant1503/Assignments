#PF-Assgn-46

def nearest_palindrome(number):
    i=number+1
    count1,b=0,0
    while count1<1:
        c=str(i)
        a=c[::-1]
        if(c==a):
            b=int(i)
            count1+=1
        else:
            i=i+1
                
    return b
number=12300
print(nearest_palindrome(number))
