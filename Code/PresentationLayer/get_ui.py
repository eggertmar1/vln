
from Models.flight import Flight
from Models.destination import Destination
from Models.aircraft import Aircraft
from Models.aircraft_type import AircraftType
from Models.crew import Crew

import datetime
from LogicLayer.logic_layer_api import LLAPI


class GetUI():
    def __init__(self):
        self.__LLAPI = LLAPI()

    def showPilots(self):
        """Gets a list of all pilots and prints it out"""
        pilot_list = self.__LLAPI.getAllPilots()
        for pilot in pilot_list:
           print(pilot)
        return pilot_list
    
    def showPilotsByAircraftType(self):
        """Gets a list of pilots that have license on aircraft type and prints it out"""
        pilot_by_aircrafttype_dict = self.__LLAPI.getAllPilotsByAircraftType()
        
        for aircraft_type in pilot_by_aircrafttype_dict.keys():
            number_of_pilots = 0
            print("{}:".format(aircraft_type))
            for pilot in pilot_by_aircrafttype_dict[aircraft_type]:
                print("\t{} | {} | {} | {} | {}".format(pilot.get_ssn(), pilot.get_name(), pilot.get_rank(), pilot.get_address(), pilot.get_phonenumber()))
                number_of_pilots += 1
            print("{} Pilots have license on {} aircraft!".format(number_of_pilots, aircraft_type))
            print()
    
    def showPilotsByInputAircraftType(self):
        """Gets a list of pilots that have license on input aircraft type and prints it out"""
        pilot_by_aircrafttype_dict = self.__LLAPI.getAllPilotsByAircraftType()
        aircraft_list, aircraft_type_list = self.__LLAPI.getAllAircrafts()
        aircraft_type = input("Input aircraft type: ").upper()
        if self.__LLAPI.is_valid_aircraft_type(aircraft_type, aircraft_list):
            number_of_pilots = 0
            for pilot in pilot_by_aircrafttype_dict[aircraft_type]:
                print("\t{} | {} | {} | {} | {}".format(pilot.get_ssn(), pilot.get_name(), pilot.get_rank(), pilot.get_address(), pilot.get_phonenumber()))
                number_of_pilots += 1
            print("{} Pilots have license on {} aircraft!".format(number_of_pilots, aircraft_type))
            return pilot_by_aircrafttype_dict
        else:
            print("Aircraft type not found!")
            return "Aircraft type not found!"

    def showAllStaff(self):
        """Gets a list of all staff and prints it out"""
        crew_list = self.__LLAPI.getAllCrew()
        for crew in crew_list[1:]:
            print(crew)
        return crew_list
        
    def showFlightAttendants(self):
        """Gets a list of all flight attendants and prints it out"""
        fl_attendant_list = self.__LLAPI.getAllFlightAttendants()
        for flight_attendant in fl_attendant_list:
            print(flight_attendant)
        return fl_attendant_list
    
    def showCrewByName(self):
        """Gets a string of employee with the input social security number and prints it out"""
        ssn = input("Input SSN: ")
        name = self.__LLAPI.getCrewByName(ssn)
        print(name)
        return name

    def showAllDestinations(self):
        """Gets a list of all destinations and prints it out"""
        destination_list = self.__LLAPI.getAllDestinations()
        for destination in destination_list[1:]:
            print(destination)
        return destination_list

    def showDestination(self):
        """Gets a destination with the input ident and prints it out"""
        ident = input("Input ident: ").strip().upper()
        destination = self.__LLAPI.getDestination(ident)
        print(destination)
        return destination
    
    def showAllVoyages(self):
        """Gets a list of all voyages and its status and prints it out"""
        voyages_list = self.__LLAPI.getAllVoyages()
        print("All voyages:")
        for i in range(1, len(voyages_list), 2):
            print("Out: {}\n{} | {}".format(voyages_list[i-1][0], voyages_list[i-1][1], voyages_list[i-1][2]))
            print("In: {}\n{} | {}".format(voyages_list[i][0], voyages_list[i][1], voyages_list[i][2]))
            print()
        return voyages_list

    def showAllAircrafts(self):
        """Gets a list of all aircrafts and prints it out"""
        aircraft_list, aircraft_type_list = self.__LLAPI.getAllAircrafts()
        for aircraft in aircraft_list:
            print(aircraft)
        return aircraft_list

    def showVoyagesByWeek(self):
        """Gets a list of all voyages in an input week and its status and prints it out"""
        date = input("Input start of week (yyyy-mm-dd): ")
        flights_and_status_list, dates = self.__LLAPI.getVoyageByWeek(date)
        if flights_and_status_list != "Invalid date!":
            print()
            print("Voyages in week: {} - {}".format(dates[0], dates[-1]))
            if len(flights_and_status_list) == 0:
                print("No voyages in that week")
                print()
            else:
                for i in range(1, len(flights_and_status_list), 2):
                    print("Out: {}\n{} | {}".format(flights_and_status_list[i-1][0], flights_and_status_list[i-1][1], flights_and_status_list[i-1][2]))
                    print("In: {}\n{} | {}".format(flights_and_status_list[i][0], flights_and_status_list[i][1], flights_and_status_list[i][2]))
                    print()
        else:
            print(flights_and_status_list)
        return flights_and_status_list

    def showVoyagesByDay(self):
        """Gets a list of all voyages in an input day and its status and prints it out"""
        date = input("Input date (yyyy-mm-dd): ")
        flights_and_status_list, date = self.__LLAPI.getVoyageByDay(date)
        if flights_and_status_list != "Invalid date!":
            print()
            print("Voyages on day: {}".format(date))
            if len(flights_and_status_list) == 0:
                print("No voyages on that day")
                print()
            else:
                for i in range(1, len(flights_and_status_list), 2):
                    print("Out: {}\n{} | {}".format(flights_and_status_list[i-1][0], flights_and_status_list[i-1][1], flights_and_status_list[i-1][2]))
                    print("In: {}\n{} | {}".format(flights_and_status_list[i][0], flights_and_status_list[i][1], flights_and_status_list[i][2]))
                    print()
        else:
            print(flights_and_status_list)
        return flights_and_status_list
    
    def showVoyageToday(self):
        """Gets a list of all voyages today and its status and prints it out"""
        flights_and_status_list, today = self.__LLAPI.getVoyageToday()
        print()
        print("Voyages today: {}".format(today))
        if len(flights_and_status_list) == 0:
            print("No voyages today")
            print()
        else:
            for i in range(1, len(flights_and_status_list), 2):
                print("Out: {}\n{} | {}".format(flights_and_status_list[i-1][0], flights_and_status_list[i-1][1], flights_and_status_list[i-1][2]))
                print("In: {}\n{} | {}".format(flights_and_status_list[i][0], flights_and_status_list[i][1], flights_and_status_list[i][2]))
                print()

    def showAvailableCrew(self):
        """Gets a list of all available and unavailable crew on input day
        and prints out the list of available employees"""
        date = input("Input date (yyyy-mm-dd): ")
        available_crew_set, unavailable_crew_dict = self.__LLAPI.getAvailableCrew(date)
        if available_crew_set != "Invalid date!":
            if available_crew_set:
                print()
                print("Available Crew:")
                for crew in available_crew_set:
                    print(crew)
            else:
                print("No available crew!")
        else:
            print(available_crew_set)
        return available_crew_set
        
    def showUnavailableCrew(self):
        """Gets a list of all available and unavailable crew on input day
        and prints out the list of unavailable employees"""
        date = input("Input date (yyyy-mm-dd): ")
        available_crew_set, unavailable_crew_dict = self.__LLAPI.getAvailableCrew(date)
        if unavailable_crew_dict != "Invalid date!":
            if unavailable_crew_dict:
                print()
                print("Unavailable Crew:")
                for crew, destination in unavailable_crew_dict.items():
                    print("\n{}".format(crew.get_name()))
                    print("\tDestinations:", end=" ")
                    for des in destination:
                        print(des, end=" ")
                    print("\n\tssn: {}\n\tRole: {}\n\tRank: {}\n\tLicense: {}\n\tAddress: {}\n\tPhonenumber: {}".format(crew.get_name(), crew.get_ssn(), crew.get_role(), crew.get_rank(), crew.get_licence(), crew.get_address(), crew.get_phonenumber())) 
            else:
                print("All crew is available!")
        else:
            print(unavailable_crew_dict)
        return unavailable_crew_dict

    def showOccupiedAircrafts(self):
        """Gets a list of all available and unavailable crew on input day
        and prints out both list"""
        date = input("Input date (yyyy-mm-dd): ")
        unavailable_aircrafts_list, available_aircrafts_list = self.__LLAPI.getOccupiedAircrafts(date)
        if unavailable_aircrafts_list != "Invalid date!":
            print()
            print("Available aircrafts:")
            print("\t{:<6s} | {:<12s} | {}".format("Name", "Type", "Capacity"))
            for aircraft, capacity in available_aircrafts_list:
                print("\t{} | {:<12s} | {}".format(aircraft.get_plane_insignia(), aircraft.get_plane_type_id(), capacity))
            
            print()
            print("Unavailable aircrafts:")
            print("\t{:<6s} | {:<12s} | {}".format("Name", "Type", "Capacity"))
            for aircraft, capacity, info in unavailable_aircrafts_list:
                print("\t{} | {:<12s} | {}".format(aircraft.get_plane_insignia(), aircraft.get_plane_type_id(), capacity))
                if len(info) == 2:
                    print("\tFlight number: {} | Destination: {}\n\tFlight number: {} | Destination: {} \n\tAvailable next: {}\n".format(info[0][0], info[0][1], info[1][0], info[1][1], info[1][2]))
                else:
                    print("\tFlight number: {} | Destination: {}\n\tAvailable next: {}\n".format(info[0][0], info[0][1], info[0][2]))
        else:
            print(unavailable_aircrafts_list)
        return unavailable_aircrafts_list
        
    def showPaycheck(self):
        """Gets a list of all voyages by a employee on input week and prints it out"""
        date = input("Input start of week (yyyy-mm-dd): ")
        ssn = input("Input ssn: ")
        crew_flights_dict, dates, crew = self.__LLAPI.getPaycheck(date, ssn)
        if crew:
            num_of_voyages = 0
            print(crew.get_name())
            print("Week: {} - {}".format(dates[0], dates[-1]))
            print("Voyages:")
            for flights in crew_flights_dict.values():
                for i in range(1, len(flights), 2):
                    print("\t{}\n\t{}".format(flights[i-1], flights[i]))
                    print()
                    num_of_voyages += 1
            print("Number of voyages: {}".format(num_of_voyages))    
            
                
        else:
            print(crew_flights_dict)
        return crew_flights_dict

    def showPopularDestination(self):
        """Gets a dict of all destinations and how many times it was flown to. Prints out top 3 of that list (KEF not included)"""
        destination_dict = self.__LLAPI.getPopularDestination()
        destination_list = self.__LLAPI.getAllDestinations()
        print("Top 3 most popular destinations: ")
        print()
        top3_list = sorted(destination_dict, key=destination_dict.get, reverse=True)[:3]
        for i in range(len(top3_list)):
            ident = top3_list[i]
            for destination in destination_list:
                if destination.get_ident() == ident:
                    airport = destination.get_airport()
            print("\t{}. {}, {} - Flown to {} times".format(i + 1,airport ,ident, destination_dict[top3_list[i]]))
            print()
    
    def showMostWorkingCrew(self):
        """Gets a dict of all employees and how many times it has flown. Prints out top 5 of that list."""
        crew_dict = self.__LLAPI.getMostWorkingCrew()
        crew_list = self.__LLAPI.getAllCrew()
        print("Top 5 most working employees: ")
        print()
        top5_list = sorted(crew_dict, key=crew_dict.get, reverse=True)[:5]
        for i in range(len(top5_list)):
            ssn = top5_list[i]
            for crew in crew_list:
                if crew.get_ssn() == ssn:
                    name = crew.get_name()
            print("\t{}. {}, {} - Flown {} times".format(i + 1, name, ssn, crew_dict[top5_list[i]]))
            print()
