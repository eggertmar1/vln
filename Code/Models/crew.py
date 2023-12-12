class Crew():
    '''Initializes the Crew Model Class with 7 instance variables which contain information about the Crew member:
        Variables:
                        SSN:            Unique id of the Crew member. His social security number is used
                        name:           Name of the crew member
                        role:           The job that the crew member does in NaN air
                        rank:           Crew member status in NaN air in relation to role, (Captain/Copilot, Flight service manager/Cabin crew)
                        licence:        Used to tell what aircrafts the pilots can fly. Only used if the role is pilot, else blank
                        address:        Crew member's address
                        phonenumber:    Crew member's phonenumber
                        
        '''  
    
    def __init__(self, SSN, name, role, rank, licence, address, phonenumber):
        self.__ssn = SSN
        self.__name = name
        self.__role = role
        self.__rank = rank
        self.__licence = licence
        self.__address = address
        self.__phonenumber = phonenumber
    
    def get_ssn(self):
        return self.__ssn
    def get_name(self):
        return self.__name
    def get_role(self):
        return self.__role
    def get_rank(self):
        return self.__rank
    def get_licence(self):
        return self.__licence
    def get_address(self):
        return self.__address
    def get_phonenumber(self):
        return self.__phonenumber
    
    def change_role(self, role):
        self.__role = role
    def change_rank(self, rank):
        self.__rank = rank
    def change_licence(self, licence):
        self.__licence = licence
    def change_address(self, address):
        self.__address = address
    def change_phonenumber(self, phonenumber):
        self.__phonenumber = phonenumber

    def add_to_file(self):
        '''Prepares the object to be written into a file as csv.
           Returns a string representation of the object with comma seperating values '''
           
        return  "{},{},{},{},{},{},{}\n".format(self.__ssn, self.__name, self.__role, self.__rank, self.__licence, self.__address, self.__phonenumber)
    
    def __str__(self):
        return "{}:\n\tssn: {}\n\tRole: {}\n\tRank: {}\n\tLicense: {}\n\tAddress: {}\n\tPhonenumber: {}\n".format(self.__name, self.__ssn, self.__role, self.__rank, self.__licence, self.__address, self.__phonenumber)