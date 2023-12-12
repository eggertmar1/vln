class Aircraft():
    '''Initializes the Aircraft Model Class with 2 instance variables an Air:
        Variables:
                        plane_insignia:          Unique id of the aircraft.
                        plane_type_id:           Id of the plane type. Used as a foreign key to match the correct aircraft type from another class.
                        
        '''  
    def __init__(self, plane_insignia, plane_type_id):
        self.__plane_insignia = plane_insignia
        self.__plane_type_id = plane_type_id
    
    def get_plane_type_id(self):
        return self.__plane_type_id

    def get_plane_insignia(self):
        return self.__plane_insignia
    
    def add_to_file(self):
        '''Prepares the object to be written into a file as csv.
           Returns a string representation of the object with comma seperating values '''

        return "{},{}\n".format(self.__plane_insignia, self.__plane_type_id)
    
    def __str__(self):
        return "{} | {}".format(self.__plane_insignia, self.__plane_type_id)