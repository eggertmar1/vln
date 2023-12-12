from DataLayer.io_api import IoAPI
from Models.aircraft import Aircraft
from Models.aircraft_type import AircraftType
from LogicLayer.is_valid_LL import validChecker
import datetime

class AircraftLL():
    def __init__(self):
        self.__IoAPI = IoAPI()
        self.__valid = validChecker()

    def getAllAircrafts(self):
        """Gets a list of all aircrafts from Aircraft.csv and all aircraft types from AircraftType.csv and returns both lists """
        aircraft_list, aircraft_type_list = self.__IoAPI.loadAllAircraftsFromFile()
        return aircraft_list, aircraft_type_list

    def getOccupiedAircrafts(self, date):
        '''finding out what aircrafts are occupied at a certain time using datetime, also returns available aircrafts'''
        aircraft_list, aircraft_type_list = self.__IoAPI.loadAllAircraftsFromFile()
        flight_list = self.__IoAPI.loadAllFlightsFromFile()
        if self.__valid.is_valid_date(date):
            flights_on_date = list()
            available_aircrafts_set = set()
            unavailable_aircrafts_dict = dict()
            date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
            for flight in flight_list:
                if flight.get_start_time().date() == date:
                    flights_on_date.append(flight)
                elif flight.get_arrival_time().date() == date:
                    flights_on_date.append(flight)
            
            for flight in flights_on_date:
                for aircraft in aircraft_list[1:]:
                    if flight.get_aircraft_id() == aircraft.get_plane_insignia():
                        if aircraft not in unavailable_aircrafts_dict:
                            unavailable_aircrafts_dict[aircraft] = []
                            unavailable_aircrafts_dict[aircraft].append([flight.get_flight_number(), flight.get_destination(), flight.get_arrival_time()])
                        else:
                            unavailable_aircrafts_dict[aircraft].append([flight.get_flight_number(), flight.get_destination(), flight.get_arrival_time()])
            
            for aircraft in aircraft_list[1:]:
                if aircraft not in unavailable_aircrafts_dict:
                    available_aircrafts_set.add(aircraft)

            available_aircrafts_list = list()
            unavailable_aircrafts_list = list()
            for aircraft in available_aircrafts_set:
                for aircraft_type in aircraft_type_list:
                    if aircraft_type.get_plane_type_id().upper() == aircraft.get_plane_type_id().upper():
                        available_aircrafts_list.append([aircraft, aircraft_type.get_plane_capacity()])
            
            for aircraft, info in unavailable_aircrafts_dict.items():
                for aircraft_type in aircraft_type_list:
                    if aircraft_type.get_plane_type_id().upper() == aircraft.get_plane_type_id().upper():
                        unavailable_aircrafts_list.append([aircraft, aircraft_type.get_plane_capacity(), info])
            
            return unavailable_aircrafts_list, available_aircrafts_list
        
        else:
            return "Invalid date!", None

    def createAircraft(self, aircraft):
        ''' running the new aircraft through is-valid and sending it forward if it passes'''
        if self.__valid.is_valid_aircraft_insignia(aircraft):
            aircraft_list, aircraft_type_list = self.__IoAPI.loadAllAircraftsFromFile()
            if self.__valid.is_valid_aircraft_type(aircraft.get_plane_type_id().upper(), aircraft_type_list): 
                self.__IoAPI.storeAircraftToFile(aircraft)
                return "New aircraft added!"
            else:
                return None
        else: 
            return "Invalid aircraft insignia!"

    def createAircraftType(self, aircraft_type):
        '''if the aircraft type is not in the file, it takes the model information and creates a new aircraft-type, 
            sending it forward to the data layer, if it passes is-valid'''
        if self.__valid.is_valid_new_aircraft(aircraft_type):
            self.__IoAPI.storeAircraftTypeToFile(aircraft_type)
            return "New aircraft type added!"
        else:
            return "Invalid input!"  