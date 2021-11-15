# Generic class
class Vegetable(object):
    def __init__(self, species="Vegetable", temp=None, water=None):
         self.species = species
         self.best_temp = temp
         self.water = water

    def __str__(self):
        return self.species

    # Print information of class inheritance and instance attributes
    def show_info(self):
        name = self.__class__
        mro = name.mro()
        print(f"▼ {mro[1].__name__} > {mro[0].__name__}")
        print(f"Species : {self.species}")
        print(f"Best Temperature(deg) : {self.best_temp}")
        print(f"Water(%) : {self.water}")

# Sub class 1
class Tomato(Vegetable):
    def __init__(self):
        super().__init__("Tomato", "20~25", 94)

# Sub class2
class Watermellon(Vegetable):
    def __init__(self):
        super().__init__("Watermellon", "25~30", 90)

# Sub class 3
class Spinach(Vegetable):
    def __init__(self):
        super().__init__("Spinach", "10~15", 92)

# Sub class 4
class Papper(Vegetable):
    def __init__(self):
        super().__init__("Papper", "25~30", 93)

# Sub class 5
class Carrot(Vegetable):
    def __init__(self):
        super().__init__("Carrot", "16~20", 89)

# Sub class 6
class Pumpkin(Vegetable):
    def __init__(self):
        super().__init__("Pumpkin", "17~23", 76)