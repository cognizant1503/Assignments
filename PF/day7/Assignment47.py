#PF-Assgn-47
def encrypt_sentence(sentence):
    #start writing your code here
    data=sentence.split()
    str1=''
    vow1=['a','e','i','o','u','A','E','I','O','U']
    for i in range(0,len(data)):
        if(i%2==0):
            
            a=data[i][::-1]
            str1+=a
        else:
            vow=''
            con=''
            for x in data[i]:
                if x not in vow1:
                    con+=x
                else:
                    vow+=x
            str1+=con+vow    
        str1+=' '
    str1=str1.strip()
    return str1
sentence="The sun rises in the east"
encrypted_sentence=encrypt_sentence(sentence)
print(encrypted_sentence)
