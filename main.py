import time
import random


class Lift:

    def __init__(self):

        self.load_capacity = 1000
        self.amount_of_floors = 9
        self.current_floor = 1

    def open(self):
        print("Двери открываются")

    def close(self):
        print("Двери закрываются")

    def filling(self):
        amount_of_people = int(input("сколько людей едет?"))
        return amount_of_people

    def move(self, amount_of_people):

        weight = 0

        for i in range(amount_of_people):
            weight += random.randint(40, 90)

        print(f"Вес в лифте {weight} килограмм")

        if weight > self.load_capacity:
            print("Лифт не может ехать из за того что грузоподъемность привышена")


        else:
            floor = int(input("На какой этаж вы хотите поехать? 1-9"))
            while True:
                if floor < self.current_floor:

                    print(f"Вы на {self.current_floor} этаже")
                    self.current_floor -= 1
                    time.sleep(1)

                elif floor > self.current_floor:

                    print(f"Вы на {self.current_floor} этаже")
                    self.current_floor += 1
                    time.sleep(1)


                else:
                    print("Вы приехали")
                    break


lift = Lift()

while True:
    lift.open()
    amount_of_people = lift.filling()
    lift.close()
    lift.move(amount_of_people)
