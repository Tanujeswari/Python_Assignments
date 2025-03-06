class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def car_info(self):
        print(f"This is a {self.brand} {self.model}.")
