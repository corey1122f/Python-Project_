import random

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
    while player_spawn == "Escape Pod":
        player_spawn = random.choice(list(locations))
    alien_spawn = random.choice(list(locations))
    while player_spawn == alien_spawn:
        alien_spawn = random.choice(list(locations))

    return player_spawn, alien_spawn
def view_room_items(locations, current_location, player_inventory):
    if  "item" in locations[current_location]:
        item = locations[current_location]["item"]
        print(f"Available Item: {item}") 
        while True:
            pickup = input(f"Pick up {item} (y/n)?: ") 
            pickup = pickup.lower()
            if pickup == "y":
                player_inventory.append(item)
                del locations[current_location]["item"]
                print(f"{item} added to inventory.\n")
                break
            elif pickup == "n":
                print(f"{item} not picked up.\n")
                break
            else:
                print("Invalid choice.")
                continue
    else:
        print("This room is empty!")
def move_player(locations, current_location, move_count, player_inventory):
    available_moves = locations[current_location]
    new_dict = {}
    for k,v in available_moves.items():
        if k != "item":
            new_dict[k] = v
    print(f"You are currently in {current_location}")
    print(f"Availble moves: ")
    for k , v in new_dict.items():
        print(f"Direction {k}: {v}")
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
                 print("You need the keycard to enter the escape pod!")
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
        if move_counter < 2:
            print("Alien is close")
            alien_location = random.choice(list(locations))
            while alien_location == current_location:
                alien_location = random.choice(list(locations))
            break
        elif "stun gun" in player_inventory:
            print("The alien is here!")
            use_stun_gun = input("Use stun gun?(y/n): ").lower()
            if use_stun_gun == "y":
                print("Alien stunned!")
                move_counter = 0
                continue
            elif use_stun_gun == "n":
                print("The Alien has killed you!")
                return alien_location, move_counter, True
            else:
                print("Invalid input, your mistake has killed you!")
                return alien_location, move_counter, True
        else:
            print("The alien has killed you!")
            return alien_location, move_counter, True
        
    return alien_location, move_counter, False
def view_inventory(player_inventory, oxygen_level):
    if len(player_inventory) != 0:
        print("Player items: ")
        for i in player_inventory:
            print(f"\n {i} \n")
        if "oxygen tank" in player_inventory:
            while True:
                use_oxygen = input(f"Use oxygen tank? (y/n): ")
                use_oxygen = use_oxygen.lower()
                if use_oxygen == "y":
                    oxygen_level += 30
                    print("30 seconds of Oxygen added!")
                    print(f"New oxygen level: {oxygen_level} seconds")
                    player_inventory.remove("oxygen tank")
                    break
                elif use_oxygen == "n":
                    print(f"Oxygen not used. Remaining oxygen level {oxygen_level} seconds")
                    break
        
        
    return oxygen_level
def view_oxygen(oxygen_level):
    print(f"Oxygen remaining {oxygen_level} seconds. ")
def escape(current_location, player_inventory):
    if current_location == "Escape Pod":
        if "fuel cell" in player_inventory:
            use_fuel_cell = input("Use fuel cell?").lower()
            if use_fuel_cell == "y":
                print("Congratulations you have Escaped Station Orion!!")
                return True
    return False
                



def game_over():
    pass


            



