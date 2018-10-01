#OOPR-Assgn-20
#Start writing your code here

class Applicant:
    __application_dict=None
    __applicant_id_count=1000
    def __init__(self,applicant_name):
        self.__applicant_id=None
        self.__applicant_name=applicant_name
        self.__job_band=None

    def get_applicant_id(self):
        return self.__applicant_id
    def get_applicant_name(self):
        return self.__applicant_name
    def get_job_band(self):
        return self.__job_band

    def generate_applicant_id(self):
        Applicant.__applicant_id_count+=1
        self.__applicant_id=Applicant.__applicant_id_count
        
    
    def apply_for_job(self,job_band):
        for x,y in Applicant.__application_dict.items():
            if(job_band==x):
                if(y<5):
                    y=y+1
                    Applicant.__application_dict.update({x:y})
                else:
                    return -1
        Applicant.__applicant_id_count+=1
        self.__applicant_id=Applicant.__applicant_id_count
        self.__job_band=job_band
    
    @staticmethod
    def get_application_dict():
        return Applicant.__application_dict