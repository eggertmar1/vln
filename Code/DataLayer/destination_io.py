from Models.destination import Destination
import datetime

class DestinationIO:
    def __init__(self):
        self.__destination_filename = "csvFiles/Destinations.csv"

    def modifyDestinationToFile(self, destination_list):
        '''re-write list to the file with the changed destination'''
        file_stream = open(self.__destination_filename, "w", encoding="utf-8")
        for destination in destination_list:
            file_stream.write(destination.add_to_file())
        file_stream.close()
        return "Updated destination!"

    def storeDestinationToFile(self, destination):
        '''appending destination to file'''
        file_stream = open(self.__destination_filename, "a", encoding = "utf-8")
        file_stream.write(destination.add_to_file())
        file_stream.close()

    def loadAllDestinationsFromFile(self):
        '''reading all destinations from file'''
        file_stream = open(self.__destination_filename, "r", encoding = "utf-8")
        destination_list = list()
        for line in file_stream:
            ident, airport, flight_time, distance_from_iceland, emergency_contact, emergency_contact_number = line.strip().split(",")
            destination = Destination(ident, airport, flight_time, distance_from_iceland, emergency_contact, emergency_contact_number)
            destination_list.append(destination) 
        return destination_list