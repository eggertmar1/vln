from Models.flight import Flight
import datetime
class FlightIO:
    def __init__(self):
        self.__flight_filename = "csvFiles/Flights.csv"
    def modifyFlightToFile(self, flight_list):
        '''re-write list to the file with the changed flights'''
        file_stream = open(self.__flight_filename, "w", encoding="utf-8")
        file_stream.write("flightNumber,departingFrom,arrivingAt,departure,arrival,aircraftID,captain,copilot,fsm,fa1,fa2\n")
        for flight in flight_list:
            file_stream.write(flight.add_to_file())
        file_stream.close()
        return "Flight manned!"
        
    def storeFlightToFile(self, flight):
        '''appending flight to appropriate file'''
        file_stream = open(self.__flight_filename, "a", encoding="utf-8")
        file_stream.write(flight.add_to_file())
        file_stream.close()
        
    def loadAllFlightsFromFile(self):
        '''reading all flights from the file, skipping the header of the file'''
        file_stream = open(self.__flight_filename, "r", encoding = "utf-8")
        flight_list = list()
        for line_no, line in enumerate(file_stream):
            if line_no != 0:
                flight_number, start_location, destination, start_time, arrival_time, aircraft_id, captain, copilot, flight_service_manager, flight_attendant_1, flight_attendant_2 = line.strip().split(",")
                start_time_daytime = datetime.datetime.strptime(start_time, "%Y-%m-%dT%H:%M:%S")
                arrival_time_daytime = datetime.datetime.strptime(arrival_time, "%Y-%m-%dT%H:%M:%S")
                flight = Flight(flight_number, start_location, destination, start_time_daytime, arrival_time_daytime, aircraft_id, captain, copilot, flight_service_manager, flight_attendant_1, flight_attendant_2)
                flight_list.append(flight)
        return flight_list