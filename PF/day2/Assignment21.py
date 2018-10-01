import calendar
def generate_next_date(day,month,year):
    #Start writing your code here
    month1=[1,3,5,7,8,10]
    month2=[4,6,9,11]
    if(month==2):
        if(calendar.isleap(year)):
            if(month==2 and day==29):
                day,month=1,3
        else:
            if(month==2 and day==28):
                day=day+1
            
    elif((day==31) and (month in month1)):
        day,month=1,month+1
    elif(day==31 and month==12):
        day,month,year=1,1,year+1
    elif((day==30) and (month in month2)):
        day,month=1,month+1
    else:
        day=day+1         
    print(day,'-',month,'-',year)

generate_next_date(31,12,2015)