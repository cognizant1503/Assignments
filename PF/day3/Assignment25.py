#PF-Tryout

#debug the below code
counter1=0
counter2=5
while(counter1 < 5):
  
  while(counter2>counter1):
     star=""
     for i in range(0,counter2):
        star=star+ "*"
     counter2-=1
     print(star)
  counter1+=1
