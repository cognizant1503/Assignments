#DSA-Assgn-18

def find_unknown_words(text,vocabulary):
    #Remove pass and write your logic here
    lst=text.split()
    new_list=[]
    for i in lst:
        new_str=i.replace('.','')
        new_str=new_str.lower()
        if(new_str not in vocabulary):
            new_list.append(new_str)
    if(len(new_list)<1):
        return -1
    return set(new_list)

text="The sun rises in the east and sets in the west."
vocabulary = ["sun","in","rises","the","east"]
unknown_words=find_unknown_words(text,vocabulary)
print("The unknown words in the file are:",unknown_words)