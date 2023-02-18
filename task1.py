"""
Задание 1.
Создать класс TrafficLight (светофор)
и определить у него один приватный атрибут color (цвет) и публичный метод
running (запуск).
В рамках метода running реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный)
составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение.
Для имитации "горения" каждого цвета испольщуйте ф-цию sleep модуля time
Переключение между режимами должно осуществляться только
в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""

from time import sleep


class TrafficLight:
    __modes = (("red", 7), ("yellow", 2), ("green", 8))
    __colors_list = ["red", "yellow", "green"]
    __color: str

    def __init__(self, init_color="red"):
        self.__color = init_color

    def running(self):
        print(f"Текущий свет - {self.__color}")
        i = 0
        while i < 10:
            color_index = self.__colors_list.index(self.__color)
            t = self.__modes[color_index][1]
            sleep(t)
            self.__color = self.__colors_list[color_index + 1] if color_index < 2 else "red"
            print(f"Свет переключился на {self.__color}")
            i += 1


if __name__ == '__main__':
    tl = TrafficLight()
    tl.running()
