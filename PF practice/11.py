#PF-Prac-11
def find_upper_and_lower(sentence):
    #start writing your code here
    up,low=0,0
    for i in sentence:
        if i.isupper():
            up+=1
        elif(i.islower()):
            low+=1
    result_list=[up,low]
    return result_list

sentence="Come Here"
print(find_upper_and_lower(sentence))