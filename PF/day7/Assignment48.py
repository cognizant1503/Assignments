#PF-Assgn-48

def find_correct(word_dict):
    #start writing your code here
    count1,count2,count3=0,0,0
    
    for x,y in word_dict.items():
        if(len(x)!=len(y)):
            count3+=1
        elif(x==y):
            count1+=1
        elif(len(x)==len(y)):
            cun=0
            for i in range(0,len(x)):
                if(x[i]!=y[i]):
                    cun+=1
            if(cun<=2):
                count2+=1
            else:
                count3+=1                    
    lst=[count1,count2,count3]    
        
    return lst
word_dict={"THEIR": "THEIR","BUSINESS":"BISINESS","WINDOWS":"WINDMILL","WERE":"WEAR","SAMPLE":"SAMPLE"}
print(find_correct(word_dict))
