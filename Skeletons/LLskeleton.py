from IOskeleton import IoAPI
from Models import Voyage
class DestinationLL:
    def __init__(self):
        self.__IoAPI = IoAPI()
        self.__valid = validChecker
    def getDestination(airport):
        pass
    def getDestination(self):
        ident = "KEF"           # Hardcoded ident because we don't have that yet
        destination_list = self.__IoAPI.loadAllDestinationsFromFile()
        #print(destination_list)
        destination_searched = []
        for destination in destination_list:
            if destination.get_ident() == ident:
                destination_searched.append(destination)
        return destination_searched

    def getAllDestinations(self):
        destination_list = self.__IoAPI.loadAllDestinationsFromFile()
        return destination_list
    def createDestination(self, destination):
        if self.__valid.is_valid_new_destination(self, destination):
            self.__IoAPI.storeDestinationToFile(destination)
            return "New destination added!"
        else: 
            return "Invalid Input"


        
    def updateDestination():
        pass



class FlightLL:
    def __init__(self):
        self.__IoAPI = IoAPI()
    def getAllFlights(self):
        flight_list = self.__IoAPI.loadAllFlightsFromFile()
    def createFlight(self, flight):
        ''' HAVEN'T MADE THE IS VALID FLIGHT''' #!!!!!! 
        flight_list = self.__IoAPI.storeFlightToFile(flight) 


class VoyageLL:
    def __init__(self):
        self.__IoAPI = IoAPI()
    def getAllVoyages(self):
        flight_list = self.__IoAPI.loadAllFlightsFromFile()
        voyage_list = [] 
        for line_no, flight in enumerate(flight_list, start = 1 ): #START = 1 because HEADERS in file when we take header out, take start!!!
            voyage_list_one = []
            try:
                voyage_list_one.append(flight_list[line_no])
                voyage_list_one.append(flight_list[line_no+1])
                voyage_list.append(voyage_list_one)
            except:
                break
        return voyage_list
    def getVoyageByDay(day):
        pass
    def getVoyageByWeek(week):
        pass
    def createVoyage(Voyage):
        pass
    def updateVoyage(Voyage):
        pass

class AircraftLL():
    def __init__(self):
        self.__IoAPI = IoAPI()
        
    def getAllAircrafts(self):
        aircraft_list, aircraft_type_list = self.__IoAPI.loadAllAircraftsFromFile()
        return aircraft_list, aircraft_type_list
    def createAircraft():
        pass
    def updateAircraft():
        pass
    def getOccupiedAircrafts():
        pass

class CrewLL():

    def __init__(self):
        self.__IoAPI = IoAPI()
        self.__valid = validChecker

    def getAllCrew(self):
        crew_list = self.__IoAPI.loadAllCrewsFromFile()
        return crew_list
    
    def getAllPilots(self):
        pilot_list = []
        crew_list = self.__IoAPI.loadAllCrewsFromFile()
        for crew in crew_list:
            if crew.get_role() == "Pilot":
                pilot_list.append(crew)
        return pilot_list
    
    def getAllPilotsByAircraftType(self):
        pilot_list = []
        pilot_by_aircrafttype_dict = {}
        crew_list = self.__IoAPI.loadAllCrewsFromFile()
        for crew in crew_list:
            if crew.get_role() == "Pilot":
                pilot_list.append(crew)

        aircraft_list, aircraft_type_list = self.__IoAPI.loadAllAircraftsFromFile()
        
        for i in range(1, len(aircraft_list)): #Start at 1 to skip the header line.
            aircraft_type = aircraft_list[i].get_plane_type_id()
            if aircraft_type not in pilot_by_aircrafttype_dict:
                pilot_by_aircrafttype_dict[aircraft_type] = list()
        
        for aircraft_type, set_of_pilots in pilot_by_aircrafttype_dict.items():
            for pilot in pilot_list:
                if aircraft_type == pilot.get_licence():
                    pilot_by_aircrafttype_dict[aircraft_type].append(pilot)

        return pilot_by_aircrafttype_dict




    def getAllFlightAttendants(self):
        fl_attendants_list = []
        crew_list = self.__IoAPI.loadAllCrewsFromFile()
        for crew in crew_list:
            if crew.get_role() == "Cabincrew":
                fl_attendants_list.append(crew)
        return fl_attendants_list
    
    def getCrewByName(self, ssn):
        if self.__valid.is_valid_ssn(self, ssn):
            crew_list = self.__IoAPI.loadAllCrewsFromFile()
            for crew in crew_list:
                if crew.get_ssn() == ssn:
                    return crew
        return "Invalid SSN"


    def createCrew():
        pass
    def updateCrew():
        pass

class validChecker:
    def __init__(self):
        self.__IoAPI = IoAPI()
    
    def is_valid_aircraft_type(self, aircraft_type, aircraft_list):
        valid_aircraft_type_set = set()
        for aircraft in aircraft_list[1:]:
            valid_aircraft_type_set.add(aircraft.get_plane_type_id())
        
        return aircraft_type in valid_aircraft_type_set

    def is_valid_new_destination(self, destination):
        new_flight_time = ""
        ident = destination.get_ident()
        airport = destination.get_airport()
        flight_time = destination.get_flight_time()
        distance_from_iceland = destination.get_distance_from_iceland()
        emergency_contact = destination.get_emergency_contact()
        emergency_contact_number = destination.get_emergency_contact_number()
        try:
            int(ident)
            return False
        except ValueError:
            try:
                int(airport)
                return False
            except ValueError:
                try:
                    int(emergency_contact)
                    return False
                except ValueError:
                    try:
                        int(distance_from_iceland)
                    except ValueError:
                        return False
                    try:
                        int(emergency_contact_number)
                    except ValueError:
                        return False
        if len(ident) != 3:
            return False
        if len(emergency_contact_number) != 7:
            return False
        
        flight_time_split = flight_time.strip().split(":")
        if len(flight_time_split) != 3:
            return False
        for i in range(len(flight_time_split)):
            try:
                int(flight_time_split[i])
            except ValueError:
                return False
            if len(flight_time_split[i]) > 2:
                return False
            elif len(flight_time_split[i]) == 1:
                flight_time_split[i] = "0"+flight_time_split[i]
            
        new_flight_time += flight_time_split[0] + ":" + flight_time_split[1] + ":" + flight_time_split[2]
        destination.change_flight_time(new_flight_time)
        return True
        

    def is_valid_ssn(self, ssn):
        if len(ssn) != 10:
            return False
        try:
            ssn = int(ssn)
            return True
        except ValueError:
            return False
    
    def is_empty_string(text):
        if len(text) == 0:
            return True
    
    def is_only_numbers(text):
        text = text.strip()
        if text.isdigit() and not is_empty_string(text):
            return True
        else:
            return False
        
    def is_valid_alphabet(self, name):
        '''Strips the whitespace, splits the words and checks if the string is only alphabet letters'''
        if is_empty_string(name):
            return False

        name = name.strip().split()
        for word in name:
            if word.isalpha() = False:
                return False
        return True

    def is_valid_role(self, role):
        role = role.lower()
        if role == "pilot" or role == "cabincrew":
            return True
    
    def is_valid_rank(self, role, rank):
        '''Checks if the rank input is valid. Returns True is correct rank is selected.
           Returns False if either string is empty or incorrect'''
        role = role.lower()
        rank = rank.lower()
        if is_empty_string(role) == True or is_empty_string(rank) == True:
            return False
        if role == "pilot":
            if rank == "copilot" or rank == "captain":
                return True
        elif role =="cabincrew":
            if rank == "flight attendant" or rank == "flight service manager":
                return True
        else:
            return False
    
    def is_valid_license(self, licence):
        licence = licence.lower()
        aircraft_list, aircraft_type_list = self.__IoAPI.loadAllAircraftsFromFile()
        for row in aircraft_list:
            if row[1].lower() == license:
                return True
        return False
    


    def is_valid_new_crew(self, crew):
        if not is_valid_ssn(self.get_ssn()):
            return False

        if not is_valid_alphabet(self.get_name()):
            return False

        if not is_valid_role(self.get_role()):
            return False

        if not is_valid_rank(self.get_rank()):
            return False

        if not is_valid_license(self.get_license():
            return False

        if is_empty_string(self.get_address()):
            return False
        
        if not is_only_numbers(self.get_phonenumber()):
            return False
        
        return True
        

class LLAPI():
    def __init__(self):
        self.__crewLL = CrewLL()
        self.__aircraftLL = AircraftLL()
        self.__DestinationLL = DestinationLL()
        self.__flightLL = FlightLL()
        self.__VoyageLL = VoyageLL()
        self.__valid = validChecker()
    

    def createDestination(self, destination):
        return self.__DestinationLL.createDestination(destination)
    def getAllCrew(self):
        return self.__crewLL.getAllCrew()
    def getAllPilots(self):
        return self.__crewLL.getAllPilots()
    def getAllPilotsByAircraftType(self):
        return self.__crewLL.getAllPilotsByAircraftType()
    def getAllFlightAttendants(self):
        return self.__crewLL.getAllFlightAttendants()
    def getCrewByName(self, name):
        return self.__crewLL.getCrewByName(name)
    def getAllDestinations(self):
        return self.__DestinationLL.getAllDestinations()
    def getDestination(self):
        return self.__DestinationLL.getDestination()
    def getAllVoyages(self):
        return self.__VoyageLL.getAllVoyages()
    
    def getAllAircrafts(self):
        return self.__aircraftLL.getAllAircrafts()
    
    def getAllFlights(self):
        return self.__flightLL.getAllFlights()
    
    def is_valid_aircraft_type(self, aircraft_type, aircraft_list):
        return self.__valid.is_valid_aircraft_type(aircraft_type, aircraft_list)

    

