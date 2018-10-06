#DSA-Assgn-10

#This assignment needs DataStructures.py file in your package, you can get it from resources page

from day2.DataStructures import LinkedList

class Compartment:
    def __init__(self,compartment_name,no_of_passengers,total_seats):
        self.__compartment_name=compartment_name
        self.__no_of_passengers=no_of_passengers
        self.__total_seats=total_seats

    def get_compartment_name(self):
        return self.__compartment_name

    def get_no_of_passengers(self):
        return self.__no_of_passengers

    def get_total_seats(self):
        return self.__total_seats

class Train:
    def __init__(self,train_name,compartment_list):
        self.__train_name=train_name
        self.__compartment_list=compartment_list
    
    def get_train_name(self):
        return self.__train_name
    
    def get_compartment_list(self):
        return self.__compartment_list
    
    def count_compartments(self):
        temp=self.__compartment_list.get_head()
        length=0
        while(temp!=None):
            length+=1
            temp=temp.get_next()
        return length
    
    def check_vacancy(self):
        count=0
        temp=self.__compartment_list.get_head()
        while(temp!=None):
            total=temp.get_data().get_total_seats()
            booked=temp.get_data().get_no_of_passengers()
            
            percent=(total-booked)/total*100
            if(percent>50):
                count+=1
            temp=temp.get_next()
        return count
    #Implement the remaining methods of Train class here

#Use different values for compartment and test your program
compartment1=Compartment("SL",250,400)
compartment2=Compartment("2AC",125,280)
compartment3=Compartment("3AC",120,300)
compartment4=Compartment("FC",160,300)
compartment5=Compartment("1AC",100,210)
compartment_list=LinkedList()
compartment_list.add(compartment1)
compartment_list.add(compartment2)
compartment_list.add(compartment3)
compartment_list.add(compartment4)
compartment_list.add(compartment5)
train1=Train("Shatabdi",compartment_list)
count=train1.count_compartments()
print("The number of compartments in the train:",count)
vacancy_count=train1.check_vacancy()
print("The number of compartments which have more than 50% vacancy:",vacancy_count)