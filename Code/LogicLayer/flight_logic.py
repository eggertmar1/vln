from DataLayer.io_api import IoAPI
from LogicLayer.is_valid_LL import validChecker
from Models.flight import Flight
import datetime

class FlightLL:
    def __init__(self):
        self.__IoAPI = IoAPI()
        self.__valid = validChecker()

    def getAllFlights(self):
        """Gets a list of all flights from the Flights.csv file from IO. Returns the list."""
        flight_list = self.__IoAPI.loadAllFlightsFromFile()
        return flight_list

    def createFlight(self, flight):
        '''Gets a half finished object from the Presentation Layer. Need to plug in start location, destination and arrival time and create.
           Start location and destination are both destination objects and start time and arrival time are datetime objects.
           Flight time is found in the destination object
           The flight is sent to the IO for creation.'''

        flight_list = self.__IoAPI.loadAllFlightsFromFile()
        
        destinations = self.__IoAPI.loadAllDestinationsFromFile()

        # Makes a dictionary of template flight numbers based on destination
        # Key is the ident and value is 2 digit string with 1 padded if the number is below 10
        number_dict = dict()
        for index, dest in enumerate(destinations):
            number_dict[dest.get_ident().lower()] = str(index).zfill(2)
        
        last_flight_number = ""

        # Reverse the list so I can quickly find the last flight
        flight_list.reverse()
        for f in flight_list:
            if f.get_destination() == flight.get_destination():
                
                last_flight_number = f.get_flight_number()
                # Take last 2 digits, cast them to int and add 2 since I will find the departure flight first
                new_num = int(last_flight_number[-2:]) + 2
                # Take the first 4 numbers, "NA + destination ident" and add the new number behind it
                last_flight_number = last_flight_number[:4] + str(new_num).zfill(2)
                break

        # If there has is no past flight to the destination. We make a new number
        if last_flight_number == "":
            last_flight_number = "NA" + number_dict[flight.get_destination().lower()] + "00"


        flight.set_flight_number(last_flight_number)


        # Loop through the destination list to find the correct destination object we need for flight time
        destination = ""
        for d in destinations:
            if d.get_ident() == flight.get_destination():
                destination = d
        flight.set_start_location("KEF")
    
        # Gets the flight time from the destination object and splits it into hours, minutes and seconds
        hour, minute, second = destination.get_flight_time().split(":")
        # Arrival time is start time + flight time
        arrival_time = flight.get_start_time() + datetime.timedelta(hours=int(hour), minutes=int(minute), seconds=int(second))
        flight.set_arrival_time(arrival_time)
        
        if self.__valid.is_valid_flight(flight):
            self.__IoAPI.storeFlightToFile(flight)
        else:
            return "Invalid flight"

        # Reverses the process for the flight home
        return_flight_number = flight.get_flight_number()
        return_flight_number = int(last_flight_number[-2:]) + 1
        return_flight_number = "NA" + number_dict[flight.get_destination().lower()] + str(return_flight_number).zfill(2)
        return_flight_start = flight.get_destination()
        return_flight_destination = flight.get_start_location()
        # Aircraft stays for 1 hour before going back.
        return_flight_start_time = flight.get_arrival_time() + datetime.timedelta(hours=1)
        return_flight_arrival_time = return_flight_start_time + datetime.timedelta(hours=int(hour), minutes=int(minute), seconds=int(second))

        return_flight = Flight(return_flight_number, return_flight_start, return_flight_destination, return_flight_start_time, return_flight_arrival_time, "", "", "", "", "", "")
        self.__IoAPI.storeFlightToFile(return_flight)