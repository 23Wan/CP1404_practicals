from car import *
import random
class UnreliableCar(Car):
     def __init__(self, name, fuel, reliability):
         super().__init__(name, fuel)
         self.reliability = reliability
     def drive(self, distance):
         random_number = random.randint(0, 100)
         if random_number <= self.reliability:
            distance_driven = super().drive(distance)
            return distance_driven
         else:
               distance = 0
               return "You need to raise your car's reliability"