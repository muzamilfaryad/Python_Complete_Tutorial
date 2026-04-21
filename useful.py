import random

feet_in_miles = 5280
meters_in_kilometer = 1000
beatles = ["John", "Paul", "George", "Ringo"]

def get_file_extension(filename):
    return filename[filename.index(".") + 1:]

def roll_dice(num_sides):
    return random.randint(1, num_sides)