#PF-Assgn-22
import calendar
def find_leap_years(given_year):

    # Write your logic here
    i=0
    list_of_leap_years=[]
    while i<15:
        if(calendar.isleap(given_year)):
            list_of_leap_years.append(given_year)
            given_year=given_year+1
            i=i+1
        else:
            given_year=given_year+1
    
    return list_of_leap_years

list_of_leap_years=find_leap_years(1000)
print(list_of_leap_years)