#DSA-Assgn-5

#This assignment needs DataStructures.py file in your package, you can get it from resources page

from day2.DataStructures import LinkedList

def create_new_sentence(word_list):
    new_sentence=""
    
    temp=word_list.get_head()
    while temp!=None:
        count=0
        while temp.get_data()=='*'or temp.get_data()=='/':
            count+=1
            temp=temp.get_next()
        if(count==1):
            a=temp.get_data()
            a=" "+a
        elif(count==2):
            a=temp.get_data()
            a=' '+a.upper()
        else:
            a=temp.get_data()
        new_sentence+=a
        temp=temp.get_next()
        
    return new_sentence

word_list=LinkedList()
word_list.add("T")
word_list.add("h")
word_list.add("e")
word_list.add("/")
word_list.add("*")
word_list.add("s")
word_list.add("k")
word_list.add("y")
word_list.add("*")
word_list.add("i")
word_list.add("s")
word_list.add("/")
word_list.add("/")
word_list.add("b")
word_list.add("l")
word_list.add("u")
word_list.add("e")
result=create_new_sentence(word_list)
print(result)