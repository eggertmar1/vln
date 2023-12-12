class AircraftType():
    '''Initializes the AircraftType Model Class with 11 instance variables which define the characteristics of an Aircraft:
        Variables:
                        plane_type_id:          Id of the plane type. Used as a foreign key to find the aircraft with this type.
                        manufacturer:           Name of the aircraft manufacturer.
                        model:                  Name of the aircraft model.
                        capacity:               Number of seats available.
                        empty_weight:           Weight of the aircraft in kilograms.
                        max_take_off_weight:    Maximum take off weight of the aircraft.
                        unit_thrust:            Thrust is the force which moves the aircraft through the air.
                        service_ceiling:        Service ceiling is the altitude at which the aircraft is unable to climb at a rate greater than 100 feet per minute.
                        length:                 Length of the aircraft
                        height:                 Height of the aircraft
                        wingspan:               The distance from one wingtip to another wingtip.
        '''             
    def __init__(self, plane_type_id, manufacturer, model, capacity,
                 empty_weight, max_take_off_weight, unit_thrust, service_ceiling, 
                 length, height, wingspan):
        self.__plane_type_id = plane_type_id
        self.__manufacturer = manufacturer
        self.__model = model
        self.__capacity = capacity
        self.__empty_weight = empty_weight
        self.__max_take_off_weight = max_take_off_weight
        self.__unit_thrust = unit_thrust
        self.__service_ceiling = service_ceiling
        self.__length = length
        self.__height = height
        self.__wingspan = wingspan
    
    def get_plane_type_id(self):
        return self.__plane_type_id
    
    def get_plane_manufacturer(self):
        return self.__manufacturer

    def get_plane_model(self):
        return self.__model

    def get_plane_capacity(self):
        return self.__capacity

    def get_plane_empty_weight(self):
        return self.__empty_weight

    def get_plane_max_take_off_weight(self):
        return self.__max_take_off_weight

    def get_plane_unit_thrust(self):
        return self.__unit_thrust

    def get_plane_service_ceiling(self):
        return self.__service_ceiling

    def get_plane_length(self):
        return self.__length

    def get_plane_height(self):
        return self.__height
    
    def get_plane_wingspan(self):
        return self.__wingspan

    def add_to_file(self):
        '''Prepares the object to be written into a file as csv.
           Returns a string representation of the object with comma seperating values '''
           
        return "{},{},{},{},{},{},{},{},{},{},{}\n".format(self.__plane_type_id,self.__manufacturer,self.__model,self.__capacity
                            ,self.__empty_weight,self.__empty_weight,self.__max_take_off_weight,self.__unit_thrust,self.__service_ceiling,
                            self.__length,self.__height,self.__wingspan)