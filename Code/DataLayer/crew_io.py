from Models.crew import Crew

class CrewIO:
    def __init__(self):
        self.__crew_filename = "csvFiles/Crew.csv"

    def modifyCrewToFile(self, crew_list):
        '''re-write list to the file with the changed crew-member'''
        file_stream = open(self.__crew_filename, "w", encoding="utf-8")
        for crew in crew_list:
            file_stream.write(crew.add_to_file())
        file_stream.close()
        return "Updated destination!"

    def storeCrewToFile(self, crew):
        ''' appending crew member to file'''
        file_stream = open(self.__crew_filename, "a", encoding="utf-8")
        file_stream.write(crew.add_to_file())
        file_stream.close()

    def loadAllCrewsFromFile(self):
        '''reading all crew members from file''' 
        file_stream = open(self.__crew_filename, "r", encoding = "utf-8")
        crew_list = list()
        for line in file_stream:
            ssn, name, role, rank, licence, address, phonenumber = line.strip().split(",")
            crew = Crew(ssn, name, role, rank, licence, address, phonenumber)
            crew_list.append(crew) 
        return crew_list