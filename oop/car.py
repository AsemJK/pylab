class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

        print(f'My car is {self.make} {self.model} {self.year}')

corolla = Car('Toyota', 'Corolla', 2015)
