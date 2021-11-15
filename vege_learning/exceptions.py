# Generic exception
class Error(Exception):
    def __init__(self, message="An exception was raised."):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message

# Sub exception 1
class TempError(Error):
    def __init__(self, vege, temp):
        super().__init__(f"Suitable temperature of {vege} isn't {temp} degrees.")

# Sub exception 2
class WaterPercentError(Error):
    def __init__(self, vege, rate):
        super().__init__(f"{vege} isn't made up of {rate} % water.")


# Evaluate whether user input is subject to TempError
def evaluate_temp(vege, temp):
    if temp == vege.best_temp:
        return "Correct!"
    else:
        raise TempError(vege, temp)

# Evaluate whether user input is subject to WaterPercentError
def evaluate_water(vege, water):
    if water == vege.water:
        return "Correct!"
    else:
        raise WaterPercentError(vege, water)

# Handler for TempError
def handle_temp_error(vege, temp):
    try:
        return evaluate_temp(vege, temp)
    except TempError as e:
        return e.message

# Handler for WaterPercentError
def handle_water_error(vege, water):
    try:
        return evaluate_water(vege, water)
    except WaterPercentError as e:
        return e.message