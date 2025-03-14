class car:
  def __init__(self,brand,model,year):
    self.brand=brand
    self.model=model
    self.year=year

  def display_derails(self):
      print(f"car brand:{self.brand}")
      print(f"car model:{self.model}")
      print(f"car year:{self.year}")

my_car = car("toyota","legender","2024")

my_car.display_derails()
