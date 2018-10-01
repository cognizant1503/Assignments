#OOPR-Assgn-10

class CallDetail:
    def __init__(self,phoneno,called_no,duration,call_type):
        self.__phoneno=phoneno
        self.__called_no=called_no
        self.__duration=duration
        self.__call_type=call_type  
        
        
class Util:
    def __init__(self):
        self.list_of_call_objects=None

    def parse_customer(self,list_of_call_string):
        self.list_of_call_objects=[]
        b=[]
        for i in list_of_call_string:
            b.append(i.split(','))
        a=b
        for i in range(0,len(a)):
            self.list_of_call_objects.append(CallDetail(a[i][0],a[i][1],a[i][2],a[i][3]))
        return self.list_of_call_objects
call='9990000001,9330000001,23,STD'
call2='9990000001,9330000002,54,Local'
call3='9990000001,9330000003,6,ISD'

list_of_call_string=[call,call2,call3]
Util().parse_customer(list_of_call_string)

