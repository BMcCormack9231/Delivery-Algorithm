import time
from datetime import timedelta

import Load
import Ui
from Classes.Distance import Distance
from Classes.HashTable import HashTable
from Classes.Truck import Truck


# Brandon McCormack
# Student ID: 010851191

# This program runs at worst O(n^2) time complexity when calling deliver_all_packages()

# Reads Package file and populates HashTable with Package objects
package_table = HashTable()
package_table.read_package_data()   # O(n) time complexity

# Reads the Distance file and populates the 'distance_data' table and 'address_data' list
distance_table = Distance()
distance_table.read_distance_data()  # O(n) time complexity
distance_table.read_address_data()  # O(n) time complexity

# Creates 3 Truck objects with their timers set to 8:00 am
truck1 = Truck(8, 0, 0, 'Truck 1')
truck2 = Truck(8, 0, 0, 'Truck 2')
truck3 = Truck(9, 5, 0, 'Truck 3')

print("Welcome to WGUPS delivery management program v1!")

# All trucks are loaded
Load.load_all_packages(truck1, truck2, truck3, package_table)   # O(n) time complexity
time.sleep(1)       # Creates a delay to simulate work being done

# Truck 2 departs first at 8:00 am
print('Truck 2 is departing Hub.')
truck2.deliver_all_packages(distance_table)     # O(n) time complexity
time.sleep(1)

# Truck 3 departs after late arrival packages at 9:05 am
print('Truck 3 is departing Hub.')
truck3.deliver_all_packages(distance_table)
time.sleep(1)

# Truck 2 returns to hub
print("Truck 3 is returning to Hub.")
truck3.return_to_hub(distance_table)
time.sleep(1)

# Truck 1 returns to hub
print("Truck 2 is returning to Hub.")
truck2.return_to_hub(distance_table)
time.sleep(1)

# The time is at least 10:20 so package id 9 can have its address updated
print('Package ID 9 has had an address correction.')
package9 = package_table.get_package(9)  # O(1) time complexity for searching of HashTable
# package9.address = '410 S State St'
# package9.zip = '84111'
# The update_address() call will store the old address and the time of update for use in the query process
package9.update_address(timedelta(hours=10, minutes=20), '410 S State St', '84111')
print(package9.updated_address)
time.sleep(1)

# Truck 1 gets a transfer of driver and timer from Truck 3
truck1.timer = truck3.timer
print('Truck 1 departing hub')
truck1.deliver_all_packages(distance_table)     # O(n) time complexity
time.sleep(1)

# Truck 1 returns to hub
print("Truck 1 is returning to Hub.\n")
truck1.return_to_hub(distance_table)
time.sleep(1)

print('All trucks have completed their deliveries and returned to the Hub')
total_miles = truck1.miles_driven + truck2.miles_driven + truck3.miles_driven
print('Total miles driven by all trucks: ', total_miles)

Ui.prompt_user(package_table, truck1, truck2, truck3)
