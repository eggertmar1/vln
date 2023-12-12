from DataLayer.destination_io import DestinationIO
from DataLayer.flight_io import FlightIO
from DataLayer.crew_io import CrewIO
from DataLayer.aircraft_io import AircraftIO

class IoAPI(AircraftIO,CrewIO,FlightIO,DestinationIO):
    def __init__(self):
        self.__aircraftIO = AircraftIO()
        self.__crewIO = CrewIO()
        self.__flightIO = FlightIO()
        self.__destinationIO = DestinationIO()
    
    def modifyAircraftToFile(self):
        return self.__aircraftIO.modifyAircraftToFile()
    def storeAircraftToFile(self,aircraft): 
        return self.__aircraftIO.storeAircraftToFile(aircraft)
    def storeAircraftTypeToFile(self,aircraft_type):
        return self.__aircraftIO.storeAircraftTypeToFile(aircraft_type)
    def loadAllAircraftsFromFile(self):
        return self.__aircraftIO.loadAllAircraftsFromFile()

    def modifyCrewToFile(self, crew):
        return self.__crewIO.modifyCrewToFile(crew) 
    def storeCrewToFile(self, crew):
        return self.__crewIO.storeCrewToFile(crew)
    def loadAllCrewsFromFile(self):
        return self.__crewIO.loadAllCrewsFromFile()

    def modifyFlightToFile(self, flight_list):
        return self.__flightIO.modifyFlightToFile(flight_list)
    def storeFlightToFile(self, flight):
        return self.__flightIO.storeFlightToFile(flight)
    def loadAllFlightsFromFile(self):
        return self.__flightIO.loadAllFlightsFromFile()

    def modifyDestinationToFile(self, destination_list):
        return self.__destinationIO.modifyDestinationToFile(destination_list)
    def storeDestinationToFile(self, destination):
        return self.__destinationIO.storeDestinationToFile(destination)
    def loadAllDestinationsFromFile(self):
        return self.__destinationIO.loadAllDestinationsFromFile()