"""
Задание 3.
Реализовать базовый класс Worker (работник),
в котором определить публичные атрибуты name, surname, position (должность),
и защищенный атрибут income (доход). Последний атрибут должен ссылаться
на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker. В классе Position реализовать публичные методы
получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).
"""


class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')


work_test = [['Василий', 'Иванов', 'аналитик', {
    'wage': 100000,
    'bonus': 50000
}], ['Васисуалий', 'Компетентный', 'Скрам-инженер', {
    'wage': 199999,
    'bonus': 9999
}], ['Мушег', 'Бабаян', 'программист', {
    'wage': 111111,
    'bonus': 1111
}]]

for el in work_test:
    pos = Position(el[0], el[1], el[2], el[3].get('wage'), el[3].get('bonus'))
    print(f'Имя: {pos.get_full_name()} ({pos.position}), доход (оклад и премия): {pos.get_total_income()}')
