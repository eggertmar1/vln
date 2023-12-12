from LogicLayer.logic_layer_api import LLAPI
from Models.flight import Flight
from Models.destination import Destination
from Models.aircraft import Aircraft
from Models.aircraft_type import AircraftType
from Models.crew import Crew
from LogicLayer.is_valid_LL import validChecker
import datetime

class UpdateUI:
    def __init__(self):
        self.__LLAPI = LLAPI()
        self.__valid = validChecker()

    def manageCrew(self):
        selected_flight_attendant = list()

        voyage_list = self.__LLAPI.getAllVoyagesNeedManned()
        if len(voyage_list) == 0:
            print("No voyage need to be manned")
            return

        for number, voyage in enumerate(voyage_list):
            print("{}.".format(number+1))
            for flight in voyage:
                print(flight)
            print()
        num_to_man = input("Enter voyage number from list to man: ")

        # Gets input until valid and returns a voyage (list with 2 flights and their manned status)
        voyage_to_man = self.voyage_input_and_error_check(voyage_list, num_to_man, "voyage number")

        if voyage_to_man == False:
            return
            
        if voyage_to_man[1] == "Not manned":

            date = str(voyage_to_man[0].get_start_time().date())
            
            unavailable_aircrafts_list, available_aircrafts_list = self.__LLAPI.getOccupiedAircrafts(date)

            if len(available_aircrafts_list) == 0:
                print("No aircrafts available")
                return

            for number, aircraft in enumerate(available_aircrafts_list):
                print("Aircraft number: {}\n{}\n".format(number + 1, aircraft[0]))
            aircraft_number = input("Enter aircraft number from list to man: ")

            # Gets input until valid and returns an aircraft not in use
            selected_aircraft = self.voyage_input_and_error_check(available_aircrafts_list, aircraft_number, "aircraft number")
            if selected_aircraft == False:
                return
            # Adds the aircraft to the voyage. items at index 1 and 3 are to indicate if the flight is fully manned
            voyage_to_man[0].set_aircraft_id(selected_aircraft[0].get_plane_insignia())
            voyage_to_man[2].set_aircraft_id(selected_aircraft[0].get_plane_insignia()) 

            available_captains_list = self.__LLAPI.get_available_captains(date, selected_aircraft[0].get_plane_type_id())

            if len(available_captains_list) == 0:
                print("No captain has a license on that aircraft type")
                return

            for number, captain in enumerate(available_captains_list):
                print("Captain number: {}\n{}".format(number + 1, captain))
            captain_number = input("Enter captain number from list to man: ")
            # Gets input until valid and returns a captain (Crew object)
            selected_captain = self.voyage_input_and_error_check(available_captains_list, captain_number, "captain number")
            if selected_captain == False:
                return
            # Captain added to the voyage.
            voyage_to_man[0].set_captain(selected_captain.get_ssn())
            voyage_to_man[2].set_captain(selected_captain.get_ssn())

            available_copilots_list = self.__LLAPI.get_available_copilots(date, selected_aircraft[0].get_plane_type_id())
        
            if len(available_copilots_list) == 0:
                print("No copilot has a license on that aircraft type")
                return

            for number, copilot in enumerate(available_copilots_list):
                print("Copilot number: {}\n{}".format(number + 1, copilot))
            copilot_number = input("Enter Copilot number from list to man: ")


            # Gets input until valid and returns a copilot (Crew object)
            selected_copilot = self.voyage_input_and_error_check(available_copilots_list, copilot_number, "copilot number")
            if selected_copilot == False:
                return
            # Copilot added to voyage
            voyage_to_man[0].set_copilot(selected_copilot.get_ssn())
            voyage_to_man[2].set_copilot(selected_copilot.get_ssn())
    
            available_fsm_list = self.__LLAPI.get_available_service_managers(date)

            if len(available_fsm_list) == 0:
                print("No flight service manager available")
                return

            for number, fsm in enumerate(available_fsm_list):
                print("Service manager number: {}\n{}".format(number + 1, fsm))
            fsm_number = input("Enter service manager number from list to man: ")
            
            # Gets input until valid and returns a flight service manager (Crew object)
            selected_fsm = self.voyage_input_and_error_check(available_fsm_list, fsm_number, "service manager number")
            if selected_fsm == False:
                return
            voyage_to_man[0].set_flight_service_manager(selected_fsm.get_ssn())
            voyage_to_man[2].set_flight_service_manager(selected_fsm.get_ssn())

            add_more = input("Do you wish to add flight attendants to the voyage? y/n: ")
            if add_more.lower() == "n":
                response = self.__LLAPI.manageCrew(voyage_to_man)
                return response
        
        if voyage_to_man[0].get_flight_attendant_1() == "":
            valid_answ = ["y","n"]
            skip_man = input("Do you wish to add flight attendant 1 to the voyage? y/n: ")
            while skip_man.lower() not in valid_answ:
                skip_man = input("Do you wish to add flight attendant 1 to the voyage? y/n: ")
            

            if skip_man == "y":
                date = str(voyage_to_man[0].get_start_time().date())

                available_cabin_list = self.__LLAPI.get_available_cabin_crew(date)

                if len(available_cabin_list) == 0:
                    print("No flight attendants available")
                    return

                for number, cabin_crew in enumerate(available_cabin_list):
                    print("Cabin crew number: {}\n{}".format(number + 1, cabin_crew))
                cabin_number_1 = input("Enter Cabin crew number number from list to man: ")

                selected_cabin_1 = self.voyage_input_and_error_check(available_cabin_list, cabin_number_1, "cabin crew number")
                if selected_cabin_1 == False:
                    return
                voyage_to_man[0].set_flight_attendant_1(selected_cabin_1.get_ssn())
                voyage_to_man[2].set_flight_attendant_1(selected_cabin_1.get_ssn())
        
        if voyage_to_man[0].get_flight_attendant_2() == "":

            valid_answ = ["y","n"]
            # overwrite to be safe
            skip_man = ""
            skip_man = input("Do you wish to add flight attendant 2 to the voyage? y/n: ")
            while skip_man.lower() not in valid_answ:
                skip_man = input("Do you wish to add flight attendant 2 to the voyage? y/n: ")

            if skip_man == "y":
                date = str(voyage_to_man[0].get_start_time().date())

                available_cabin_list = self.__LLAPI.get_available_cabin_crew(date)
                
                for crew in available_cabin_list:
                    if crew.get_ssn() == voyage_to_man[0].get_flight_attendant_1:
                        available_cabin_list.remove(crew)
                
                if len(available_cabin_list) == 0:
                    print("No flight attendants available")
                    return

                for number, cabin_crew in enumerate(available_cabin_list):
                    print("Cabin crew number: {}\n{}".format(number + 1, cabin_crew))
                cabin_number_2 = input("Enter Cabin crew number number from list to man: ")

                selected_cabin_2 = self.voyage_input_and_error_check(available_cabin_list, cabin_number_2, "cabin crew number")
                if selected_cabin_2 == False:
                    return
                voyage_to_man[0].set_flight_attendant_2(selected_cabin_2.get_ssn())
                voyage_to_man[2].set_flight_attendant_2(selected_cabin_2.get_ssn())
                
        response = self.__LLAPI.manageCrew(voyage_to_man)
        print(response)
        return


    def voyage_input_and_error_check(self, airline_list, user_input, context_text):
        while not user_input.isdigit():
            print("Invalid {}!".format(context_text))
            if self.try_again() == "n":
                return False
            user_input = input("Enter {} from list to man: ".format(context_text))
        user_input = int(user_input)

        while user_input < 0 or user_input > len(airline_list):
            print("Invalid {}!".format(context_text))
            if self.try_again() == "n":
                return False
            user_input = input("Enter {} from list to man: ".format(context_text))
            while not user_input.isdigit():
                print("Invalid {}!".format(context_text))
                if self.try_again() == "n":
                    return False
                user_input = input("Enter {} from list to man: ".format(context_text))
            user_input = int(user_input)

        selected_list_item = airline_list[user_input-1]
        return selected_list_item

    def updateCrew(self):
        """Changes the information of a employee and removes the old information about the employee.
        Then adds the new information to the Crew.csv file"""
        crew_list = self.__LLAPI.getAllCrew() 
        for crew in crew_list[1:]:
            print(crew)
        
        edit_ssn = input("Please input a social security number from the list: ")
        edit_crew = self.__LLAPI.getCrewByName(edit_ssn)
        while edit_crew == "Invalid SSN":
            print("Invalid SSN")
            if self.try_again() == "n":
                    return
            edit_ssn = input("Please input a social security number from the list: ")
            edit_crew = self.__LLAPI.getCrewByName(edit_ssn)

        print(edit_crew)
        role = input("Input new Role: ")
        if role.strip() == "": #If empty then nothing is changed
            role = edit_crew.get_role()
        while not self.__valid.is_valid_role(role): #If invalid then it asks to try again
            print("Invalid role")
            if self.try_again() == "n":
                return
            role = input("Input Role: ")
            if role.strip() == "":
                role = edit_crew.get_role()

        rank = input("Input new Rank: ")
        if rank.strip() == "":
            rank = edit_crew.get_rank()
        while not self.__valid.is_valid_rank(role, rank):
            print("Invalid rank")
            if self.try_again() == "n":
                return
            rank = input("Input Rank: ")
            if rank.strip() == "":
                rank = edit_crew.get_rank()

        licence = input("Input new License: ")
        if licence.strip() == "":
            if role.lower() == "pilot":
                licence = edit_crew.get_licence()
            elif role.lower() == "cabincrew":
                licence = "N/A"
        while not self.__valid.is_valid_licence(role, licence):
            print("Invalid license")
            if self.try_again() == "n":
                return
            licence = input("Input License: ")
            if licence.strip() == "":
                licence = edit_crew.get_licence()

        address = input("Input new Address: ")
        if address.strip() == "":
            address = edit_crew.get_address()

        phonenumber = input("Input new Phonenumber: ")
        if phonenumber.strip() == "":
            phonenumber = edit_crew.get_phonenumber()
        while not self.__valid.is_only_numbers(phonenumber):
            print("Invalid phone number")
            if self.try_again() == "n":
                return
            phonenumber = input("Phone number: ")
            if phonenumber.strip() == "":
                phonenumber = edit_crew.get_phonenumber()

        new_crew = Crew(edit_crew.get_ssn(), edit_crew.get_name(), role, rank, licence, address, phonenumber)
        
        print(new_crew)
        response = self.__LLAPI.updateCrew(new_crew, crew_list)

        print(response)

    def updateDestination(self):
        """Changes the information of a destination and removes the old information.
        Then adds the new information to the Destinations.csv file"""
        destination_list = self.__LLAPI.getAllDestinations()
        for destination in destination_list[1:]:
            print(destination)
        
        edit_ident = input("Enter destination (Ident) from the list to change: ").upper()
        response = self.__LLAPI.updateDestination(edit_ident, destination_list)
        if response != False:
            print(response)
        return
    
    def try_again(self):
        """If input is invalid it asks to try again if no then it exits the operation."""
        action = input("Try again (y/n)? ")
        return action