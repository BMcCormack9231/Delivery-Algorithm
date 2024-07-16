import random


def load_all_packages(truck1, truck2, truck3, package_table):

    # Needs an address update at 10:20
    truck1.load_package(package_table.get_package(9))

    truck2.load_package(package_table.get_package(3))
    truck2.load_package(package_table.get_package(18))
    truck2.load_package(package_table.get_package(36))
    truck2.load_package(package_table.get_package(38))

    # These packages must go on the same truck
    truck2.load_package(package_table.get_package(13))
    truck2.load_package(package_table.get_package(14))
    truck2.load_package(package_table.get_package(15))
    truck2.load_package(package_table.get_package(16))
    truck2.load_package(package_table.get_package(19))
    truck2.load_package(package_table.get_package(20))

    # Truck 3 departs after 9:05 am because of late arrival packages
    truck3.load_package(package_table.get_package(6))
    truck3.load_package(package_table.get_package(25))
    truck3.load_package(package_table.get_package(28))
    truck3.load_package(package_table.get_package(32))
    truck3.load_package(package_table.get_package(1))

    for i in range(1, package_table.size + 1):
        package = package_table.get_package(i)
        if package.is_loaded is False:
            if truck1.package_count < 16:
                truck1.load_package(package)
            elif truck2.package_count < 16:
                truck2.load_package(package)
            else:
                truck3.load_package(package)

