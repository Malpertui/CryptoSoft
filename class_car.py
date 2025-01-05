# Block №1:

class Car:
    def __init__(self, make, model, year, odometer_reading):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = odometer_reading

# Block №2:

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
# Block №3:

class Car:
    def __init__(self, make, model, year, odometer_reading = 0):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = odometer_reading