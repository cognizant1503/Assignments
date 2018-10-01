#PF-Assgn-42
def find_factors(num):
    #Accepts a number and returns the list of all the factors of a given number
    factors = []
    for i in range(2,(num+1)):
        if(num%i==0):
            factors.append(i)
    return factors
    

def is_prime(num, i):
    if(i==1):
        return True
    elif(num%i==0):
        return False;
    else:
        return(is_prime(num,i-1))

def find_largest_prime_factor(list_of_factors):
    #Accepts the list of factors and returns the largest prime factor
    
    prime_list=[]
    for i in list_of_factors:
        if is_prime(i,i//2):
            prime_list.append(i)
        else:
            continue
    max1=max(prime_list)
    return max1
def find_f(num):
    #Accepts the number and returns the largest prime factor of the number 
    factors=find_factors(num)
    max1=find_largest_prime_factor(factors)
    return max1
def find_g(num):
    #Accepts the number and returns the sum of the largest prime factors of the 9 consecutive numbers starting from the given number
#Note: Invoke function(s) from other function(s), wherever applicable.'''
    sum1=0
    for i in range(num,num+9):
        c=find_f(i)
        sum1+=c
    return sum1#
print(find_g(10))

#find_largest_prime_factor([2, 3, 6, 7, 14, 21, 42])
