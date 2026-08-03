from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name, email, NID) -> None:
        self.name = name
        self.email = email

        #TODO : set user Id dynamically
        self.id = 0
        self.NID = NID
        self.wallet = 0

    @abstractmethod
    def display_profile(self):
        raise NotImplementedError


class Rider(User):
    def __init__(self, name, email, NID) -> None:
        self.current_ride = None
        self.wallet = 0
        super().__init__(name, email, NID)

    def display_profile(self):
        print(f"A Rider that name is : {self.name} and email is : {self.email}")

    def load_cash(self,amount):
        if amount > 0:
            self.wallet += amount

    def request_ride(self, location, destination):
       if not self.current_ride:
           #TODO : set the ride properly
           #TODO : set the current ride via the match
            ride_request = None
            self.current_ride = None

class Driver(User):
    def __init__(self, name, email, NID, current_location) -> None:
        self.current_location = current_location
        self.wallet = 0
        super().__init__(name, email, NID)

    def display_profile(self):
        print(f"A Driver with name : {self.name} and email : {self.email}")

    def accept_ride(self,ride):
        ride.set_driver(self)
    