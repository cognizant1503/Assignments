#PF-Tryout
def diagonal_stars(number):
    '''for i in range(0,number):
        j=0
        while j<i:
            print('.',end='')
            j+=1
        print('*')'''
    str1='*'
    print(str1)
    for i in range(1,number):
        str1='.'+str1
        print(str1)

number=6    
diagonal_stars(number)