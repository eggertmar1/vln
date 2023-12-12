from DataLayer.io_api import IoAPI 
from LogicLayer.is_valid_LL import validChecker
from Models.destination import Destination

class DestinationLL:
    def __init__(self):
        self.__IoAPI = IoAPI()
        self.__valid = validChecker()

    def getDestination(self, ident):
        """Gets an input ident from UI and runs it through the destination list.
        If it finds a destination with the same ident it returns that destination."""
        destination_list = self.__IoAPI.loadAllDestinationsFromFile()
        if self.__valid.is_valid_ident(ident, destination_list):
            for destination in destination_list:
                if destination.get_ident() == ident:
                    return destination
        return "Invalid Ident!"

    def getAllDestinations(self):
        """Gets a list of all destinations from IO. Returns the list"""
        destination_list = self.__IoAPI.loadAllDestinationsFromFile()
        return destination_list
    
    def getPopularDestination(self):
        flight_list = self.__IoAPI.loadAllFlightsFromFile()
        destination_list = self.__IoAPI.loadAllDestinationsFromFile()
        destination_dict = dict()
        destination_num_times_list = list()
        for destination in destination_list[1:]:
            ident = destination.get_ident()
            if ident == "KEF":
                continue
            if ident not in destination_dict:
                destination_dict[ident] = 0

        for flight in flight_list:
            destination = flight.get_destination().upper()
            if destination == "KEF":
                continue
            if destination in destination_dict:
                destination_dict[destination] += 1
        
        return destination_dict

    def createDestination(self, destination):
        if self.__valid.is_valid_new_destination(destination):
            self.__IoAPI.storeDestinationToFile(destination)
            return "New destination added!"
        else: 
            return "Invalid Input"
        
    def updateDestination(self, ident, destination_list):
        """Gets a new destination (old but with new information) and the list of all destinations.
        Finds the destination in the destination list and changes its information with the information of the new destination.
        It stores everything in a new list and sends him to the IO to write the file Destinations.csv again (with the new info)"""
        new_destination_list = list()
        
        while not self.__valid.is_valid_ident(ident, destination_list):
            print("Invalid ident!")
            if self.try_again() == "n":
                return False
            ident = input("Enter destination (Ident) from the list to change: ").upper()

        edit_destination = self.getDestination(ident)
        print()
        print(edit_destination)
        emergency_contact = input("Input new emergency contact: ").strip()
        if emergency_contact == "":
                emergency_contact = edit_destination.get_emergency_contact()
        while not self.__valid.is_valid_alphabet(emergency_contact):
            print("Invalid emergency contact")
            if self.try_again() == "n":
                return False
            emergency_contact = input("Input emergency contact: ").strip()
            if emergency_contact == "":
                emergency_contact = edit_destination.get_emergency_contact()
            
        emergency_contact_number = input("Input new emergency contact number: ").strip()
        if emergency_contact_number == "":
                emergency_contact_number = edit_destination.get_emergency_contact_number()
        while not self.__valid.is_valid_contact_number(emergency_contact_number):
            print("Invalid emergancy contact number")
            if self.try_again() == "n":
                return False
            emergency_contact_number = input("Input emergancy contact number: ").strip()
            if emergency_contact_number == "":
                emergency_contact_number = edit_destination.get_emergency_contact_number()

        new_destination = Destination(edit_destination.get_ident(), edit_destination.get_airport(), edit_destination.get_flight_time(), edit_destination.get_distance_from_iceland(),
        emergency_contact, emergency_contact_number)
        print(new_destination)
        for destination in destination_list:
            if destination.get_ident() == new_destination.get_ident():
                destination.change_emergancy_contact(emergency_contact)
                destination.change_emergancy_contact_number(emergency_contact_number)
            new_destination_list.append(destination)
        destination = self.__IoAPI.modifyDestinationToFile(new_destination_list)
        return destination
    
    def try_again(self):
        """If input is invalid it asks to try again if no then it exits the operation."""
        action = input("Try again (y/n)? ")
        return action