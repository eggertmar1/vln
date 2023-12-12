
from LogicLayer.aircraft_logic import AircraftLL
from LogicLayer.crew_logic import CrewLL
from LogicLayer.destination_logic import DestinationLL
from LogicLayer.flight_logic import FlightLL
from LogicLayer.voyage_logic import VoyageLL
from LogicLayer.is_valid_LL import validChecker


class LLAPI():
    def __init__(self):
        self.__CrewLL = CrewLL()
        self.__AircraftLL = AircraftLL()
        self.__DestinationLL = DestinationLL()
        self.__FlightLL = FlightLL()
        self.__VoyageLL = VoyageLL()
        self.__valid = validChecker()

    def createCrewMember(self, crew):
        return self.__CrewLL.createCrew(crew)
    def createDestination(self, destination):
        return self.__DestinationLL.createDestination(destination)
    def createAircraft(self, aircraft):
        return self.__AircraftLL.createAircraft(aircraft)
    def createAircraftType(self,aircraft_type):
        return self.__AircraftLL.createAircraftType(aircraft_type)
    def getAllCrew(self):
        return self.__CrewLL.getAllCrew()
    def getAllPilots(self):
        return self.__CrewLL.getAllPilots()
    def getAllPilotsByAircraftType(self):
        return self.__CrewLL.getAllPilotsByAircraftType()
    def getAllFlightAttendants(self):
        return self.__CrewLL.getAllFlightAttendants()
    def getCrewByName(self, name):
        return self.__CrewLL.getCrewByName(name)
    def getAvailableCrew(self, date):
        return self.__CrewLL.getAvailableCrew(date)
    def getPaycheck(self, date, ssn):
        return self.__CrewLL.getPaycheck(date, ssn)
    def getMostWorkingCrew(self):
        return self.__CrewLL.getMostWorkingCrew()
    def getAllDestinations(self):
        return self.__DestinationLL.getAllDestinations()
    def getDestination(self, ident):
        return self.__DestinationLL.getDestination(ident)
    def getPopularDestination(self):
        return self.__DestinationLL.getPopularDestination()
    def getAllVoyages(self):
        return self.__VoyageLL.getAllVoyages()
    def getVoyageByWeek(self, date):
        return self.__VoyageLL.getVoyageByWeek(date)
    def getVoyageByDay(self, date):
        return self.__VoyageLL.getVoyageByDay(date)
    def getVoyageToday(self):
        return self.__VoyageLL.getVoyageToday()
    def getAllVoyagesNeedManned(self):
        return self.__VoyageLL.getAllVoyagesNeedManned()
    def getAllAircrafts(self):
        return self.__AircraftLL.getAllAircrafts()
    def getOccupiedAircrafts(self, date):
        return self.__AircraftLL.getOccupiedAircrafts(date)

    def get_available_captains(self, date, aircraft_type):
        return self.__CrewLL.get_available_captains(date, aircraft_type)

    def get_available_copilots(self, date, aircraft_type):
        return self.__CrewLL.get_available_copilots(date, aircraft_type)

    def get_available_service_managers(self, date):
        return self.__CrewLL.get_available_service_managers(date)
    
    def get_available_cabin_crew(self, date):
        return self.__CrewLL.get_available_cabin_crew(date)

    def getAllFlights(self):
        return self.__FlightLL.getAllFlights()
    
    def is_valid_aircraft_type(self, aircraft_type, aircraft_list):
        return self.__valid.is_valid_aircraft_type(aircraft_type, aircraft_list)

    def is_valid_crew(self, crew):
        return self.__valid.is_valid_crew(crew)
    
    def is_valid_ident(self, input_ident, destination_list):
        return self.__valid.is_valid_ident(input_ident, destination_list)
    
    def is_valid_alphabet(self, text):
        return self.__valid.is_valid_alphabet(text)
    
    def is_valid_contact_number(self, contact_number):
        return self.__valid.is_valid_contact_number(contact_number)
    
    def createCrew(self, crew):
        return self.__CrewLL.createCrew(crew)
    
    def updateCrew(self, crew, crew_list):
        return self.__CrewLL.updateCrew(crew, crew_list)
    
    def updateDestination(self, ident, destination_list):
        return self.__DestinationLL.updateDestination(ident, destination_list)
    
    def createFlight(self, flight):
        return self.__FlightLL.createFlight(flight)

    def manageCrew(self, voyage):
        return self.__VoyageLL.manageCrew(voyage)
