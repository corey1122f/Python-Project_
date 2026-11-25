import random
from datetime import datetime

# ANSI ESCAPE CODES
BLUE = "\033[94m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"


def create_locations():
    g_locations = { 
 'Corridor':{'fore': 'Escape Pod', 'starboard': 'Engine Bay', 'aft': 'Cargo Hold', 
              'item': 'keycard'},

 'Escape Pod': {'aft': 'Corridor', 'item': 'stun gun'},

 'Engine Bay': {'port': 'Corridor', 'fore': 'Lab', 'item': 'fuel cell'},

 'Lab': {'aft': 'Engine Bay', 'item': 'oxygen tank'}, 

 'Cargo Hold': {'fore': 'Corridor'} #Removed alien to allow for random alien spawn
} 
    return g_locations


def randomise_spawn(locations):
    player_spawn = random.choice(list(locations))
    while player_spawn == "Escape Pod": #Stops player spawning into a locked escape pod
        player_spawn = random.choice(list(locations))
    alien_spawn = random.choice(list(locations))
    while alien_spawn == player_spawn or alien_spawn == "Escape Pod": #Prevents alien spawning in escape pod and stopping player from getting the stun gun
        alien_spawn = random.choice(list(locations))

    return player_spawn, alien_spawn


def view_room_items(locations, current_location, player_inventory, item_points):
    if  "item" in locations[current_location]:
        item = locations[current_location]["item"]
        print(f"Available Item: {item}") 
        while True:
            pickup = input(f"Pick up {item} (y/n)?: ") 
            pickup = pickup.lower()
            if pickup == "y":
                player_inventory.append(item)
                if item == "keycard":
                    item_points +=10
                elif item == "fuel cell":
                    item_points += 10
                elif item == "oxygen tank":
                    item_points += 5
                del locations[current_location]["item"]
                print(f"{GREEN}{item} added to inventory.{RESET}\n")
                break
            elif pickup == "n":
                print(f"{item} not picked up.\n")
                break
            else:
                print("Invalid choice.")
                continue
    else:
        print(f"{YELLOW}This room is empty!{RESET}")
    return item_points


def move_player(locations, current_location, move_count, player_inventory):
    available_moves = locations[current_location]
    new_dict = {}
    for k,v in available_moves.items():
        if k != "item":
            new_dict[k] = v
    print(f"\n ********************************** \nYou are currently in {current_location}") # makes lines easier to read
    print(f"Availble moves: ")
    for k , v in new_dict.items():
         print(f"Direction {BLUE}{k}{RESET}: {v}") #changes colour of available directions to blue for easier reading
    while True:
        move_to = input("Enter Direction (b to to back): ")
        move_to = move_to.lower()
        if move_to == "b":
            break
        elif move_to not in new_dict:
            print("Invalid direction")
            continue
        if new_dict[move_to] == "Escape Pod":
            if "keycard" not in player_inventory:
                 print(f"{YELLOW}You need the keycard to enter the escape pod!{RESET}")
                 continue

            use_keycard = input("Use keycard (y/n): ").lower()

            if use_keycard != "y":
                 print("You did not use the keycard!")
                 continue
            
        current_location = new_dict[move_to]
        print(f"You are now in {current_location}")
        move_count +=1
        break
    return current_location, move_count


def check_alien_encounter(current_location, alien_location, move_counter, locations, player_inventory):
    while True:
        if current_location != alien_location:
            break
        if move_counter < 2: # gives the player 2 moves before potential alien encounter
            print(f"{RED}Alien is close{RESET}")
            alien_location = random.choice(list(locations))
            while alien_location == current_location:
                alien_location = random.choice(list(locations))
            break
        elif "stun gun" in player_inventory:
            print(f"{RED}The alien is here!{RESET}")
            use_stun_gun = input(f"{BLUE}Use stun gun?(y/n):{RESET} ").lower()
            if use_stun_gun == "y":
                print(f"{GREEN}Alien stunned!{RESET}")
                player_inventory.remove("stun gun")
                alien_location = None
                break
            elif use_stun_gun == "n":
                print(f"{RED}The Alien has killed you!{RESET}")
                return alien_location, move_counter, True
            else:
                print(f"{RED}Invalid input, your mistake has killed you!{RESET}")
                return alien_location, move_counter, True
        else:
            print(f"{RED}The alien has killed you!{RESET}")
            return alien_location, move_counter, True
        
    return alien_location, move_counter, False


def view_inventory(player_inventory, oxygen_level):
    if len(player_inventory) != 0:
        print("Player items: ")
        for i in player_inventory:
            print(f"\n {i} \n")
        if "oxygen tank" in player_inventory:
            while True:
                use_oxygen = input(f"{GREEN}Use oxygen tank? (y/n):{RESET} ")
                use_oxygen = use_oxygen.lower()
                if use_oxygen == "y":
                    oxygen_level += 60
                    print(f"{GREEN}60 seconds of Oxygen added!{RESET}")
                    print(f"New oxygen level: {oxygen_level} seconds")
                    player_inventory.remove("oxygen tank")
                    break
                elif use_oxygen == "n":
                    print(f"{YELLOW}Oxygen not used. Remaining oxygen level {oxygen_level} seconds{RESET}")
                    break
        
        
    return oxygen_level


def view_oxygen(oxygen_level):
    print(f"{CYAN}Oxygen remaining: {oxygen_level} seconds.{RESET} ")


def escape(current_location, player_inventory):
    if current_location == "Escape Pod":
        if "fuel cell" in player_inventory:
            use_fuel_cell = input("Use fuel cell? (y/n): ").lower()
            if use_fuel_cell == "y":
                print("Congratulations you have Escaped Station Orion!!")
                return True
    return False


def save_score(name, final_score):
    date = datetime.now().strftime("%d/%m/%Y %H:%M")
    with open("hall_of_fame.txt", "a") as f:
        f.write(f"{name},{final_score},{date}\n")           


def view_hall_of_fame():
    scores = []
    try:
        with open("hall_of_fame.txt", "r") as f:
            for line in f:
                parts = line.strip().split(",")

                if len(parts) == 3:
                    name, score, date = parts
                    scores.append((name, int(score), date)) #Adds a tuple of name, score and date to keep the data together
    except FileNotFoundError:
        print("No scores recorded yet!")
        return # So below doesnt print
    if len(scores) == 0:
        print("No scores recorded yet!") #Doesnt print below because of return
        return

    print("\n ******************* HALL OF FAME  ******************* ")
    for name, score , date in scores:
        print(f"NAME: {name}  SCORE: {score}  DATE: {date}")


def game_over():
    pass


            



