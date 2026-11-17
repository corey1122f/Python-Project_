import random



g_locations = {
    "Corridor": {"fore": "Escape Pod", "starboard": "Engine Bay", "aft": "Cargo Hold", "item": "keycard"}, 
   "Escape Pod": {"aft": "Corridor", "item": "stun gun"},
   "Engine Bay": {"port": "Corridor", "fore": "Lab", "item": "fuel card"},
   "Lab": {"aft": "Engine Bay", "item": "oxygen tank"},
   "Cargo Hold": {"fore": "Corridor", "item": "alien"}
}
player_inventory = []


def main_gameloop():
    player_position = random.choice(list(g_locations))
    alien_position = random.choice(list(g_locations))
    while alien_position == player_position:
        alien_position = random.choice(list(g_locations))

    print(player_position, "********Player")
    print(alien_position, "*********Alien")

    while True:
        print(f"You are currently in {player_position}")
        player_choice = input("Options: \n 1- Move player \n 2- View items in room \n 3- View player items \n 4- Quit ")
        if player_choice == "1":
            print("Available Directions:")
            for directions in g_locations[player_position]:
                if directions != "item":
                    print("-", directions)

            move_to = input("What direction would you like to move to? (b to go back): ")
            if move_to.lower() == "b":
                continue

            elif move_to not in g_locations[player_position]:
                print(f"{move_to} is not a valid option. Please try again!")
            else:
                player_position = g_locations[player_position][move_to]
                if player_position == alien_position and "stun gun" not in player_inventory:
                    print("The alien killed you, game over!")
                    break
                elif player_position == alien_position and "stun gun" in player_inventory:
                    use_stun_gun = input("Alien is here!! Would you like to use your stun gun? (y/n): ")
                    if use_stun_gun.lower() =="n":
                        print("The alien killed you, game over! ")
                        break
                    elif use_stun_gun.lower() == "y":
                        print("The alien is now stunned. Move quickly!")
                    else:
                        print("Invalid choice, you are now dead! ")
                        break
        elif player_choice == "2":
            if "item" in g_locations[player_position]:
                print(f"Item available - \n {g_locations[player_position]["item"]}")
                pickup = input("Pick up? (y/n)")
                if pickup.lower() == "y":
                    print(f"You have picked up the {g_locations[player_position]["item"]}")
                    player_inventory.append(g_locations[player_position]["item"])
                    g_locations[player_position].pop("item")
                elif pickup.lower() == "n":
                    print(f"{g_locations[player_position]["item"]} has not been picked up.")
            else:
                print("There are no items available!")
        elif player_choice == "3":
            print("Inventory items:")
            for items in player_inventory:
                print(items)


                

main_gameloop()
      
   
   
   
   


    # choice = input(f"You are currently in {player_position}. \n Options:\n 1 - Move player \n 2 - show items in room  \n 3 - quit: ")

    # if choice == "1":
    #     possible_moves = g_locations[player_position]
    #     print("Possible moves: ")
    #     for direction in possible_moves:
    #         if direction != "item":
    #             print("-", direction)



