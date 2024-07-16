from datetime import datetime, timedelta
from Classes.Package import Package


def prompt_user(package_table, truck1, truck2, truck3):
    while True:
        print("\nSelect a command to query the delivery operation:")
        print("1 - Check the status of a package at any time")
        print("2 - Check the status of all packages at any time")
        print("3 - Check the status of all trucks at any time")
        print("4 - Exit")
        prompt = input(">")
        try:
            if int(prompt) == 1:
                single_package_status(package_table)
            elif int(prompt) == 2:
                all_package_status(package_table)
            elif int(prompt) == 3:
                truck_status(truck1, truck2, truck3)
            elif int(prompt) == 4:
                break
        except ValueError:
            print("Invalid input")
    return False


def truck_status(truck1, truck2, truck3):
    print("Enter a time (HH:MM) to check the status of all trucks at any time (or 'back' to return to main menu):")
    time_input = input(">")
    while True:
        if time_input == 'back':
            return False
        try:
            time_format = "%H:%M"
            time_object = datetime.strptime(time_input, time_format)
            time_delta = timedelta(hours=time_object.hour, minutes=time_object.minute)
            if time_delta < timedelta(hours=8):
                print("Error: The operation does not start until 08:00")
                return False
            else:
                truck1.get_status(time_delta)
                truck2.get_status(time_delta)
                truck3.get_status(time_delta)
                return True
        except ValueError:
            print("Error: invalid input")
            return False


def all_package_status(package_table):
    print("Enter a time (HH:MM) (or 'back to return to main menu):")
    time_input = input(">")
    if time_input == 'back':
        return False
    try:
        time_format = "%H:%M"
        time_object = datetime.strptime(time_input, time_format)
        time_delta = timedelta(hours=time_object.hour, minutes=time_object.minute)
        if time_delta < timedelta(hours=8):
            print("Error: The operation does not start until 08:00")
        else:
            for i in range(1, package_table.size + 1):
                package = package_table.get_package(i)
                print(Package.get_status(package, time_delta))
    except ValueError:
        print("Error: invalid input")


def single_package_status(package_table):
    while True:
        print("Enter a package ID 1 - 40 (or 'back' to return to main menu):")
        id_input = input(">")
        if id_input == 'back':
            return False
        if 1 <= int(id_input) <= 40:
            print("Enter a time (HH:MM) (or 'back' to return to main menu):")
            time_input = input(">")
            if id_input == 'back':
                return True
            try:
                time_format = "%H:%M"
                time_object = datetime.strptime(time_input, time_format)
                time_delta = timedelta(hours=time_object.hour, minutes=time_object.minute)
                if time_delta < timedelta(hours=8):
                    print("Error: The operation does not start until 08:00")
                else:
                    package = package_table.get_package(int(id_input))
                    print(Package.get_status(package, time_delta))
            except ValueError:
                print("Error: invalid input")
        else:
            continue

