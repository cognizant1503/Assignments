#PF-Assgn-43
import itertools
def find_smallest_number(num):
    for i in range(1,1000):
        count1=1
        for j in range(1,i):
            if(i%j==0):
                count1+=1    
        if(count1==num):
            return i

num=16
print("The number of divisors :",num)
result=find_smallest_number(num)
print("The smallest number having",num," divisors:",result)

'''import itertools
def find_smallest_number(num):
    for i in itertools.count():
        count1=1
        for j in range(1,i):
            if(i%j==0):
                count1+=1    
        if(count1==num):
            return i

num=16
print("The number of divisors :",num)
result=find_smallest_number(num)
print("The smallest number having",num," divisors:",result)'''
