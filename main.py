from interface import Transport
from service import Car, Bike, Bus

def start_trip(transport: Transport):
    transport.move()

c = Car("Toyota", 50)
b = Bike("Stels")
bus = Bus("Mercedes Bus", 30)

start_trip(c)
start_trip(b)
start_trip(bus)