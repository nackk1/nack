heroes = ["Ironman", "Thor", "Hulk", "Superman", "Spiderman"]

def display_heroes():
    print(heroes)

def add_heroes():
    global heroes
    heroes_add = input("Please input new heroes: ")
    heroes.append(heroes_add)
    print(heroes)


display_heroes()
add_heroes()