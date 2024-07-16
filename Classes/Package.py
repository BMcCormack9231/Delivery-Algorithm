from datetime import timedelta
from enum import Enum


# class DeliveryStatus(Enum):
#     WAREHOUSE = 'Warehouse'
#     LOADED = 'Loaded'
#     ENROUTE = 'Enroute'
#     DELIVERED = 'Delivered'


class Package:
    def __init__(self, id, address, city, state, zip, delivery_deadline, weight, special_notes):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.delivery_deadline = delivery_deadline
        self.weight = weight
        self.special_notes = special_notes
        self.delivery_time = None
        self.is_loaded = False
        self.is_delivered = False
        self.time_left_hub = None
        self.truck_id = None
        self.updated_address = {
            "is_updated": False,
            "time_updated": None,
            "old_address": None,
            "old_zip": None
        }

    def __str__(self):  # String method to allow for printing of Package object
        return (f"{self.id}, {self.address}, {self.city}, {self.state}, {self.zip}, {self.delivery_deadline}, "
                f"{self.weight}, {self.special_notes}, {self.delivery_time}, {self.truck_id}")

    # O(1) time complexity.
    def get_status(self, time):
        address = self.address
        zip = self.zip

        # If the address has been updated
        if self.updated_address["is_updated"] == True:
            # Check if the query is before the updated time
            if time < self.updated_address["time_updated"]:
                address = self.updated_address["old_address"]
                zip = self.updated_address["old_address"]

        # If package has left hub but has not been delivered
        if self.time_left_hub < time < self.delivery_time:
            status = "En route"
        # If package has been delivered
        elif self.delivery_time < time:
            status = f"Delivered at {self.delivery_time}"
        # If package has not yet left hub
        else:
            status = "Warehouse"

        return (f"{self.id} | {self.truck_id} | {address} | {self.city} | {self.state} | {zip} | "
                f"{self.delivery_deadline} | {self.weight} lb(s) | {status}")

    def update_address(self, time, new_address, new_zip):
        self.updated_address["is_updated"] = True
        self.updated_address["time_updated"] = time
        # Stores old address so it can be rendered when during query
        self.updated_address["old_address"] = self.address
        # Updates package object address
        self.address = new_address
        self.updated_address["old_zip"] = self.zip
        self.zip = new_zip


