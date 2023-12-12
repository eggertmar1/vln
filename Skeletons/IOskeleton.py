#aircraftIO 
from Models import Crew
from Models import Aircraft, AircraftType
from Models import Destination
from Models import Flight

class AircraftIO:
    def __init__(self):
        self.__aircraft_filename = "Aircraft.csv" 
        self.__aircraft_type_filename = "AircraftType.csv"

    def modifyAircraftToFile():
        pass
    def storeAircraftToFile(): 
        pass
    def loadAllAircraftsFromFile(self):
        file_stream = open(self.__aircraft_filename, "r", encoding = "utf-8")
        aircraft_list = list()
        for line in file_stream:
            plane_insignia, plane_type_id = line.strip().split(",")
            aircraft = Aircraft(plane_insignia, plane_type_id)
            aircraft_list.append(aircraft)
        file_stream.close()

        file_stream = open(self.__aircraft_type_filename, "r", encoding = "utf-8")
        aircraft_type_list = list()
        for line in file_stream:
            plane_type_id, manufacturer, model, capacity, empty_weight, max_take_off_weight, unit_thrust, service_ceiling, length, height, wingspan = line.split(",")
            aircraft_type = AircraftType(plane_type_id, manufacturer, model, capacity, empty_weight, max_take_off_weight,
                                         unit_thrust, service_ceiling, length, height, wingspan)
            aircraft_type_list.append(aircraft_type)
        file_stream.close()
        return (aircraft_list, aircraft_type_list)
        

class CrewIO:
    def __init__(self):
        self.__crew_filename = "Crew.csv"
    def modifyCrewToFile():
        pass 
    def storeCrewToFile(self, crew):
        file_stream = open(self.__crew_filename, "a", encoding="utf-8")
        file_stream.write(str(crew))
        file_stream.close()
    def loadAllCrewsFromFile(self):
        file_stream = open(self.__crew_filename, "r", encoding = "utf-8")
        crew_list = list()
        for line in file_stream:
            ssn, name, role, rank, licence, address, phonenumber = line.split(",")
            crew = Crew(ssn, name, role, rank, licence, address, phonenumber)
            crew_list.append(crew) 
        return crew_list


class FlightIO:
    def __init__(self):
        self.__flight_filename = "Flights.csv"
    def modifyFlightToFile():
        pass
    def storeFlightToFile(self, flight):
        file_stream = open(self.__flight_filename, "a", encoding="utf-8")
        file_stream.write(flight.add_to_file())
        file_stream.close()
        

    def loadAllFlightsFromFile(self):
        file_stream = open(self.__flight_filename, "r", encoding = "utf-8")
        flight_list = list()
        for line in file_stream:
            flight_number, start_location, destination, start_time, arrival_time, aircraft_id, captain, copilot, flight_service_manager, flight_attendant_1, flight_attendant_2 = line.strip().split(",")
            flight = Flight(flight_number, start_location, destination, start_time, arrival_time, aircraft_id, captain, copilot, flight_service_manager, flight_attendant_1, flight_attendant_2)
            flight_list.append(flight)
        return flight_list

class DestinationIO:
    def __init__(self):
        self.__destination_filename = "Destinations.csv"
    def modifyDestinationToFile():
        pass
    def storeDestinationToFile(self, destination):
        file_stream = open(self.__destination_filename, "a", encoding = "utf-8")
        file_stream.write(destination.add_to_file())
        file_stream.close()

    def loadAllDestinationsFromFile(self):
        file_stream = open(self.__destination_filename, "r", encoding = "utf-8")
        destination_list = list()
        for line in file_stream:
            ident, airport, flight_time, distance_from_iceland, emergency_contact, emergency_contact_number = line.split(",")
            destination = Destination(ident, airport, flight_time, distance_from_iceland, emergency_contact, emergency_contact_number)
            destination_list.append(destination) 
        return destination_list


class IoAPI(AircraftIO,CrewIO,FlightIO,DestinationIO):
    def __init__(self):
        self.__aircraftIO = AircraftIO()
        self.__crewIO = CrewIO()
        self.__flightIO = FlightIO()
        self.__destinationIO = DestinationIO()
    
    def modifyAircraftToFile(self):
        return self.__aircraftIO.modifyAircraftToFile()
    def storeAircraftToFile(self): 
        return self.__aircraftIO.storeAircraftToFile()
    def loadAllAircraftsFromFile(self):
        return self.__aircraftIO.loadAllAircraftsFromFile()

    def modifyCrewToFile(self):
        return self.__crewIO.modifyCrewToFile() 
    def storeCrewToFile(self):
        return self.__crewIO.storeCrewToFile()
    def loadAllCrewsFromFile(self):
        return self.__crewIO.loadAllCrewsFromFile()

    def modifyFlightToFile(self):
        return self.__flightIO.modifyFlightToFile()
    def storeFlightToFile(self, flight):
        return self.__flightIO.storeFlightToFile(flight)
    def loadAllFlightsFromFile(self):
        return self.__flightIO.loadAllFlightsFromFile()

    def modifyDestinationToFile(self):
        return self.__destinationIO.modifyDestinationToFile()
    def storeDestinationToFile(self, destination):
        return self.__destinationIO.storeDestinationToFile(destination)
    def loadAllDestinationsFromFile(self):
        return self.__destinationIO.loadAllDestinationsFromFile()

