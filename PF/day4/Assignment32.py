#PF-Assgn-32
import operator
def max_visited_speciality(patient_medical_speciality_list,medical_speciality):
    # write your logic here
    a=patient_medical_speciality_list.count('P')
    b=patient_medical_speciality_list.count('O')
    c=patient_medical_speciality_list.count('E')
    
    if(a>b and a>c):
        speciality=medical_speciality['P']
    elif(b>a and b>c):
        speciality=medical_speciality['O']
    else:
        speciality=medical_speciality['E']
    
    return speciality

#provide different values in the list and test your program
patient_medical_speciality_list=[301,'P',302, 'P' ,305, 'P' ,401, 'E' ,656, 'E']
medical_speciality={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
speciality=max_visited_speciality(patient_medical_speciality_list,medical_speciality)
print(speciality)

'''#PF-Assgn-32
def max_visited_speciality(patient_medical_speciality_list,medical_speciality):
    # write your logic here
    dict_value={}
    for i in patient_medical_speciality_list:
        if str(i).isalpha():
            count=patient_medical_speciality_list.count(i)
            dict_value.update({(i,count)})
    
    list1=list(dict_value.values())
    maximum=max(list1)     
    for key,value in dict_value.items():
        if value==maximum:
            ped=key
    speciality = medical_speciality[ped] 
    speciality = max(dict_value.items(),key=operator.itemgetter(1))[0]
    speciality = medical_speciality[speciality]
    return speciality

#provide different values in the list and test your program
patient_medical_speciality_list=[301,'P',302, 'P' ,305, 'P' ,401, 'E' ,656, 'E']
medical_speciality={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
speciality=max_visited_speciality(patient_medical_speciality_list,medical_speciality)
print(speciality)
'''