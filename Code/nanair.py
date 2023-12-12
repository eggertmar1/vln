from PresentationLayer.get_ui import GetUI
from PresentationLayer.create_ui import CreateUI
from PresentationLayer.update_ui import UpdateUI
import datetime

LENGHT = 50
CALCULATION_OF_BORDER = 3


def print_screen(text, options):
    """Prints out the "window" screen"""
    print("#"*LENGHT)
    print("# {}".format(text) +  " "*(LENGHT - len(text) - CALCULATION_OF_BORDER) + "#")
    print("#"*LENGHT)
    for i in range(len(options)):
        print("#" + " "*(LENGHT - 2) + "#")
        print("# {}".format(options[i]) +  " "*(LENGHT - len(options[i]) - CALCULATION_OF_BORDER) + "#")
    print("#" + " "*(LENGHT - 2) + "#")
    print("#"*LENGHT)

def actions_after():
    print("b: Back")
    action = input("").lower()
    while action != "b":
        print("Invalid action!")
        action = input("").lower()            
    return

def main_menu():
    """prints out the main menu then the user can input what he wants to do."""    
    text = "Main menu"
    options = ["1. Create", "2. Get information", "3. Update", "q: Quit"]
    action = ""
    while action != "q":
        #Prints out the window
        print_screen(text, options)
        action = input("").lower()
        if action == "1":
            create_submenu()
        elif action == "2":
            get_submenu()
        elif action == "3":
            update_submenu()
    return

def create_submenu():
    text = "Create"
    options = ["1. Create employee", "2. Create destination", "3: Create voyage", "4. Create aircraft", "b: Back"]
    action = ""
    while action != "b":
        #Prints out the window
        print_screen(text, options)
        action = input("").lower()
        if action == "1":
            create_employee()
        elif action == "2":
            create_destination()
        elif action == "3":
            create_flight()
        elif action == "4":
            create_airplane()
    return

def create_employee():
    text = "Create Employee"
    print("#"*LENGHT)
    print("# {}".format(text) +  " "*(LENGHT - len(text) - CALCULATION_OF_BORDER) + "#")
    print("#"*LENGHT)
    result = create_ui.createCrewMember() 
    actions_after()
    return

def create_destination():
    text = "Create destination"
    print("#"*LENGHT)
    print("# {}".format(text) +  " "*(LENGHT - len(text) - CALCULATION_OF_BORDER) + "#")
    print("#"*LENGHT)
    result = create_ui.createDestination()
    actions_after()
    return

def create_flight():
    text = "Create voyage"
    print("#"*LENGHT)
    print("# {}".format(text) +  " "*(LENGHT - len(text) - CALCULATION_OF_BORDER) + "#")
    print("#"*LENGHT)
    result = create_ui.createFlight()
    actions_after()
    return

def create_airplane():
    text = "Create Aircraft"
    print("#"*LENGHT)
    print("# {}".format(text) +  " "*(LENGHT - len(text) - CALCULATION_OF_BORDER) + "#")
    print("#"*LENGHT)
    result = create_ui.createAircraft()
    actions_after()
    return



def get_submenu():
    text = "Get information"
    options = ["1. Show employee", "2. Show voyages", "3. Show destinations", "4. Show aircrafts", "5: Get employee status", "b: Back"]
    action = ""
    while action != "b":
        #Prints out the window
        print_screen(text, options)
        action = input("").lower()
        if action == "1":
            show_employee_submenu()
        elif action == "2":
            show_voyages_submenu()
        elif action == "3":
            show_destination_submenu()
        elif action == "4":
            show_aircrafts_submenu()
        elif action == "5":
            show_employee_status_submenu()
    return

def show_employee_submenu():
    text = "Show employee"
    options = ["1. Show all", "2. Show pilots","3. Show pilots by aircraft type", "4. Show flight attendants", "5. Show by SSN", "6. Show employees paycheck", "7. Top 5 most working employees", "b: Back"]
    action = ""
    while action != "b":
        #Prints out the window
        print_screen(text, options)
        action = input("").lower()
        if action == "1":
            show_all_crew()
        elif action == "2":
            show_pilots()
        elif action == "3":
            show_pilots_by_aircraft_type_submenu()
        elif action == "4":
            show_flight_attendants()
        elif action == "5":
            show_crew_by_name()
        elif action == "6":
            result = get_ui.showPaycheck()
            while result == "Invalid input!":
                action = input("Try again (y/n)? ").lower()
                if action == "n":
                    break
                result = get_ui.showPaycheck()
            actions_after()
            continue
        elif action == "7":
            get_ui.showMostWorkingCrew()
            actions_after()
            continue
    return

def show_pilots():
    text = "Show pilots"
    #Prints out the window
    print("#"*LENGHT)
    print("# {}".format(text) +  " "*(LENGHT - len(text) - CALCULATION_OF_BORDER) + "#")
    print("#"*LENGHT)
    
    #Prints out all Pilots
    get_ui.showPilots()
    actions_after()
    return

def show_pilots_by_aircraft_type_submenu():
    text = "Show pilots by aircraft type"
    options = ["1. Show pilots by all aircraft types", "2. Show pilots by input aircraft type", "b: Back"]
    action = ""
    while action != "b":
        #Prints out the window
        print_screen(text, options)
        action = input("").lower()
        if action == "1":
            get_ui.showPilotsByAircraftType()
            actions_after()
            continue
        elif action == "2":
            result = get_ui.showPilotsByInputAircraftType()
            while result == "Aircraft type not found!":
                action = input("Try again (y/n)? ").lower()
                if action == "n":
                    break
                result = get_ui.showPilotsByInputAircraftType()
            actions_after()
            continue
    return

def show_flight_attendants():
    text = "Show flight attendants"
    #Prints out the window
    print("#"*LENGHT)
    print("# {}".format(text) +  " "*(LENGHT - len(text) - CALCULATION_OF_BORDER) + "#")
    print("#"*LENGHT)
    
    #Prints out all Pilots
    get_ui.showFlightAttendants()
    actions_after()
    return

def show_all_crew():
    text = "Show all employees"
    #Prints out the window
    print("#"*LENGHT)
    print("# {}".format(text) +  " "*(LENGHT - len(text) - CALCULATION_OF_BORDER) + "#")
    print("#"*LENGHT)
    
    #Prints out all staff
    get_ui.showAllStaff()
    actions_after()
    return

def show_crew_by_name():
    text = "Show by name"
    #Prints out the window
    print("#"*LENGHT)
    print("# {}".format(text) +  " "*(LENGHT - len(text) - CALCULATION_OF_BORDER) + "#")
    print("#"*LENGHT)
    
    #Prints out all staff
    result = get_ui.showCrewByName()
    while result == "Invalid SSN":
        action = input("Try again (y/n)? ").lower()
        if action == "n":
            break
        result = get_ui.showCrewByName()
    actions_after()
    return

def show_voyages_submenu():
    text = "Show employee"
    options = ["1. Show all voyages","2. Show voyages today", "3. Show all by day", "4. Show all by week", "b: Back"]
    action = ""
    while action != "b":
        #Prints out the window
        print_screen(text, options)
        action = input("").lower()
        if action == "1":
            get_ui.showAllVoyages()
            actions_after()
            continue
        elif action == "2":
            get_ui.showVoyageToday()
            actions_after()
            continue
        elif action == "3":
            result = get_ui.showVoyagesByDay()
            while result == "Invalid date!":
                action = input("Try again (y/n)? ").lower()
                if action == "n":
                    break
                result = get_ui.showVoyagesByDay()
            actions_after()
            continue  
        elif action == "4":
            result = get_ui.showVoyagesByWeek()
            while result == "Invalid date!":
                action = input("Try again (y/n)? ").lower()
                if action == "n":
                    break
                result = get_ui.showVoyagesByWeek()
            actions_after()
            continue
    return

def show_destination_submenu():
    text = "Show employee"
    options = ["1. Show all destinatons", "2. Show destination by ident", "3. Top 3 most popular destinations", "b: Back"]
    action = ""
    while action != "b":
        #Prints out the window
        print_screen(text, options)
        action = input("").lower()
        if action == "1":
            get_ui.showAllDestinations()
            actions_after()
            continue  
        elif action == "2":
            result = get_ui.showDestination()
            while result == "Invalid Ident!":
                action = input("Try again (y/n)? ").lower()
                if action == "n":
                    break
                result = get_ui.showDestination()
            actions_after()
            continue
        if action == "3":
            get_ui.showPopularDestination()
            actions_after()
            continue  
    return

def show_aircrafts_submenu():
    text = "Show aircrafts"
    options = ["1. Show all aircrafts", "2. Show aircrafts status", "b: Back"]
    action = ""
    while action != "b":
        #Prints out the window
        print_screen(text, options)
        action = input("").lower()
        if action == "1":
            get_ui.showAllAircrafts()
            actions_after()
            continue  
        elif action == "2":
            result = get_ui.showOccupiedAircrafts()
            while result == "Invalid date!":
                action = input("Try again (y/n)? ").lower()
                if action == "n":
                    break
                result = get_ui.showOccupiedAircrafts()
            actions_after()
            continue  
    return

def show_employee_status_submenu():
    text = "Show employee status"
    options = ["1. Show all unavailable employees", "2. Show all available employees", "b: Back"]
    action = ""
    while action != "b":
        #Prints out the window
        print_screen(text, options)
        action = input("").lower()
        if action == "1":
            result = get_ui.showUnavailableCrew()
            while result == "Invalid date!":
                action = input("Try again (y/n)? ").lower()
                if action == "n":
                    break
                result = get_ui.showUnavailableCrew()
            actions_after()
            continue  
        elif action == "2":
            result = get_ui.showAvailableCrew()
            while result == "Invalid date!":
                action = input("Try again (y/n)? ").lower()
                if action == "n":
                    break
                result = get_ui.showAvailableCrew()
            actions_after()
            continue  
    return

def update_submenu():
    text = "Update"
    options = ["1. Update employee", "2. Manage Crew", "3. Update destination", "b: Back"]
    action = ""
    while action != "b":
        #Prints out the window
        print_screen(text, options)
        action = input("").lower()
        if action == "1":
            update_employee()
        elif action == "2":
            manage_crew()
        elif action == "3":
            update_destination_submenu()
    return

def update_employee():
    text = "Update employee"
    print("#"*LENGHT)
    print("# {}".format(text) +  " "*(LENGHT - len(text) - CALCULATION_OF_BORDER) + "#")
    print("#"*LENGHT)
    result = update_ui.updateCrew()
    while result == "Invalid input!":
        action = input("Try again (y/n)? ").lower()
        if action == "n":
            break
        result = update_ui.updateCrew()
    actions_after()
    return


def manage_crew():
    text = "Manage crew"
    print("#"*LENGHT)
    print("# {}".format(text) +  " "*(LENGHT - len(text) - CALCULATION_OF_BORDER) + "#")
    print("#"*LENGHT)
    result = update_ui.manageCrew()
    while result == "Invalid input!":
        action = input("Try again (y/n)? ").lower()
        if action == "n":
            break
        result = update_ui.manageCrew()
    actions_after()
    return

def update_destination_submenu():
    text = "Update destination"
    print("#"*LENGHT)
    print("# {}".format(text) +  " "*(LENGHT - len(text) - CALCULATION_OF_BORDER) + "#")
    print("#"*LENGHT)
    result = update_ui.updateDestination()
    while result == "Invalid input!":
        action = input("Try again (y/n)? ").lower()
        if action == "n":
            break
        result = update_ui.updateDestination()
    actions_after()
    return

#Calls main menu here
get_ui = GetUI()
create_ui = CreateUI()
update_ui = UpdateUI()
main_menu()