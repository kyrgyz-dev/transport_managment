from interface import Transport


class Car(Transport):
    def __init__(self, name, fuel_level):
        super().__init__(name)
        self.__fuel_level = fuel_level  # private

    def move(self):
        if self.__fuel_level > 0:
            self.__fuel_level -= 10
            print(f'{self.name} едет на бензине. Осталось топливо: {self.__fuel_level}')
        else:
            print(f"{self.name} не может ехать. Топливо закончилось.")


class Bike(Transport):
    def __init__(self, name):
        super().__init__(name)
        self._tire_pressure = 100  # protect

    def move(self):
        print(f"{self.name} крутит педали. Давление в шинах: {self._tire_pressure}")


class Bus(Transport):
    def __init__(self, name, passengers):
        super().__init__(name)
        self.passengers = passengers

    def move(self):
        print(f"{self.name} перевозит {self.passengers} пассажиров.")
