#PF-Assgn-30

def encode(message):
    count=1
    
    element=''
    for i in range(1,len(message)):
        if(message[i-1]==message[i]):
            count=count+1
        else:
            element+=str(count)+message[i-1]
            count=1
    element+=str(count)+message[len(message)-1]
    return element
#Provide different values for message and test your program
encoded_message=encode("ABBBBCCCCCCCCAA")
print(encoded_message)
