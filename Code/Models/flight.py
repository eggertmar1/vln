import datetime

class Flight():
    '''Initializes the Flight Model Class with 11 instance variables which contain information about a single flight.
        Variables:
                        flight_number:              Unique id of the flight
                        start_location:             The location where the flight departs from
                        destination:                The destination of the flight. The id of the destination is used
                        start_time:                 Flight's departure time in datetime
                        arrival_time:               Flight's arrival time in datetime
                        aircraft_id:                The aircraft used in in a flight. plane_insignia is used.
                        captain:                    Flight Captain's SSN
                        copilot:                    Flight Copilot's SSN
                        flight_service_manager:     Flight Flight Service Manager's SSN
                        flight_attendant_1:         Flight Attendant 1's SSN. Can be blank
                        flight_attendant_2:         Flight Attendant 2's SSN. Can be blank
        '''  

    def __init__(self, flight_number, start_location , destination, start_time, arrival_time, aircraft_id, captain ,
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

    def set_flight_number(self, number):
        self.__flight_number = number
    
    def set_start_time(self, date_time):
        self.__start_time = date_time
    
    def set_arrival_time(self, date_time):
        self.__arrival_time = date_time

    def set_start_location(self, location):
        self.__start_location = location

    def set_destination(self, destination):
        self.__destination = destination
    
    def set_arrival_time(self, arrival_time):
        self.__arrival_time = arrival_time

    def set_aircraft_id(self, aircraft_id):
        self.__aircraft_id = aircraft_id

    def set_captain(self, captain):
        self.__captain = captain

    def set_copilot(self, copilot):
        self.__copilot = copilot
    
    def set_flight_service_manager(self, flight_service_manager):
        self.__flight_service_manager = flight_service_manager
    
    def set_flight_attendant_1(self, flight_attendant_1):
        self.__flight_attendant_1 = flight_attendant_1
    
    def set_flight_attendant_2(self, flight_attendant_2):
        self.__flight_attendant_2 = flight_attendant_2

    def show(self):
        return self.__flight_number

    def get_flight_number(self):
        return self.__flight_number
    
    def get_start_location(self):
        return self.__start_location
    
    def get_destination(self):
        return self.__destination

    def get_start_time(self):
        return self.__start_time

    def get_arrival_time(self):
        return self.__arrival_time

    def get_aircraft_id(self):
        return self.__aircraft_id

    def get_captain(self):
        return self.__captain

    def get_copilot(self):
        return self.__copilot
    
    def get_flight_service_manager(self):
        return self.__flight_service_manager

    def get_flight_attendant_1(self):
        return self.__flight_attendant_1

    def get_flight_attendant_2(self):
        return self.__flight_attendant_2
    
    def get_arranged_crew(self):
        '''Returns a list of all of the crew member's on a flight'''
        
        return [self.__captain, self.__copilot, self.__flight_service_manager, self.__flight_attendant_1, self.__flight_attendant_2]


    def add_to_file(self):
        '''Prepares the object to be written into a file as csv.
           Returns a string representation of the object with comma seperating values '''

        return "{},{},{},{},{},{},{},{},{},{},{}\n".format(self.__flight_number,self.__start_location,self.__destination,self.__start_time.isoformat(),self.__arrival_time.isoformat(),
                                                        self.__aircraft_id,self.__captain,self.__copilot,self.__flight_service_manager,
                                                        self.__flight_attendant_1,self.__flight_attendant_2)
    
    def __str__(self):
        return "{} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {}".format(self.__flight_number,self.__start_location,self.__destination,self.__start_time,self.__arrival_time,
                                                        self.__aircraft_id,self.__captain,self.__copilot,self.__flight_service_manager,
                                                        self.__flight_attendant_1,self.__flight_attendant_2)

