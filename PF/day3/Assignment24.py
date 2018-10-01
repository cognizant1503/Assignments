#PF-Assgn-24
def form_triangle(num1,num2,num3):
    #Do not change the messages provided below
    success="Triangle can be formed"
    failure="Triangle can't be formed"
    
    a=num2+num3
    b=num1+num3
    c=num1+num2
    #Write your logic here
    if(num1>=a or num2>=b or num3>=c):
        return failure
    else:
        return success  

    #Use the following messages to return the result wherever necessary
    
    

#Provide different values for the variables, num1, num2, num3 and test your program
num1=3
num2=3
num3=5
print(form_triangle(num1, num2, num3))