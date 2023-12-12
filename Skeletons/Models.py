class Crew():

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
    def get_licence(self):
        return self.__licence

    def __str__(self):
        return  "{},{},{},{},{},{},{}".format(self.__ssn, self.__name, self.__role, self.__rank, self.__licence, self.__address, self.__phonenumber)
        
class Aircraft():
    def __init__(self, plane_insignia, plane_type_id):
        self.__plane_insignia = plane_insignia
        self.__plane_type_id = plane_type_id
    
    def get_plane_type_id(self):
        return self.__plane_type_id

class AircraftType():
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

class Destination():
    def __init__(self, ident, airport, flight_time, distance_from_iceland,
                emergency_contact, emergency_contact_number):
        self.__ident = ident
        self.__airport = airport
        self.__flight_time = flight_time
        self.__distance_from_iceland = distance_from_iceland
        self.__emergency_contact = emergency_contact
        self.__emergency_contact_number = emergency_contact_number
    
    def get_ident(self):
        return self.__ident
    def get_airport(self):
        return self.__airport
    def get_flight_time(self):
        return self.__flight_time
    def change_flight_time(self, flight_time):
        self.__flight_time = flight_time
    def get_distance_from_iceland(self):
        return self.__distance_from_iceland
    def get_emergency_contact(self):
        return self.__emergency_contact
    def get_emergency_contact_number(self):
        return self.__emergency_contact_number
    
    def add_to_file(self):
        return "{},{},{},{},{},{}\n".format(self.__ident, self.__airport, self.__flight_time, self.__distance_from_iceland, self.__emergency_contact, self.__emergency_contact_number)
    
    def __str__(self):
        return "{}, {} | {} | {} | {}: {}".format(self.__airport, self.__ident, self.__flight_time, self.__distance_from_iceland, self.__emergency_contact, self.__emergency_contact_number)

    def get_ident(self):
        return self.__ident




class Voyage():
    def __init__(self, flight_out, flight_in):
        self.__flight_out = flight_out
        self.__flight_in = flight_in
    
    def show(self):
        return self.__flight_out.show()
        

class Flight():
    def __init__(self, flight_number  , start_location , destination, start_time, arrival_time, aircraft_id, captain ,
                copilot, flight_service_manager, flight_attendant_1, flight_attendant_2  ):
        self.__flight_number = flight_number
        self.__start_location = start_location
        self.__destination = destination
        self.__start_time = start_time
        self.__arrival_time = arrival_time
        self.__aircraft_id = aircraft_id
        self.__captain = captain
        self.__copilot = copilot
        self.__flight_service_manager = flight_service_manager
        self.__flight_attendant_1 = flight_attendant_1
        self.__flight_attendant_2 = flight_attendant_2

    def show(self):
        return self.__flight_number

    def add_to_file(self):
        return "{},{},{},{},{},{},{},{},{},{},{}\n".format(self.__flight_number,self.__start_location,self.__destination,self.__start_time,self.__arrival_time,
                                                        self.__aircraft_id,self.__captain,self.__copilot,self.__flight_service_manager,
                                                        self.__flight_attendant_1,self.__flight_attendant_2)

