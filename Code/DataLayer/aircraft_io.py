from Models.aircraft import Aircraft
from Models.aircraft_type import AircraftType

class AircraftIO:
    def __init__(self):
        self.__aircraft_filename = "csvFiles/Aircraft.csv" 
        self.__aircraft_type_filename = "csvFiles/AircraftType.csv"

    def storeAircraftToFile(self, aircraft): 
        '''appending new aircraft to the file, if the aircraft-type is already in the file'''
        file_stream = open(self.__aircraft_filename, "a", encoding="utf-8")
        file_stream.write(aircraft.add_to_file())
        file_stream.close()

    def storeAircraftTypeToFile(self, aircraft_type):
        '''if the aircraft is not in the file, then it appends the new aircraft-type here'''
        file_stream = open(self.__aircraft_type_filename, "a", encoding="utf-8")
        file_stream.write(aircraft_type.add_to_file())
        file_stream.close()

    def loadAllAircraftsFromFile(self):
        '''reading all aircrafts from file, finding insignia and type-id'''
        file_stream = open(self.__aircraft_filename, "r", encoding = "utf-8")
        aircraft_list = list()
        for line in file_stream:
            plane_insignia, plane_type_id = line.strip().split(",")
            aircraft = Aircraft(plane_insignia, plane_type_id)
            aircraft_list.append(aircraft)
        file_stream.close()

        file_stream = open(self.__aircraft_type_filename, "r", encoding = "utf-8")
        aircraft_type_list = list()
        for line in file_stream:
            plane_type_id, manufacturer, model, capacity, empty_weight, max_take_off_weight, unit_thrust, service_ceiling, length, height, wingspan = line.split(",")
            aircraft_type = AircraftType(plane_type_id, manufacturer, model, capacity, empty_weight, max_take_off_weight,
                                         unit_thrust, service_ceiling, length, height, wingspan)
            aircraft_type_list.append(aircraft_type)
        file_stream.close()
        return (aircraft_list, aircraft_type_list)       