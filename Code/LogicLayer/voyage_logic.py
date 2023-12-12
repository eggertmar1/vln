from DataLayer.io_api import IoAPI
import datetime
from Models.flight import Flight
from LogicLayer.is_valid_LL import validChecker


class VoyageLL:
    def __init__(self):
        self.__IoAPI = IoAPI()
        self.__valid = validChecker()

    def getAllVoyages(self):
        '''Gets a list of all flights from the IO. Makes a new list with all the flights and its status.
        Return the new list'''
        flight_list = self.__IoAPI.loadAllFlightsFromFile()
        voyage_and_status_list = []
        
        voyage_and_status_list = self.get_manned_status_on_flights(flight_list, voyage_and_status_list)
                
        voyage_and_status_list = self.get_status_on_flights(voyage_and_status_list)
        return voyage_and_status_list
    
    def getAllVoyagesNeedManned(self):
        '''Gets a list of all flights and its status from the getAllVoyages. 
        Makes a new list with all the flights that are not fully manned and are not in the past.
        Return the new list'''
        voyages_list = self.getAllVoyages()
        voyages_need_to_be_manned = []
        today = datetime.datetime.now()
        
        for i in range(1, len(voyages_list), 2):
            flight_out = voyages_list[i-1][0]
            manned_status_flight_out = voyages_list[i-1][1]
            flight_in = voyages_list[i][0]
            manned_status_flight_in = voyages_list[i][1]

            if today <= flight_out.get_start_time():
                if manned_status_flight_out != "Fully manned":
                    voyages_need_to_be_manned.append([flight_out, manned_status_flight_out, flight_in, manned_status_flight_in])
        return voyages_need_to_be_manned
        
    def getVoyageByWeek(self, date):
        '''Gets a list of all flights from the IO. Sorts out the flights that are in the input week.
        Makes a new list with all the flights and its status.
        Return the new list'''
        voyage_and_status_list = list()
        flight_list = self.__IoAPI.loadAllFlightsFromFile()
        if self.__valid.is_valid_date(date):
            datetime_object = datetime.datetime.strptime(date, "%Y-%m-%d")
            dates = list()
            for i in range(7):
                next_day = datetime_object + datetime.timedelta(days = i)
                dates.append(next_day.date())

            flights_on_date = list()
            for flight in flight_list:
                if flight.get_start_time().date() in dates:
                    flights_on_date.append(flight)
                elif flight.get_arrival_time().date() in dates:
                    flights_on_date.append(flight)
            
            voyage_and_status_list = self.get_manned_status_on_flights(flights_on_date, voyage_and_status_list)

            voyage_and_status_list = self.get_status_on_flights(voyage_and_status_list)
            return voyage_and_status_list, dates
        else:
            return "Invalid date!", None

        
    def getVoyageByDay(self, date):
        '''Gets a list of all flights from the IO. Sorts out the flights that are in the input day.
        Makes a new list with all the flights and its status.
        Return the new list''' 
        voyage_and_status_list = list()
        flight_list = self.__IoAPI.loadAllFlightsFromFile()
        if self.__valid.is_valid_date(date):
            date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
            flights_on_date = list()
            for flight in flight_list:
                if flight.get_start_time().date() == date:
                    flights_on_date.append(flight)
                elif flight.get_arrival_time().date() == date:
                    flights_on_date.append(flight)
            
            voyage_and_status_list = self.get_manned_status_on_flights(flights_on_date, voyage_and_status_list)

            voyage_and_status_list = self.get_status_on_flights(voyage_and_status_list)
            return voyage_and_status_list, date
        else:
            return "Invalid date!", date

    def getVoyageToday(self):
        '''Gets a list of all flights from the IO. Sorts out the flights that are today.
        Makes a new list with all the flights and its status.
        Return the new list'''
        voyage_and_status_list = list()
        flight_list = self.__IoAPI.loadAllFlightsFromFile()
        today = datetime.datetime.now()

        flights_on_date = list()
        for flight in flight_list:
            if flight.get_start_time().date() == today.date():
                flights_on_date.append(flight)
            elif flight.get_arrival_time().date() == today.date():
                flights_on_date.append(flight)
        
        voyage_and_status_list = self.get_manned_status_on_flights(flights_on_date, voyage_and_status_list)
        
        voyage_and_status_list = self.get_status_on_flights(voyage_and_status_list)
        
        return voyage_and_status_list, today

    def manageCrew(self, voyage):
        flight_list = self.__IoAPI.loadAllFlightsFromFile()
        new_flight_list = list()
        flight_out = voyage[0]
        flight_in = voyage[2]
        for flight in flight_list:
            if flight.get_flight_number() == flight_out.get_flight_number():
                flight = flight_out
            if flight.get_flight_number() == flight_in.get_flight_number():
                flight = flight_in
            new_flight_list.append(flight)

        response = self.__IoAPI.modifyFlightToFile(new_flight_list)
        return response

    def get_status_on_flights(self, voyage_and_status_list):
        """Gets a list of flights and its manned status. It then appends to it the status on the flight.
        Whether it is in air, finished or not started. Returns the list and the new status"""
        today = datetime.datetime.now()
        for element in  voyage_and_status_list:
            flight = element[0]

            if flight.get_start_time() > today:
                element.append("Not started")

            elif flight.get_start_time() < today:
                if flight.get_arrival_time() > today:
                    element.append("In air")
                elif flight.get_arrival_time() < today:
                    element.append("Finished")

        return voyage_and_status_list
    
    def get_manned_status_on_flights(self, flight_list, voyage_and_status_list):
        """Gets a list of flights and appends to it the manned status.
        Fully manned if all 5 spots are manned. Minimum manned is at least the 3 important spots are manned.
        Empty if the minimum requirement is not fulfilled. Returns the list and the status"""
        for flight in  flight_list:
            manned = False
            empty = True
            fullmanned = False
            arranged_crew = flight.get_arranged_crew()
            if len(arranged_crew[0]) != 0 and len(arranged_crew[1]) != 0 and len(arranged_crew[2]) != 0:
                manned = True
                empty = False

            if manned:
                fullmanned = True
                for crew in arranged_crew:
                    if len(crew) == 0:
                        fullmanned = False

            if fullmanned:
                voyage_and_status_list.append([flight, "Fully manned"])
            elif manned:
                voyage_and_status_list.append([flight, "Minimum manned"])
            elif empty:
                voyage_and_status_list.append([flight, "Not manned"])
        return voyage_and_status_list