from datetime import timedelta


class Truck:
    def __init__(self, h, m, s, id):
        self.truck_packages = []
        self.priority_packages = []
        self.current_address = "HUB"
        self.miles_driven = 0.0
        self.package_count = 0
        self.timer = timedelta(hours=int(h), minutes=int(m), seconds=int(s))
        self.driver = False
        self.truck_id = id

    def __str__(self):
        packages_string = '\n '.join(str(pkg) for pkg in self.truck_packages)
        return (f"truck_packages: [{packages_string}], \ncurrent address: {self.current_address},"
                f"\ntruck timer: {self.timer}")

    # O(1) time complexity
    def load_package(self, package):
        self.truck_packages.append(package)
        self.package_count += 1
        package.is_loaded = True
        package.truck_id = self.truck_id
        if package.delivery_deadline != '':
            self.priority_packages.append(package)

    # O(n) time complexity
    def deliver_nearest_package(self, distance_table, package_list):
        # Gets the package object and distance value by calling nearest_package on the Distance object
        nearest_package, distance = distance_table.nearest_package(self.current_address, package_list)
        travel_time = timedelta(hours=distance / 18)
        # Increments truck timer
        self.timer += travel_time
        self.miles_driven += distance
        # Updates package delivery status and delivery time
        nearest_package.is_delivered = True
        nearest_package.delivery_time = self.timer
        self.current_address = nearest_package.address
        # Alerts if delivery deadline was missed
        if nearest_package.delivery_time > nearest_package.delivery_deadline:
            print(f"----Package id: {nearest_package.id} was delivered after the designated deadline.----")

    # Uses nearest neighbor (greedy) algorithm by calling deliver_nearest_package() on each package in truck_packages
    # O(n^2) time complexity
    def deliver_all_packages(self, distance_table):
        self.driver = True
        for package in self.truck_packages:  # Sets time_left_hub for each package
            package.time_left_hub = self.timer
        for _ in range(len(self.priority_packages)):        # Deliver all priority packages first
            self.deliver_nearest_package(distance_table, self.priority_packages)
        for _ in range(len(self.truck_packages) - len(self.priority_packages)):     # Deliver remaining loaded packages
            self.deliver_nearest_package(distance_table, self.truck_packages)

    # O(1) time complexity
    def return_to_hub(self, distance_data):
        distance = distance_data.distance_between(self.current_address, 'HUB')
        self.current_address = 'HUB'
        travel_time = timedelta(hours=distance / 18)
        self.timer += travel_time
        self.miles_driven += distance
        self.driver = False  # Driver is removed from truck

    # O(1) time complexity
    def get_timer(self):
        return self.timer

    # O(1) time complexity
    def set_timer(self, timer):
        if isinstance(timer, timedelta):
            self.timer = timer
        else:
            raise ValueError("Error when calling set_timer(): timer must be a timedelta object")

    # O(n) time complexity
    def get_status(self, time_delta):
        print(f"{self.truck_id}\n"
              f"Package count: {self.package_count}\n"
              f"Loaded packages:")
        for package in self.truck_packages:
            print(package.get_status(time_delta))

