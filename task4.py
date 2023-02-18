"""
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать
текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение
о превышении скорости. Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    speed: int
    color: str
    name: str
    is_police: bool

    def __init__(self, color: str, name: str, speed: int = 0, is_police: bool = False):
        self.color = color
        self.name = name
        self.is_police = is_police
        self.speed = speed

    def go(self):
        if self.speed == 0:
            self.speed = 10
        print(f"Машина {self.name} поехала")

    def stop(self):
        self.speed = 0
        print(f"Машина {self.name} остановилась")

    @staticmethod
    def turn(direction):
        if direction in ("left", "right"):
            print(f"Car's turned {direction}")

    def show_speed(self):
        print(f"Скорость: {self.speed} км/ч")


class TownCar(Car):
    speed_limit = 60

    def show_speed(self):
        if self.speed > self.speed_limit:
            print(f"Превышение скорости! Текущая скорость {self.speed} км/ч "
                  f"при максимально разрешенной скорости {self.speed_limit}")


class WorkCar(Car):
    speed_limit = 40

    def show_speed(self):
        if self.speed > self.speed_limit:
            print(f"Превышение скорости! Текущая скорость {self.speed} км/ч "
                  f"при максимально разрешенной скорости {self.speed_limit}")


class SportCar(Car):
    pass


class PoliceCar(Car):
    is_police = True


test_data = {
    ('Green', 'Skoda', 80): TownCar,
    ('Black', 'Bugatti', 110): SportCar,
    ('Blue', 'Ford Focus', 60): WorkCar,
    ('White', 'LADA', 130, True): PoliceCar,
}

for car_data, car_class in test_data.items():
    car = car_class(*car_data)

    print(f"Car name: {car.name}")
    print(f"Car color: {car.color}")
    print(f"Car is police: {car.is_police}")

    car.go()
    car.turn("right")
    car.show_speed()
    car.stop()
    print("___")
