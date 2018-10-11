#PF-Tryout
def find_five_digit():
    #start writing your code here
    for i in range(2,10):
        n3=i
        n2=i+2
        n1=n2+2
        n4=i-2
        n5=n4+2
        if(n1+n2+n3+n4+n5==19 and n3+n4+n5==n1):
            lst=[n1,n2,n3,n4,n5]
            str1=''
            for i in lst:
                str1+=str(i)
            print(str1)
            break
find_five_digit()