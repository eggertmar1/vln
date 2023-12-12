from DataLayer.io_api import IoAPI
from LogicLayer.is_valid_LL import validChecker
import datetime

class CrewLL():   
    def __init__(self):
        self.__IoAPI = IoAPI()
        self.__valid = validChecker()

    def getAllCrew(self):
        """Gets a list of all crews from the file Crew.csv. Returns the list"""
        crew_list = self.__IoAPI.loadAllCrewsFromFile()
        return crew_list
    
    def getAllPilots(self):
        """Gets a list of all crews from the file Crew.csv. Makes a new list with only the pilots
        Returns the pilot list"""
        pilot_list = []
        crew_list = self.__IoAPI.loadAllCrewsFromFile()
        for crew in crew_list:
            if crew.get_role().lower() == "pilot":
                pilot_list.append(crew)
        return pilot_list
    
    def getAllPilotsByAircraftType(self):
        '''finds all pilots by aircraft licence from the all crew member list, returns dictionary'''
        pilot_list = []
        pilot_by_aircrafttype_dict = {}
        crew_list = self.__IoAPI.loadAllCrewsFromFile()
        for crew in crew_list:
            if crew.get_role().lower() == "pilot":
                pilot_list.append(crew)

        aircraft_list, aircraft_type_list = self.__IoAPI.loadAllAircraftsFromFile()
        
        for i in range(1, len(aircraft_list)): #Start at 1 to skip the header line.
            aircraft_type = aircraft_list[i].get_plane_type_id().upper()
            if aircraft_type not in pilot_by_aircrafttype_dict:
                pilot_by_aircrafttype_dict[aircraft_type] = list()
        
        for aircraft_type, set_of_pilots in pilot_by_aircrafttype_dict.items():
            for pilot in pilot_list:
                if aircraft_type == pilot.get_licence().upper():
                    pilot_by_aircrafttype_dict[aircraft_type].append(pilot)

        return pilot_by_aircrafttype_dict

    def getAllFlightAttendants(self):
        '''using the same method to find pilots, to find flight attendands. Returns the list of
        flight attendants'''
        fl_attendants_list = []
        crew_list = self.__IoAPI.loadAllCrewsFromFile()
        for crew in crew_list:
            if crew.get_role().lower() == "cabincrew":
                fl_attendants_list.append(crew)
        return fl_attendants_list
    
    def getCrewByName(self, ssn):
        '''Finding crew member by name using the all-crew-member list. Returns the employee'''
        if self.__valid.is_valid_ssn(ssn):
            crew_list = self.__IoAPI.loadAllCrewsFromFile()
            for crew in crew_list:
                if crew.get_ssn() == ssn:
                    return crew
        return "Invalid SSN"

    def getAvailableCrew(self, date):
        '''finding available and unavailable crew-members by comparing all flights with all crew members, using datetime.
        Returns a set of available crew and a dictionary of the unavailable crew with the information on where they are going'''
        crew_list = self.__IoAPI.loadAllCrewsFromFile()
        flight_list = self.__IoAPI.loadAllFlightsFromFile()
        if self.__valid.is_valid_date(date):
            available_crew_set = set()
            unavailable_crew_dict = dict()
            date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
            for flight in flight_list:
                if flight.get_start_time().date() == date:
                    for working_crew_ssn in flight.get_arranged_crew():
                        for crew in crew_list[1:]:
                            if crew.get_ssn() == working_crew_ssn:
                                if crew not in unavailable_crew_dict:
                                    unavailable_crew_dict[crew] = {flight.get_destination()}
                                else:
                                    unavailable_crew_dict[crew].add(flight.get_destination())

                elif flight.get_arrival_time().date() == date:
                    for working_crew_ssn in flight.get_arranged_crew():
                        for crew in crew_list[1:]:
                            if crew.get_ssn() == working_crew_ssn:
                                if crew not in unavailable_crew_dict:
                                        unavailable_crew_dict[crew] = {flight.get_destination()}
                                else:
                                        unavailable_crew_dict[crew].add(flight.get_destination())

            for crew in crew_list[1:]:
                if crew not in unavailable_crew_dict:
                    available_crew_set.add(crew)

            return available_crew_set, unavailable_crew_dict
        else:
            return "Invalid date!", "Invalid date!"

    def get_available_captains(self, date, aircraft_type):
        available_crew_set, unavailable_crew_dict = self.getAvailableCrew(date)
        available_captains_list = list()
        for crew in available_crew_set:
            if crew.get_rank().lower() == "captain" and crew.get_licence().lower() == aircraft_type.lower():
                available_captains_list.append(crew)
        return available_captains_list

    def get_available_copilots(self, date, aircraft_type):
        available_crew_set, unavailable_crew_dict = self.getAvailableCrew(date)
        available_copilots_list = list()
        for crew in available_crew_set:
            if crew.get_rank().lower() == "copilot" and crew.get_licence().lower() == aircraft_type.lower():
                available_copilots_list.append(crew)
        return available_copilots_list

    def get_available_service_managers(self, date):
        available_crew_set, unavailable_crew_dict = self.getAvailableCrew(date)
        available_service_manager_list = list()
        for crew in available_crew_set:
            if crew.get_rank().lower() == "flight service manager":
                available_service_manager_list.append(crew)
        return available_service_manager_list

    def get_available_cabin_crew(self, date):
        available_crew_set, unavailable_crew_dict = self.getAvailableCrew(date)
        available_cabin_crew_list = list()
        for crew in available_crew_set:
            if crew.get_role().lower() == "cabincrew" and crew.get_rank().lower() == "flight attendant":
                available_cabin_crew_list.append(crew)
        return available_cabin_crew_list
    
    def getPaycheck(self, date, ssn):
        """Gets a list of all flights from the file Flights.csv and makes a new list with only the flights
        that take place in the input week. Checks which of them the input employee has worked on.
        Returns date, employee and a dictionary where the flights (voyages) are the values."""
        crew_flights_dict = dict()
        flight_list = self.__IoAPI.loadAllFlightsFromFile()
        valid_status, crew = self.__valid.is_existing_crew(ssn)
        if self.__valid.is_valid_date(date) and valid_status:
            datetime_object = datetime.datetime.strptime(date, "%Y-%m-%d")
            dates = list()
            for i in range(7):
                next_day = datetime_object + datetime.timedelta(days = i)
                dates.append(next_day.date())
            
            for flight in flight_list:
                if flight.get_start_time().date() in dates:
                    for working_crew_ssn in flight.get_arranged_crew():
                        if ssn == working_crew_ssn:
                            if crew not in crew_flights_dict:
                                crew_flights_dict[crew] = [flight]
                            else:
                                crew_flights_dict[crew].append(flight)

                elif flight.get_start_time().date() in dates:
                    for working_crew_ssn in flight.get_arranged_crew():
                        if ssn == working_crew_ssn:
                            if crew not in crew_flights_dict:
                                crew_flights_dict[crew] = [flight]
                            else:
                                crew_flights_dict[crew].append(flight)
            return crew_flights_dict, dates, crew

        else:
            return "Invalid input!", None, None
    
    def getMostWorkingCrew(self):
        flight_list = self.__IoAPI.loadAllFlightsFromFile()
        crew_list = self.__IoAPI.loadAllCrewsFromFile()
        crew_dict = dict()
        crew_num_flights_list = list()
        for crew in crew_list[1:]:
            ssn = crew.get_ssn()
            if ssn not in crew_dict:
                crew_dict[ssn] = 0

        for flight in flight_list:
            working_crew_ssn = flight.get_arranged_crew()
            for ssn in working_crew_ssn:
                if ssn in crew_dict: 
                    crew_dict[ssn] += 1
        
        return crew_dict

    def createCrew(self, crew):
        """If the input crew from the UI is valid it asks the IO to add the new crew to the Crew.csv file.
        Returns the result"""
        if self.__valid.is_valid_crew(crew):
            if crew.get_role().lower() == "cabincrew":
                if crew.get_licence().strip() == "":
                    crew.change_licence("N/A")
            self.__IoAPI.storeCrewToFile(crew)
            return "New crew member added!"
        else:
            return "Invalid input!"

    def updateCrew(self, crew, crew_list):
        """Gets a new crew member (old but with new information) and the list of all crew.
        Finds the crew member in the crew list and changes its information with the information of the new crew member.
        It stores everything in a new list and sends him to the IO to write the file Crew.csv again (with the new info)"""
        new_crew_list = list()
        if self.__valid.is_valid_crew(crew):
            if crew.get_licence().strip() == "":
                crew.change_licence("N/A")
            for old_crew in crew_list:
                if old_crew.get_ssn() == crew.get_ssn():
                    old_crew.change_role(crew.get_role())
                    old_crew.change_rank(crew.get_rank())
                    old_crew.change_licence(crew.get_licence())
                    old_crew.change_address(crew.get_address())                        
                    old_crew.change_phonenumber(crew.get_phonenumber())
                new_crew_list.append(old_crew)
            result = self.__IoAPI.modifyCrewToFile(new_crew_list)
            return result
        else:
            return "Invalid input!"