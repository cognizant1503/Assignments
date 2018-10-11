#PF-Prac-26
def check_occurence(string):
    #start writing your code here
    string=string.upper()
    c1=string.count('MAT')
    c2=string.count('JET')
    if(c1==c2):
        return True
    return False
        
string="Jet on the Mat but mat is too long"
print(check_occurence(string))