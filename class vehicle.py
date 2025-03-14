class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand 
        self.model = model  

    def display_info(self):
        print(f"Vehicle Brand: {self.brand}")
        print(f"Vehicle Model: {self.model}")

class Car(Vehicle):
    def __init__(self, brand, model, car_type):
        super().__init__(brand, model)  
        self.car_type = car_type  

    def display_car_info(self):
        self.display_info()  
        print(f"Car Type: {self.car_type}")
vehicle = Vehicle("Toyota", "supra")
vehicle.display_info()

print("\n--- Car Information ---")
car = Car("Honda", "Civic", "Sedan")
car.display_car_info()
