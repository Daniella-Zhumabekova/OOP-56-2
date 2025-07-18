class Vehicle:
    def __init__(self, model, speed, fuel):
        self.model = model
        self.speed = speed
        self.fuel = fuel
    def description(self):
        return f"Модель: {self.model}, Скорость: {self.speed}, Топливо: {self.fuel}"

car = Vehicle("Toyota Camry", 200, 'бензин')
bike = Vehicle("Yamaha R3", 150, 'Бензин')

print(car.description())
print(bike.description())