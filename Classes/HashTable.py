import csv
from datetime import datetime, timedelta

from Classes.Package import Package


# This class will be used as a table to hold all the package objects. "PackageTable" would be a more appropriate
# name for it, but I have named it "HashTable" to associate it with my custom data structure.

class HashTable:
    def __init__(self, size=40):      # Default size is set to 40 packages
        self.packages = [None] * size   # A list of None values is created for the packages
        self.size = size

    def __hash__(self, key):
        return hash(key) % len(self.packages)

    # O(1) time complexity
    def set_package(self, package_id, package):
        index = self.__hash__(package_id)
        if self.packages[index] is None:        # Creates a list at the index of the packages list (2-d list)
            self.packages[index] = []
        self.packages[index].append(package)

    # O(n) time complexity
    def read_package_data(self, filepath='Data/Package_File.csv'):
        with open(filepath) as file:
            package_data = csv.reader(file, delimiter=',')
            for row in package_data:
                id = int(row[0])        # Casts the id to an int, so it can be hashed
                address = row[1]
                city = row[2]
                state = row[3]
                zip = row[4]
                delivery_deadline = HashTable.parse_delivery_deadline(row[5])
                weight = row[6]
                special_notes = row[7]
                package = Package(id, address, city, state, zip, delivery_deadline, weight, special_notes)
                # Sets Package status while observing packages with delays in special_notes
                # if special_notes == 'Delayed on flight---will not arrive to depot until 9:05 am':
                #     package.is_loaded = DeliveryStatus.ENROUTE
                # else:
                #     package.is_loaded = DeliveryStatus.WAREHOUSE
                package.is_loaded = False
                self.set_package(package.id, package)

    # O(1) time complexity
    @staticmethod
    def parse_delivery_deadline(time_string):
        if time_string == 'EOD':
            return timedelta(hours=23, minutes=59, seconds=59)  # Sets to final second in the day for comparison
        else:
            time_object = datetime.strptime(time_string, '%I:%M %p')
            h = time_object.hour
            m = time_object.minute
            return timedelta(hours=h, minutes=m)

    # O(n) time complexity
    def print_table(self):
        for index, bucket in enumerate(self.packages):
            if bucket is not None:
                for package in bucket:
                    print(package)

    # O(n) time complexity only in the case of a data collision
    def get_package(self, package_id):
        index = self.__hash__(package_id)
        list = self.packages[index]
        for package in list:
            if package.id == package_id:
                return package
        return None
