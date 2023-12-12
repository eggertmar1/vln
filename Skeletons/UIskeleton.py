from LLskeleton import LLAPI 
from Models import Flight
import Models
class CreateUI:
    def __init__(self):
        self.__LLAPI = LLAPI()
    def createAircraft(): #B-Krafa
        pass
    def createCrewMember(): #A-Krafa (skiptist í flugmenn og flugþjóna)
        SSN, name, role, rank, licence, address, phonenumber
        ssn = input("Input Social security number: ")
        name = input("Input Name: ")
        role = input("Input Role: ")
        rank = input("Input Rank: ")
        licence = input("Input Licence: ")
        address = input("Input Address: ")
        phonenumber = input("Phone number: ")

        new_crew = Models.Crew(ssn, name, role, rank, licence, address, phonenumber)
        crew = self.__LLAPI.createCrewMember(new_crew)

    def createDestination(self): #A-Krafa
        ident = input("Input ident: ").upper()
        airport = input("Input arrival airport: ")
        flight_time = input("Input flight time (hh:mm:ss): ")
        distance_from_iceland = input("Input distance from Reykjavík (km): ")
        emergency_contact = input("Input emergency contact: ")
        emergency_contact_number = input("Input emergancy contact number: ")
        new_destination = Models.Destination(ident, airport, flight_time, distance_from_iceland, emergency_contact, emergency_contact_number)
        
        destination = self.__LLAPI.createDestination(new_destination)
        print(destination)

    def createFlight(self): #A-Krafa
        destination = input("Input destination: ").upper()
        aircraft = input("Input aircraft ID: ").upper()
        time = input("Input time in the format: HH:MM  ")
        day = input("Input day in the format Year:Month:Day: ")
        ### day and time 
        day_and_time = '0'
        new_flight = Models.Flight('', '', destination, day_and_time, aircraft,'' ,'','','','','')

        flight = self.__LLAPI.createFlight(new_flight)
        print(new_flight)
        

    def createVoyage(): #A-Krafa
        pass



class GetUI():
    def __init__(self):
        self.__LLAPI = LLAPI()

    def showPilots(self):
        pilot_list = self.__LLAPI.getAllPilots()
        for pilot in pilot_list:
           print(pilot)
        return pilot_list
    
    def showPilotsByAircraftType(self): #B-Krafa (Búin)
        pilot_by_aircrafttype_dict = self.__LLAPI.getAllPilotsByAircraftType()
        
        for aircraft_type in pilot_by_aircrafttype_dict.keys():
            print("{}:".format(aircraft_type))
            for pilot in pilot_by_aircrafttype_dict[aircraft_type]:
                print("\t{}".format(pilot))
    
    def showPilotsByInputAircraftType(self): #B-Krafa (Villuskoða Input)!
        pilot_by_aircrafttype_dict = self.__LLAPI.getAllPilotsByAircraftType()
        aircraft_list, aircraft_type_list = self.__LLAPI.getAllAircrafts()
        aircraft_type = input("Input aircraft type: ")
        if self.__LLAPI.is_valid_aircraft_type(aircraft_type, aircraft_list):
            for pilot in pilot_by_aircrafttype_dict[aircraft_type]:
                print("\t{}".format(pilot))
        else:
            print("Aircraft type not found!")

    def showAllStaff(self):
        crew_list = self.__LLAPI.getAllCrew()
        for crew in crew_list:
            print(crew)
        return crew_list
        
    def showFlightAttendants(self):
        fl_attendant_list = self.__LLAPI.getAllFlightAttendants()
        for flight_attendant in fl_attendant_list:
            print(flight_attendant)
        return fl_attendant_list
    
    def showCrewByName(self):
        ssn = input("Input SSN: ")
        name = self.__LLAPI.getCrewByName(ssn)
        print(name)
        return name

    def showAllDestinations(self):
        destination_list = self.__LLAPI.getAllDestinations()
        for destination in destination_list:
            print(destination)
        return destination_list

    def showDestination(self):
        one_destination_list = self.__LLAPI.getDestination()
        print(one_destination_list)
        return one_destination_list
    
    def showAllVoyages(self):
        voyages_list = self.__LLAPI.getAllVoyages()
        #print(voyages_list)
        return voyages_list



    def showAllAircrafts(self):
        aircraft_list = self.__LLAPI.getAllAircrafts()
        print(aircraft_list)
        return aircraft_list

    def showAllVoyage(): #A-Krafa
        pass
    def showVoyage(voyageId): #A-Krafa
        pass
    def showAvailableCrew(Crew): #A-Krafa
        pass
    def showUnavailableCrew(Crew): #A-Krafa
        pass
    def showOccupiedAircrafts(): #B-krafa
        pass


class UpdateUI:
    def __init__():
        pass
    def updateFlight(Flight):
        pass
    def updateVoyage(Voyage):
        pass
    def updateFlight(Flight):
        pass
    def updateAircraft(Aircraft):
        pass
    def updateCrew(Crew): 
        pass
    def updateDestination(Destination):
        pass

uI1 = CreateUI()
uI = GetUI()
#uI.showAllStaff()

uI.showPilotsByAircraftType()

#uI.showPilots()

#uI.showFlightAttendants()

uI.showCrewByName()

#uI.showAllDestinations()

#uI.showDestination()
#uI1.createFlight()
#uI.showAllAircrafts()