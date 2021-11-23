#moodle test 25 kérdés 60 perc
#laboros vizsga, jelentkezni kell, 35 fős létszámkorlát, #9-10 10-11
#javitó gyak január 5. + vizsgaidőszak legvégén
from enum import Enum

class Colors(Enum):
    r = "red"
    g = "green"
    b = "blue"
    red = "red"
    green = "green"
    blue = "blue"



class Main:
    def __init__(self):
        self.restaurants = []

    def get_restaurants(self):
        with open("restaurants.txt", "r") as file:
            restaurants_strs = [line.strip().split("*") for line in file.readlines()]
            for restaurant_str in restaurants_strs:
                self.restaurants.append(
                    Restaurant(
                        restaurant_str[0],
                        restaurant_str[1],
                        restaurant_str[2],
                        restaurant_str[3]))

    def print_restaurants_with_foods(self):
        for rest in self.restaurants:
            print(rest.name)
            for food in rest.foods:
                print("\t", food.name, food.price)

    def print_restaurants(self):
        for rest in self.restaurants:
            print(rest.name, end="\t")


    def run(self):
        self.get_restaurants()
        #self.print_restaurants_with_foods()
        self.print_restaurants()
        valasztas = input("Válassz egy éttermet:")
        for rest in self.restaurants:
            if valasztas == rest.name:
                print("Kajak:")
                for food in rest.foods:
                    print(food.name, food.price, end="\t")


class Customer:...

class Food:
    def __init__(self, name, price, osszetevok):
        self.name = name
        self.price = int(price)
        self.osszetevok = osszetevok

    def __eq__(self, other):
        if self.name == other.name:
            return True


class Restaurant:
    def __init__(self, id, name, address, type):
        self.id = int(id)
        self.name = name
        self.address = address
        self.type = type
        self.foods = []
        self.get_foods()

    def get_foods(self):
        with open("foods.txt", "r") as file:
            foods_strs = [line.strip().split("*") for line in file.readlines()]
            for food_str in foods_strs:
                if int(food_str[0]) == self.id:
                    self.foods.append(Food(food_str[1], food_str[2], food_str[3]))


class DeliveryRestaurant(Restaurant):...


if __name__ == '__main__':
    app = Main()
    app.run()




