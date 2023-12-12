class Destination():
    '''Initializes the Destination Model Class with 6 instance variables which contain information about a destination flown to.
        Variables:
                        ident:                      Unique id of the destination
                        airport:                    Name of the destination airport
                        flight_time:                The time in hours and minutes it takes to fly to the destination
                        distance_from_iceland:      The distance in kilometers from Iceland to the destination
                        emergency_contact:          Name of the emergency contact
                        emergency_contact_number:   Emergency contact's phone number of the destination
                        
        '''  
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
    def get_distance_from_iceland(self):
        return self.__distance_from_iceland
    def get_emergency_contact(self):
        return self.__emergency_contact
    def get_emergency_contact_number(self):
        return self.__emergency_contact_number

    def change_flight_time(self, flight_time):
        self.__flight_time = flight_time
    def change_emergancy_contact(self, emergancy_contact):
        self.__emergency_contact = emergancy_contact
    def change_emergancy_contact_number(self, emergancy_contact_number):
        self.__emergency_contact_number = emergancy_contact_number
        
    def add_to_file(self):
        '''Prepares the object to be written into a file as csv.
           Returns a string representation of the object with comma seperating values '''
           
        return "{},{},{},{},{},{}\n".format(self.__ident, self.__airport, self.__flight_time, self.__distance_from_iceland, self.__emergency_contact, self.__emergency_contact_number)
    
    def __str__(self):
        return "{}, {}\n\tFlight time: {}\n\tDistance from Iceland: {}\n\tEmergancy contact: {}\n\tEmergancy contact number: {}\n".format(self.__airport, self.__ident, self.__flight_time, self.__distance_from_iceland, self.__emergency_contact, self.__emergency_contact_number)

    def get_ident(self):
        return self.__ident