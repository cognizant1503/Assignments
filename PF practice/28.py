#PF-Tryout
def sing_99_bottles():
   #start writing your code here
    for i in range(99,0,-1):
        if(i==99):
            print('99 bottles of beer on the wall, 99 bottles of beer.')
        else:
            print('Take one down, pass it around, '+str(i)+' bottles of beer on the wall.')
        
   
sing_99_bottles()