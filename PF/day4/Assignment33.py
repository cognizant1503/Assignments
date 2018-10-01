#PF-Assgn-33

def find_common_characters(msg1,msg2):
    common_characters=''
    for i in msg1:
        if i in msg2 and i!=" " and (i not in common_characters):
            common_characters+=i
        
    if(len(common_characters)>0):
        return common_characters
    else:
        return -1
#Provide different values for msg1,msg2 and test your program
msg1="moto"
msg2="moto"
common_characters=find_common_characters(msg1,msg2)
print(common_characters)