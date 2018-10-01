#PF-Assgn-50

def sms_encoding(data):
    #start writing your code here
    vow=['a','e','i','o','u','A','E','I','O','U']
    data=data.split()
    data1=[]
    count1=0
    
    for word in data:
        str1=''
        for chr in word:
            if chr in vow:
                count1+=1
            else:
                str1+=chr
        if(count1==len(word) or len(word)==1):
            data1.append(word)
        else:
            data1.append(str1)         
    data1=' '.join(data1) 
    return data1   
data="I love Python"
print(sms_encoding(data))
