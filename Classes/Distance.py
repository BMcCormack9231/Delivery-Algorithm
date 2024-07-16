import csv



class Distance:
    def __init__(self):
        self.distance_data = []
        self.address_data = []

    # O(n) time complexity
    def read_distance_data(self, filepath='Data/Distance-File.csv'):
        with open(filepath) as file:
            data = csv.reader(file, delimiter=',')
            for row in data:
                self.distance_data.append(row)

    # Unlike for the distance_data list (above), this uses 'extend(row)' to prevent adding lists to the list and
    # creating an unnecessary 2-d list for the addresses
    # O(n) time complexity
    def read_address_data(self, filepath='Data/Address-File.csv'):
        with open(filepath) as file:
            data = csv.reader(file, delimiter=',')
            for row in data:
                self.address_data.extend(row)

    # O(1) time complexity
    def distance_between(self, package1, package2):
        try:
            # Checks if package1 is a string
            if isinstance(package1, str):
                index1 = self.address_data.index(package1)
            else:
                index1 = self.address_data.index(package1.address)
        except ValueError:
            return f"Error: '{package1} was not found in address data"
        try:
            if isinstance(package2, str):
                index2 = self.address_data.index(package2)
            else:
                index2 = self.address_data.index(package2.address)
        except ValueError:
            return f"Error: '{package2}' was not found in address data"
        distance = self.distance_data[index2][index1]
        if distance != '':
            return float(distance)
        else:
            return float(self.distance_data[index1][index2])

    # O(n) time complexity
    def nearest_package(self, from_package, package_list):
        min_distance = float('inf')
        nearest_package = None
        for package in package_list:
            if package.is_delivered is False:
                distance = self.distance_between(from_package, package)
                if distance < min_distance:
                    min_distance = distance
                    nearest_package = package
        return nearest_package, min_distance  # Also returns min_distance
