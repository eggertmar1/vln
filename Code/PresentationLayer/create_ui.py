from LogicLayer.logic_layer_api import LLAPI
from Models.flight import Flight
from Models.destination import Destination
from Models.aircraft import Aircraft
from Models.aircraft_type import AircraftType
from Models.crew import Crew
from LogicLayer.is_valid_LL import validChecker
import datetime

class CreateUI:
    def __init__(self):
        self.__LLAPI = LLAPI()
        self.__valid = validChecker()

    def createAircraft(self):
        """Creates a new aircraft and adds it to the Aircraft.csv file.
        If the aircraft type of the new aircraft isn't in the AircraftType.csv file it 
        creates a new aircraft type and adds it to the file."""
        insignia = input("Input aircraft insignia: ").upper()
        while self.__valid.is_empty_string(insignia):
            print("Invalid aircraft insignia")
            if self.try_again() == "n":
                return
            insignia = input("Input aircraft insignia: ").upper()
            
        plane_type = input("Input aircraft type: ") 
        while self.__valid.is_empty_string(plane_type):
            print("Invalid plane type")
            if self.try_again() == "n":
                return
            plane_type = input("Input aircraft type: ")

        new_aircraft = Aircraft(insignia, plane_type)
        response = self.__LLAPI.createAircraft(new_aircraft)
        if response == "New aircraft added!":
            print(response)
        elif response == None: #If the type isn't in the aircraft_type.csv file it adds the type there.
            print("You are adding a new type to the aircraft types")
            aircraft_type = self.createAircraftType(plane_type)
            if aircraft_type == "New aircraft type added!":
                print(aircraft_type)
                response = self.__LLAPI.createAircraft(new_aircraft)
                print(response)
            else:
                print(aircraft_type)
        else:
            print(response)
                
    def createAircraftType(self, plane_type_id = None):
        """Creates a new aircraft type and adds it to the AircraftType.csv file."""
        if plane_type_id == None:
            plane_type_id = input("Input type ID: ")
            while self.__valid.is_empty_string(plane_type_id):
                print("Invalid plane type ID")
                if self.try_again() == "n":
                    return
                plane_type_id = input("Input type ID: ")

        manufacturer = input("Input manufacturer: ")
        while self.__valid.is_empty_string(manufacturer):
            print("Invalid manufacturer")
            if self.try_again() == "n":
                return
            manufacturer = input("Input manufacturer: ")

        model = input("Input model: ")
        while self.__valid.is_empty_string(model):
            print("Invalid model")
            if self.try_again() == "n":
                return
            model = input("Input model: ")

        capacity = input("Input seat capacity: ")
        while not self.__valid.is_only_numbers(capacity):
            print("Invalid capacity")
            if self.try_again() == "n":
                return
            capacity = input("Input seat capacity: ")

        empty_weight = input("Input empty weight: ")
        while not self.__valid.is_only_numbers(empty_weight):
            print("Invalid empty weight")
            if self.try_again() == "n":
                return
            empty_weight = input("Input empty weight: ")

        max_take_off_weight = input("Input maximum take-off weight: ")
        while not self.__valid.is_only_numbers(max_take_off_weight):
            print("Invalid max take off weight")
            if self.try_again() == "n":
                return
            max_take_off_weight = input("Input maximum take-off weight: ")

        unit_thrust = input("Input thrust: ")
        while not self.__valid.is_only_numbers(unit_thrust):
            print("Invalid thrust")
            if self.try_again() == "n":
                return
            unit_thrust = input("Input thrust: ")

        service_ceiling = input("Input service ceiling: ")
        while not self.__valid.is_only_numbers(service_ceiling):
            print("Invalid service ceiling")
            if self.try_again() == "n":
                return
            service_ceiling = input("Input service ceiling: ")

        length = input("Input length of aircraft: ")
        while not self.__valid.is_only_numbers(length):
            print("Invalid lenght")
            if self.try_again() == "n":
                return
            length = input("Input length of aircraft: ")

        height = input("Input height of aircraft: ")
        while not self.__valid.is_only_numbers(height):
            print("Invalid height")
            if self.try_again() == "n":
                return
            height = input("Input height of aircraft: ")

        wingspan = input("Input wingspan of aircraft: ")
        while not self.__valid.is_only_numbers(wingspan):
            print("Invalid wingspan")
            if self.try_again() == "n":
                return
            wingspan = input("Input wingspan of aircraft: ")

        new_aircraft_type = AircraftType(plane_type_id,manufacturer,model,capacity,empty_weight,max_take_off_weight,unit_thrust,service_ceiling
                                    ,length,height,wingspan)
        aircraft_type = self.__LLAPI.createAircraftType(new_aircraft_type)
        return aircraft_type

    def createCrewMember(self):
        """Creates a new employee and adds it to the Crew.csv file."""
        ssn = input("Input Social security number: ")
        while not self.__valid.is_available_ssn(ssn):
            print("Invalid Social security number (Might be already in use)")
            if self.try_again() == "n":
                return
            ssn = input("Input Social security number: ")

        name = input("Input Name: ")
        while not self.__valid.is_valid_alphabet(name):
            print("Invalid name")
            if self.try_again() == "n":
                return
            name = input("Input Name: ")

        role = input("Input Role: ")
        while not self.__valid.is_valid_role(role):
            print("Invalid role")
            if self.try_again() == "n":
                return
            role = input("Input Role: ")

        rank = input("Input Rank: ")
        while not self.__valid.is_valid_rank(role, rank):
            print("Invalid rank")
            if self.try_again() == "n":
                return
            rank = input("Input Rank: ")

        licence = input("Input License: ")
        while not self.__valid.is_valid_licence(role, licence):
            print("Invalid license")
            if self.try_again() == "n":
                return
            licence = input("Input License: ")

        address = input("Input Address: ")
        while self.__valid.is_empty_string(address):
            print("Invalid address")
            if self.try_again() == "n":
                return
            address = input("Input Address: ")

        phonenumber = input("Phone number: ")
        while not self.__valid.is_only_numbers(phonenumber):
            print("Invalid phone number")
            if self.try_again() == "n":
                return
            phonenumber = input("Phone number: ")

        new_crew = Crew(ssn, name, role, rank, licence, address, phonenumber)
        response = self.__LLAPI.createCrewMember(new_crew)
        print(response)
        return

    def createDestination(self):
        """Creates a new destination and adds it to the Destinations.csv file."""
        ident = input("Input ident: ").strip().upper()
        while not self.__valid.is_available_ident(ident):
            print("Invalid ident (Might be already in use)")
            if self.try_again() == "n":
                return
            ident = input("Input ident: ").strip().upper()

        airport = input("Input arrival airport: ").strip()
        while not self.__valid.is_valid_alphabet(airport):
            print("Invalid airport")
            if self.try_again() == "n":
                return
            airport = input("Input arrival airport: ").strip()

        flight_time = input("Input flight time (hh:mm): ").strip()
        while not self.__valid.is_valid_input_flight_time(flight_time):
            print("Invalid flight time")
            if self.try_again() == "n":
                return
            flight_time = input("Input flight time (hh:mm): ").strip()

        distance_from_iceland = input("Input distance from Reykjavík (km): ").strip()
        while not self.__valid.is_only_numbers(distance_from_iceland):
            print("Invalid distance")
            if self.try_again() == "n":
                return
            distance_from_iceland = input("Input distance from Reykjavík (km): ").strip()

        emergency_contact = input("Input emergency contact: ").strip()
        while not self.__valid.is_valid_alphabet(emergency_contact):
            print("Invalid emergency contact")
            if self.try_again() == "n":
                return
            emergency_contact = input("Input emergency contact: ").strip()

        emergency_contact_number = input("Input emergency contact number: ").strip()
        while not self.__valid.is_valid_contact_number(emergency_contact_number):
            print("Invalid emergency contact number")
            if self.try_again() == "n":
                return
            emergency_contact_number = input("Input emergency contact number: ").strip()

        new_destination = Destination(ident, airport, flight_time, distance_from_iceland, emergency_contact, emergency_contact_number)
        destination = self.__LLAPI.createDestination(new_destination)
        print(destination)
        return

    def createFlight(self):
        """Creates a new flight out and automatically makes a flight in
        (voyage) and adds the flights to the Flights.csv file."""
        destination_list = self.__LLAPI.getAllDestinations()
        flight_list = self.__LLAPI.getAllFlights()

        create_flight = Flight('','','','','','','','','','','')

        destination = input("Input destination Ident: ").upper()
        while not self.__valid.is_valid_ident(destination, destination_list) or destination.lower() == "kef":
            print("Incorrect destination ident!")
            if self.try_again() == "n":
                return
            destination = input("Input destination Ident: ").upper()
        create_flight.set_destination(destination)

        date = input("Input departure date in the format yyyy-mm-dd: ")
        time = input("Input departure time in the format hh:mm: ")
        while self.__valid.is_not_in_past(date, time) or not self.__valid.is_valid_input_flight_time(time):
            print("Incorrect date or time!")
            if self.try_again() == "n":
                return
            date = input("Input departure date in the format yyyy-mm-dd: ")
            time = input("Input departure time in the format hh:mm: ")

        year, month, day = date.split("-")
        dt = datetime.datetime(int(year), int(month), int(day))
        create_flight.set_start_time(dt)
        
        while not self.__valid.is_runway_free(create_flight, flight_list, time):
            print("Runway taken!")
            if self.try_again() == "n":
                return
            time = input("Input departure time in the format hh:mm: ")
            while not self.__valid.is_valid_input_flight_time(time):
                print("Runway taken or your time input is not following the format hh:mm")
                if self.try_again() == "n":
                    return
                time = input("Input departure time in the format hh:mm: ")
        
        hour, minute = time.split(":")
        create_flight.set_start_time(datetime.datetime(int(year), int(month), int(day), int(hour), int(minute)))
        self.__LLAPI.createFlight(create_flight)
        print("Voyage added!")

    def try_again(self):
        """If input is invalid it asks to try again if no then it exits the operation."""
        action = input("Try again (y/n)? ")
        return action