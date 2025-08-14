import random
player_health = 10
player_gold = 0

while True:
    print("You are in a dark room.")
    choice = input("Do you go left or right?")
    
    if choice.lower() == "quit":
        print("Thanks for playing!")
        break  # exits the loop
        print("you choose:", choice)

    events = ["treasure","nothing", "monster"]
    events = random.choice(events)

    if events == "treasure":
        print("you found some gold!")
        player_gold += 1
    elif events == "monster":
        print("A monster attacks you!")
        player_health -= 2    
    else:
        print("The room is empty.")

    print("Health", player_health, "Gold", player_gold)