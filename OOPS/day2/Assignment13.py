#OOPR-Assgn-13
#Start writing your code here
class Classroom:
    classroom_list=None    
    @staticmethod
    def search_classroom(class_room):
        if(class_room.upper() in Classroom.classroom_list):
                return "Found"
        else:
            return -1
    
    