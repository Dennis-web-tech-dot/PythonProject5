class Smartphone:
    def _init_(self, brand, model, battery):
        self.brand = brand
        self.model = model
        self.__battery = battery

    def charge(self, amount):
        self._battery = min(100, self._battery + amount)
        print(f"{self.model} charged to {self.__battery}%")

    def get_battery(self):
        return self.__battery



class GamingPhone(Smartphone):
    def _init_(self, brand, model, battery, cooling_system):
        super()._init_(brand, model, battery)
        self.cooling_system = cooling_system

    def play_game(self, game):
        if self.get_battery() > 20:
            print(f"Playing {game} on {self.model} with {self.cooling_system} cooling!")
        else:
            print(f"Battery too low to play {game}!")





class Vehicle:
    def move(self):
        pass


class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")



vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()