#DSA-Assgn-21

#This assignment needs DataStructures.py file in your package, you can get it    from resources page

from res.DataStructures import Stack, Queue

#Global variables
flight_details=["AI890:BAN:MUM:1400","AI678:BAN:LON:1200","AI345:BAN:CAN:1410","AF780:BAN:AGF:1340","AI001:BAN:AUS:1500","AI404:BAN:NY:1220"]

passenger_details_dict=\
{"LW101":["Amanda","AI678","C7",25],"LW103":["John","AI345","A2",10],"LW107":["Alex","AI678","G5",12],\
"TW700":["Hary","AF780","D2",26],"LW167":["Kate","AI001","G3",25],"LT890":["Wade","AI404","G3",25],\
"TW677":["Preet","AF780","D3",25],"LA106":["Henry","AI001","B5",25.5],"LA104":["Ajay","AI001","A7",23],\
"LW202":["Amy","AI345","C3",24.5],"LT673":["Susan","AI404","J8",5],"TW709":["Tris","AF780","H5",22.5],\
"LA188":["Cameron","AI890","H4",22],"LA902":["Scofield","AI678","G4",23],"TW767":["Pom","AF780","H4",2],\
"LW787":["Burrows","JA678","B4",15],"LW898":["Sara","AI678","E4",14],"LW104":["Williams","AI890","C4",10] }

def find_flights(flight_time):
    flight=[]
    for i in flight_details:
        lst=i.split(':')
        if(int(lst[-1])>=int(flight_time) and int(lst[-1])<=int(flight_time)+200):
            flight.append(i)
    return flight
        

def sort_flight_list(flight_list):
    flight_list.sort(key=lambda time:time.split(':')[-1]) 
    return flight_list

def get_passenger_details(flight_detail):
    pnr_list=[]
    lst=flight_detail.split(':')
    for x,y in passenger_details_dict.items():
        if(lst[0]==y[1]):
            pnr_list.append(x)
    return pnr_list
def security_check(passenger_pnr_list):
    lst=[]
    for i in passenger_pnr_list:
        for x,y in passenger_details_dict.items():
            if(i==x and y[-1]>=0 and y[-1]<=25):
                lst.append(i)
    return lst
def sort_passengers(passenger_pnr_list):
    pass_dict={}
    for i in passenger_pnr_list:
        a=passenger_details_dict[i]
        pass_dict.update({i:a})
        
    lst=[]
    for x,y in pass_dict.items():
        lst.append(y)
    lst.sort(key=lambda seat:seat[-2])
    
    pnr_list=[]
    for i in lst:
        for x,y in pass_dict.items():
            if(i==y):
                pnr_list.append(x)
    return pnr_list

def boarding(passenger_pnr_list):
    pass_queue=Queue(len(passenger_pnr_list))
    for i in passenger_pnr_list:
        pass_queue.enqueue(i)
    return pass_queue

def seating(passenger_queue):
    pass_stack=Stack(passenger_queue.get_max_size())
    
    while not passenger_queue.is_empty():
        val=passenger_queue.dequeue()
        pass_stack.push(val)
    return pass_stack

print("The flight details :")
print(flight_details)
print()
print("The passenger details at the airport:")
print(passenger_details_dict)
print()
time=1130
print("Details of the flight between the timings",time,"and",time+200,"are:")
flight_list=['AI404:BLR:NY:1220', 'JA678:BLR:SYD:1200']
flight_list=sort_flight_list(flight_list)
print(flight_list)
print()
print("Details of the passengers boarding the flights between the timings ",time,"and",(time+200),"are:")
print()
for i in range(0,len(flight_list)):
    flight_data=flight_list[i].split(':')
    flight_name=flight_data[0]

    passenger_pnr_list=get_passenger_details(flight_list[i])
    print("PNR details of the passengers boarding the flight",flight_name,":")
    print(passenger_pnr_list)

    print()
    updated_passenger_pnr_list=security_check(passenger_pnr_list)
    print("PNR details of the passengers of flight",flight_name," whose baggage has been cleared:")
    print(updated_passenger_pnr_list)

    sorted_passenger_pnr_list=sort_passengers(updated_passenger_pnr_list)
    print("PNR details of the passengers of flight",flight_name," sorted based on seating number:")
    print(sorted_passenger_pnr_list)

    print()
    print("The PNR details of the passengers at the queue",flight_name,":")
    passenger_queue=boarding(updated_passenger_pnr_list)
    passenger_queue.display()

    print()
    seating_stack=seating(passenger_queue)
    print("The PNR details of the passengers in the flight",flight_name,":")
    seating_stack.display()