import random
from datetime import date, datetime

OUNCES_PER_POUND = 16
DEFAULT_MOOD = "content"


def calculate_age(birthdate):
    birth_date = datetime.strptime(birthdate, "%m/%d/%Y").date()
    today = date.today()

    if birth_date > today:
        raise ValueError("Birthdate cannot be in the future.")

    months_old = (today.year - birth_date.year) * 12
    months_old += today.month - birth_date.month
    if today.day < birth_date.day:
        months_old -= 1

    years = months_old // 12
    months = months_old % 12
    if years > 0:
        return str(years) + " years and " + str(months) + " months"
    if months > 0:
        return str(months) + " months"
    return "less than 1 month"


def introduce_baby(baby_name, age, current_weight):
    funny_things = [
        "wearing socks on my ears",
        "having a staring contest with a banana",
        "practicing my tiny dance moves",
        "trying to catch my own toes",
    ]
    print("Hello! My name is", baby_name + "!")
    print("I am", age, "old.")
    print("I weigh", current_weight, "ounces.")
    print("I like", random.choice(funny_things) + "!")


def eat(current_weight, eat_count):
    current_weight += 11
    eat_count += 1
    print("Baby ate +11 oz.")
    if eat_count % 3 == 0:
        current_weight = poop(current_weight)
    return current_weight, eat_count
def drink(current_weight, drink_count):
    current_weight += 8
    drink_count += 1
    print("Baby drank +8 oz.")
    if drink_count % 3 == 0:
        current_weight = pee(current_weight)
    return current_weight, drink_count
def poop(current_weight):
    current_weight -= 5
    print("Baby pooped -5 oz.")
    return current_weight
def pee(current_weight):
    current_weight -= 4
    print("Baby peed -4 oz.")
    return current_weight
def cry():
    print("Baby is crying loudly.")
    return "sad"
def sleep():
    print("Baby is sleeping peacefully.")
    return "content"


def dance():
    print("Baby does a wobbly dance!")


def peekaboo():
    print("Peekaboo! Baby pops out and giggles!")


def giggle():
    print("Baby giggles: hee hee hee!")


def world_takeover():
    print("Baby's pretend world takeover has begun!")
    print("First, Baby declares nap time for everyone.")
    print("Then, teddy bears become the royal advisors.")
    print("The world is ruled with giggles, cuddles, and cookies!")


def display_status(baby_name, current_weight, mood, eat_count, drink_count):
    pounds = current_weight / OUNCES_PER_POUND
    print("----- Baby Status -----")
    print("Name:", baby_name)
    print("Current weight (oz):", current_weight)
    print("Current weight (lbs):", pounds)
    print("Mood:", mood)
    print("Feedings:", eat_count)
    print("Drinks:", drink_count)
    print("------------------------")
def main():
    baby_name = input("Baby's Name: ")
    while True:
        bdate = input("Birthdate (MM/DD/YYYY): ")
        try:
            age = calculate_age(bdate)
            break
        except ValueError:
            print("Please enter a real date in MM/DD/YYYY format, not in the future.")
    current_weight = int(input("Starting weight (oz): "))
    height = input("Height (inches): ")
    eat_count = 0
    drink_count = 0
    mood = DEFAULT_MOOD
    introduce_baby(baby_name, age, current_weight)
    print("Starting mood:", mood)
    while True:
        action = input(
            "Choose an action (eat, drink, sleep, cry, dance, peekaboo, "
            "giggle, take over world, status, home): "
        ).lower()
        if action == "eat":
            current_weight, eat_count = eat(current_weight, eat_count)
            mood = "happy"
        elif action == "drink":
            current_weight, drink_count = drink(current_weight, drink_count)
            mood = "content"
        elif action == "sleep":
            mood = sleep()
        elif action == "cry":
            mood = cry()
        elif action == "dance":
            dance()
            mood = "happy"
        elif action == "peekaboo":
            peekaboo()
            mood = "happy"
        elif action == "giggle":
            giggle()
            mood = "happy"
        elif action == "take over world":
            world_takeover()
            mood = "happy"
        elif action == "status":
            display_status(baby_name, current_weight, mood, eat_count, drink_count)
        elif action == "home":
            print("Leaving the care menu...")
            break
        else:
            print("Unknown action — try again.")
    print("===== FINAL BABY STATUS =====")
    display_status(baby_name, current_weight, mood, eat_count, drink_count)
    print("Height (inches):", height)
    print("===== END =====")
main()
