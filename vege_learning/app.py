from classes import *
from exceptions import *
from random import randint

class Application:
    def __init__(self):
        self.menu_lis = ["1", "2", "3", "4", "5", "6"]
        self.vege_lis = [Tomato(), Watermellon(), Spinach(), Papper(), Pumpkin(), Carrot()]

    # Returns options including a correct property
    def get_option(self, idx, t_or_w):
        options = []
        if t_or_w == "t":
            for i in range(3):
                options.append(self.vege_lis[idx-i].best_temp)
        else:
            for i in range(3):
                options.append(self.vege_lis[idx-i].water)
        for i in range(2):
            options.append(options.pop(randint(0, 2-i)))
        return options

    # Returns user input on par with any in options
    def get_input(self):
        inpt = input(": ")
        while True:
            if inpt and inpt in ["1", "2", "3"]:
                return int(inpt)
            else:
                inpt = input("Enter again : ")
                continue

    def run_app(self):
        # Provides menu
        print("\n- Learn about vegetables -")
        print("[1]Tomato\n[2]Watermellon\n[3]Spinach\n[4]Papper\n[5]Pumpkin\n[6]Carrot\n[e]Crash by exception\n[Enter]Exit")
        idx = input("Choose one from above : ").lower()

        if idx in self.menu_lis:
            vege = self.vege_lis[int(idx)-1]
            t_lis = self.get_option(int(idx), "t")
            w_lis = self.get_option(int(idx), "w")

            # First question
            print(f"\nAbout【{vege}】 ...")
            print("What temperature(deg) does it grow best?")
            print(f"(1){t_lis[0]} (2){t_lis[1]} (3){t_lis[2]}")
            idx = self.get_input()
            print(handle_temp_error(vege, t_lis[idx-1]))

            # Second question
            print("\nWhat is the percentage of water in its body?")
            print(f"(1){w_lis[0]}% (2){w_lis[1]}% (3){w_lis[2]}%")
            idx = self.get_input()
            print(handle_water_error(vege, w_lis[idx-1]))

            # Shows correct information
            print(f"\n【{vege}】\nSuitable Temperature : {vege.best_temp} degrees\nWater Percentage : {vege.water}%")

        elif idx == "e":
            raise Error()

        elif idx == "":
            # Leaves instance information and kills the program
            print("\nInformation of each instance ----------------------")
            vege = Vegetable()
            vege.show_info()
            for sub in self.vege_lis:
                print()
                sub.show_info()
            print("Good Bye!")
            exit()

        # Calls the method itself
        self.run_app()

if __name__ == "__main__":
    app = Application()
    app.run_app()