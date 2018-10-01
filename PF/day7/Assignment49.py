#PF-Tryout
#Start writing your code here
import random
tail,head=0,0
for i in range(0,1000):
    x=random.randrange(1,11)
    if(x<=3):
        tail+=1
    else:
        head+=1
print("Tails = ",tail)
print("Heads = ",head)