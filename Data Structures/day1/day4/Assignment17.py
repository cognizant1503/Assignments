#DSA-Assgn-17

def find_matches(country_name):
    #Remove pass and write your logic here
    new_list=[]
    for i in match_list:
        lst=i.split(':')
        if(lst[0]==country_name):
            new_list.append(i)
    return new_list

def max_wins():
    #Remove pass and write your logic here
    mat_list=[]
    for i in match_list:
        lst=i.split(":")
        mat_list.append(lst[1])
    wor,cham,t20=[],[],[]
    for i in match_list:
        lst=i.split(":")
        if(lst[1] in mat_list):
            if(lst[1]=='WOR'):
                wor.append(int(lst[-1]))
            elif(lst[1]=='CHAM'):
                cham.append(int(lst[-1]))
            elif(lst[1]=='T20'):
                t20.append(int(lst[-1]))
   
    wor_list,cham_list,t20_list=[],[],[]
    for i in match_list:
        lst=i.split(":")
        if(lst[1] in mat_list):
            if(lst[1]=='WOR'):
                if(int(lst[-1])>=max(wor)):
                    wor_list.append(lst[0])
            elif(lst[1]=='CHAM'):
                if(int(lst[-1])>=max(cham)):
                    cham_list.append(lst[0])
            elif(lst[1]=='T20'):
                if(int(lst[-1])>=max(t20)):
                    t20_list.append(lst[0])
    new_dict={}
    for i in mat_list:
        if(i=="WOR"):
            new_dict.update({i:wor_list})
        elif(i=="CHAM"):
            new_dict.update({i:cham_list})
        elif(i=="T20"):
            new_dict.update({i:t20_list})
    return new_dict
def find_winner(country1,country2):
    #Remove pass and write your logic here
    count1,count2=0,0
    for i in match_list:
        lst=i.split(':')
        if(lst[0]==country1):
            count1+=int(lst[3])
        elif(lst[0]==country2):
            count2+=int(lst[3])
    if(count1>count2):
        return country1
    elif(count1<count2):
        return country2
    else:
        return "Tie" 

#Consider match_list to be a global variable
match_list=["AUS:CHAM:5:2","AUS:WOR:2:1","ENG:WOR:2:0","IND:T20:5:3",
            "IND:WOR:2:1","PAK:WOR:2:0","PAK:T20:5:1","SA:WOR:2:0",
            "SA:CHAM:5:1","SA:T20:5:0"]

#Pass different values to each function and test your program
print("The match status list details are:")
print(match_list)
print()