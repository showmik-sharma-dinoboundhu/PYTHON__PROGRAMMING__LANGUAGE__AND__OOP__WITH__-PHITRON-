from abc import ABC, abstractmethod
from datetime import datetime


class Ride_Sharing:
    def __init__(self, company_name) -> None:
        self.company_name = company_name
        self.riders = []
        self.drivers = []
        self.rides = []

    def add_rider(self, rider):
        self.riders.append(rider)

    def add_driver(self, driver):
        self.drivers.append(driver)

    def __repr__(self) -> str:
        print(f"{self.company_name} with riders : {len(self.riders)} and drivers : {len(self.drivers)}")
        return f"{self.company_name} with riders : {len(self.riders)} and drivers : {len(self.drivers)}"


class User(ABC):
    def __init__(self, name, email, NID) -> None:
        self.name = name
        self.email = email

        # TODO : set user id dynamically
        self.__id = 0
        self.__NID = NID
        self.wallet = 0

    @abstractmethod
    def display_profile(self):
        raise NotImplementedError


class Rider(User):
    def __init__(self, name, email, NID, current_location, intial_amount) -> None:
        self.current_ride = None
        self.wallet = intial_amount
        self.current_location = current_location
        super().__init__(name, email, NID)

    def display_profile(self):
        print(f"Rider with Name : {self.name} and Email : {self.email}")

    def load_cash(self,amount):
        if amount > 0:
            self.wallet += amount

    def update_location(self,current_location):
        self.current_location = current_location

    def Request_Ride(self, ride_sharing, destination):
        if not self.current_ride:
            print("Looking for a ride")
            ride_request = Ride_Request(self, destination)
            ride_matcher = Ride_matichig(ride_sharing.drivers)
            ride = ride_matcher.find_driver(ride_request)
            print("Got the ride, Yay!!", ride)
            self.current_ride = ride


    def show_current_ride(self):
        print(self.current_ride)


class Driver(User):
    def __init__(self, name, email, NID, Current_location) -> None:
        self.current_location = Current_location
        self.wallet = 0
        super().__init__(name, email, NID)

    def display_profile(self):
        print(f"Driver with name : {self.name} and email : {self.email}")

    def accept_ride(self,ride):
        ride.set_driver(self)


class Ride:
    def __init__(self, start_location, end_location) -> None:
        self.start_Location = start_location
        self.end_location = end_location
        self.driver = None
        self.rider = None
        self.start_time = None
        self.end_time = None
        self.estimated_fare = None

    def setDriver(self, driver):
        self.driver = driver

    def set_driver(self, driver):
        self.setDriver(driver)

    def StartRide(self):
        self.start_time = datetime.now()

    def start_ride(self):
        self.start_time = datetime.now()

    def end_ride(self, rider, amount):
        self.end_time = datetime.now()
        self.rider.wallet -= self.estimated_fare    # type: ignore
        self.driver.wallet += self.estimated_fare   # type: ignore

    def __repr__(self) -> str:
        return f"Ride details. Started: {self.start_Location} to {self.end_location}"

class Ride_Request:
    def __init__(self, rider, end_location) -> None:
        self.rider = rider
        self.end_location = end_location


class Ride_matichig:
    def __init__(self, drivers) -> None:
        self.available_drivers = drivers

    def find_driver(self, ride_request):
        if len(self.available_drivers) > 0:
            #TODO : find the closest driver of the rider
            print("Looking for a driver")
            driver = self.available_drivers[0]
            ride = Ride(ride_request.rider.current_location, ride_request.end_location)
            driver.accept_ride(ride)
            return ride
        
class vehicle(ABC):

    speed = {
        'car' : 50,
        'bike' : 60,
        'cng' : 40
    }

    def __init__(self, vehicle_type, license_plate, rate) -> None:
        self.vehicle_type = vehicle_type
        self.license_plate = license_plate
        self.rate = rate
        self.status = 'available'

    @abstractmethod
    def start_drive(self):
        pass


class Car(vehicle):
    def __init__(self, vehicle_type, license_plate, rate) -> None:
        super().__init__(vehicle_type, license_plate, rate)
    
    def start_drive(self):
        self.status = 'unavailable'

class Bike(vehicle):
    def __init__(self, vehicle_type, license_plate, rate) -> None:
        super().__init__(vehicle_type, license_plate, rate)

    def start_drive(self):
        self.status = 'unavailable'


#Check the Class Integration:

niye_jao = Ride_Sharing("Niye Jao")
sakib = Rider('Sakib Khan', 'sakib@khan.com', 1254, 'mohakhali', 1200)
niye_jao.add_rider(sakib)
kala_pakhi = Driver("Kala Pakhi", "kala@sada.com", 5648, 'Gulshan 1')
niye_jao.add_driver(kala_pakhi)
print(niye_jao)
sakib.Request_Ride(niye_jao,"uttara")
sakib.show_current_ride()