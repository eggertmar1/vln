from DataLayer.io_api import IoAPI
import datetime
from Models.flight import Flight

class validChecker:
    def __init__(self):
        self.__IoAPI = IoAPI()

    def is_valid_aircraft_type(self, aircraft_type, aircraft_list):
        """Checks if the aircraft type exists in the aircraft.csv file (Upper case)"""
        valid_aircraft_type_set = set()
        for aircraft in aircraft_list[1:]:
            valid_aircraft_type_set.add(aircraft.get_plane_type_id().upper())
        return aircraft_type in valid_aircraft_type_set

    def is_valid_aircraft_insignia(self, aircraft):
        """Checks if the input aircraft insignia ir valid by checking if its empty"""
        if self.is_empty_string(aircraft.get_plane_insignia()):
            return False 
        return True

    def is_valid_new_aircraft(self, aircraft):
        '''checks to see if all input matches it's units'''
        if self.is_empty_string(aircraft.get_plane_type_id()):
            return False
        if self.is_empty_string(aircraft.get_plane_manufacturer()):
            return False
        if self.is_empty_string(aircraft.get_plane_model()):
            return False
        if self.is_empty_string(aircraft.get_plane_capacity()):
            return False
        if self.is_empty_string(aircraft.get_plane_empty_weight()):
            return False
        if self.is_empty_string(aircraft.get_plane_max_take_off_weight()):
            return False
        if self.is_empty_string(aircraft.get_plane_unit_thrust()):
            return False
        if self.is_empty_string(aircraft.get_plane_service_ceiling()):
            return False
        if self.is_empty_string(aircraft.get_plane_length()):
            return False
        if self.is_empty_string(aircraft.get_plane_height()):
            return False
        if self.is_empty_string(aircraft.get_plane_wingspan()):
            return False
        if not self.is_only_numbers(aircraft.get_plane_capacity()):
            return False
        if not self.is_only_numbers(aircraft.get_plane_empty_weight()):
            return False
        if not self.is_only_numbers(aircraft.get_plane_max_take_off_weight()):
            return False
        if not self.is_only_numbers(aircraft.get_plane_unit_thrust()):
            return False
        if not self.is_only_numbers(aircraft.get_plane_service_ceiling()):
            return False
        if not self.is_only_numbers(aircraft.get_plane_length()):
            return False
        if not self.is_only_numbers(aircraft.get_plane_height()):
            return False
        if not self.is_only_numbers(aircraft.get_plane_wingspan()):
            return False
        return True

    def is_valid_new_destination(self, destination):
        """Checks if all the input from user when making a new destination is valid. If not all is valid returns false"""
        if not self.is_valid_alphabet(destination.get_ident()):
            return False
        if len(destination.get_ident()) != 3:
            return False
        if not self.is_valid_alphabet(destination.get_airport()):
            return False
        if not self.is_only_numbers(destination.get_distance_from_iceland()):
            return False
        if not self.is_valid_alphabet(destination.get_emergency_contact()):
            return False
        if not self.is_valid_contact_number(destination.get_emergency_contact_number()):
            return False
        if not self.is_valid_flight_time(destination):
            return False
        return True
    
    def is_valid_input_flight_time(self, flight_time):
        """Checks if the input flight time from user is valid and on the form HH:MM.
        If it is H:M then it becomes 0H:0M."""
        flight_time_split = flight_time.strip().split(":")

        if len(flight_time_split) != 2:
            return False

        for i in range(len(flight_time_split)):
            if not self.is_only_numbers(flight_time_split[i]):
                return False
            if len(flight_time_split[i]) > 2:
                return False
            elif len(flight_time_split[i]) == 1:
                flight_time_split[i] = "0"+flight_time_split[i]
        
        if not 0 <= int(flight_time_split[0]) < 24:
            return False

        if not 0 <= int(flight_time_split[1]) < 60:
            return False

        return True

    def is_valid_flight_time(self, destination):
        """Checks if the flight time of a destination is valid and on the form HH:MM.
        If it is H:M then it becomes 0H:0M."""
        flight_time = destination.get_flight_time()
        new_flight_time = ""
        flight_time_split = flight_time.strip().split(":")

        if len(flight_time_split) != 2:
            return False

        for i in range(len(flight_time_split)):
            if not self.is_only_numbers(flight_time_split[i]):
                return False
            if len(flight_time_split[i]) > 2:
                return False
            elif len(flight_time_split[i]) == 1:
                flight_time_split[i] = "0"+flight_time_split[i]
        
        if not 0 <= int(flight_time_split[0]) < 24:
            return False

        if not 0 <= int(flight_time_split[1]) < 60:
            return False
        
        new_flight_time += flight_time_split[0] + ":" + flight_time_split[1] + ":00"
        destination.change_flight_time(new_flight_time)
        return True

    def is_valid_contact_number(self, contact_number):
        """Checks if the input phone number is valid. Is only numbers and is of the lenght 7."""
        if not self.is_only_numbers(contact_number):
            return False
        if len(contact_number) != 7:
            return False
        return True

    def is_valid_ssn(self, ssn):
        """Checks if the input social security number is valid. Is only numbers and is of the lenght 10."""
        if len(ssn) != 10:
            return False
        if not ssn.isdigit():
            return False
        return True
    
    def is_empty_string(self, text):
        if len(text) == 0:
            return True
    
    def is_only_numbers(self, text):
        text = text.strip()
        if text.isdigit() and not self.is_empty_string(text):
            return True
        else:
            return False
        
    def is_valid_alphabet(self, name):
        '''Strips the whitespace, splits the words and checks if the string is only alphabet letters'''
        if self.is_empty_string(name):
            return False

        name = name.strip().split()
        for word in name:
            if word.isalpha() == False:
                return False
        return True

    def is_valid_role(self, role):
        """Checks if input role is valid."""
        role = role.lower()
        if role == "pilot" or role == "cabincrew":
            return True
    
    def is_valid_rank(self, role, rank):
        '''Checks if the rank input is valid. Returns True is correct rank is selected.
           Returns False if either string is empty or incorrect'''
        role = role.lower()
        rank = rank.lower()
        if self.is_empty_string(role) == True or self.is_empty_string(rank) == True:
            return False
        if role == "pilot":
            if rank == "copilot" or rank == "captain":
                return True
        elif role =="cabincrew":
            if rank == "flight attendant" or rank == "flight service manager":
                return True
        else:
            return False
    
    def is_valid_licence(self, role, licence):
        """Checks if the input licese if valid (the aircraft type is in the AircraftType.csv file).
        If the role is not a pilot then the allowed licence is empty or "N/A" """
        licence = licence.upper()
        aircraft_list, aircraft_type_list = self.__IoAPI.loadAllAircraftsFromFile()
        if role.lower() =="cabincrew":
            if licence.strip() == "N/A" or licence.strip() == "":
                return True
        
        for aircraft in aircraft_list:
            if aircraft.get_plane_type_id().upper() == licence:
                return True

        return False
    
    def is_valid_date(self, date):
        """Checks if the input date is on the form YYYY-MM-DD. Returns false if not."""
        date_split = date.strip().split("-")
        if len(date_split) != 3:
            return False
        for i in range(len(date_split)):
            if not self.is_only_numbers(date_split[i]):
                return False
        if len(date_split[0]) != 4:
            return False
        if int(date_split[1]) < 0 or int(date_split[1]) > 12:
            return False
        if int(date_split[2]) < 0 or int(date_split[2]) > 31:
            return False
        return True
    
    def is_not_in_past(self, date, time):
        """Checks if the input date is on the form YYYY-MM-DD and if it is not in the past.
        Returns false if not on the right form or if it is in the past."""
        today = datetime.datetime.now()
        if not self.is_valid_date(date):
            return False
        if not self.is_valid_input_flight_time(time):
            return False
        year, month, day = date.split("-")
        hours, minutes = time.split(":")
        date = datetime.datetime(int(year), int(month), int(day), int(hours), int(minutes))
        if today <= date: #check if Date is in past
            return False
        return True

    def is_valid_crew(self, crew):
        """Checks if all the input from user when making a new crew is valid. If not all is valid returns false"""
        if not self.is_valid_ssn(crew.get_ssn()):
            return False

        if not self.is_valid_alphabet(crew.get_name()):
            return False

        if not self.is_valid_role(crew.get_role()):
            return False

        if not self.is_valid_rank(crew.get_role(), crew.get_rank()):
            return False

        if not self.is_valid_licence(crew.get_role(), crew.get_licence()):
            return False

        if self.is_empty_string(crew.get_address()):
            return False
        
        if not self.is_only_numbers(crew.get_phonenumber()):
            return False
        
        return True
    
    def is_valid_ident(self, input_ident, destination_list):
        """Checks if input ident matches an ident of a destination in the destination list. Return false if not."""
        for destination in destination_list:
            if destination.get_ident() == input_ident:
                return True
        return False

    def is_valid_flight_location(self, flight, destination_list):
        """Checks if ident in a destination matches an ident of a destination in the destination list. Return false if not."""
        for destination in destination_list:
            if destination.get_ident() == flight.get_destination():
                return True
        return False

    def is_runway_free(self, flight, flight_list, time_input = None):
        """Checks if another flight has the same departure time. If so returns false."""
        start_time = flight.get_start_time()
        if time_input:
            hour_input, minute_input = time_input.split(":")
            start_time = start_time + datetime.timedelta(hours=int(hour_input), minutes=int(minute_input))

        for f in flight_list:
            if f.get_start_location() == "KEF":
                if f.get_start_time() == start_time:
                    return False
        return True

    def is_available_ident(self, ident):
        destination_list = self.__IoAPI.loadAllDestinationsFromFile()
        if not self.is_valid_alphabet(ident):
            return False
        if len(ident) != 3:
            return False
        for destination in destination_list:
            if destination.get_ident().lower() == ident.lower():
                return False
        return True

    def is_available_ssn(self, ssn):
        """Checks if input ssn matches an ssn of a crew member in the crew list. Return false if not."""
        crew_list = self.__IoAPI.loadAllCrewsFromFile()
        if not self.is_valid_ssn(ssn):
            return False
        for crew in crew_list:
            if crew.get_ssn() == ssn:
                return False
        return True

    def is_valid_flight(self, flight):
        flight_list = self.__IoAPI.loadAllFlightsFromFile()
        destination_list = self.__IoAPI.loadAllDestinationsFromFile()
        crew_list = self.__IoAPI.loadAllFlightsFromFile()

        if not self.is_valid_flight_location(flight, destination_list):
            return False
 
        if not self.is_runway_free(flight, flight_list):
            return False
        return True

    def is_existing_crew(self, ssn):
        """Checks if input ssn matches an ssn of a crew member in the crew list. Return false if not."""
        crew_list = self.__IoAPI.loadAllCrewsFromFile()
        if not self.is_valid_ssn:
            return False, False
        for crew in crew_list:
            if crew.get_ssn() == ssn:
                return True, crew
        return False, False

    def is_valid_flight_number(self, flight):
        if len(flight.get_flight_number()) > 6: 
            return False
        return True

    def is_valid_start_location(self, flight):
        if self.is_only_numbers(flight.get_start_location()):
            return False
        if self.is_empty_string(flight.get_start_location()):
            return False
        return True

    def is_valid_start_time(self, flight):
        if self.is_empty_string(get_start_time()):
            return False
        return True
    
    def is_valid_arrival_time(self, flight):
        if self.is_empty_string(flight.get_arrival_time()):
            return False
        return True

    def is_valid_destination(self, flight):
        """Checks if ident in a destination matches an ident of a destination in the destination list. Return false if not."""
        destination_list = self.__IoAPI.loadAllDestinationsFromFile()
        if flight.get_destination() not in destination_list:
            return False
        if self.is_empty_string(flight.get_destination()):
            return False
        return True

    def is_valid_aircraft(self, flight):
        """Checks if aircraft id in an aircraft matches an aircraft type of an aircraft in the aircraft type list. 
        Return false if not."""
        aircraft_list = self.__IoAPI.loadAllAircraftsFromFile()
        if flight.get_aircraft_id() not in aircraft_list:
            return False
        return True