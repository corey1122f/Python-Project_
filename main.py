from functions import *
import time
locations = create_locations()
from ascii import *
CYAN = "\033[96m"
RESET = "\033[0m"




def main_menu():
    title()
    name = input("Enter your name: ")
    print(f"Welcome, {name}!")
    while True:
        try:
            print("Choose an option (1 2 3): \n")
            choice = int(input("1.New Game\n2.View Hall of Fame\n3.Exit\n:"))
           
        except ValueError:
            print("Invalid input")
            continue
        if choice == 1:
            locations = create_locations()
            new_game() # Calls ASCII function 
            main_gameloop(locations, name) # Calls the below main_gamloop function
            
        elif choice == 2:
            view_hall_of_fame()
        elif choice == 3:
            print("Goodbye!")
            break
        else:
            print("Invalid input.")

def main_gameloop(locations, name):
    player_spawn, alien_spawn = randomise_spawn(locations)
    current_location = player_spawn
    alien_location = alien_spawn
    
    player_inventory = []
    oxygen_level = 180
    move_counter = 0
    item_points = 0
    alien_points = 0
    oxygen_points = 0
    
    last_check = time.monotonic()
    print(f"\n \nYou have spawned in {current_location}. What would you like to do? (1 2 3 4 5)")
    while True:
        seconds_passed = int(time.monotonic() - last_check)
        oxygen_level -= seconds_passed
        last_check += seconds_passed
        

        if oxygen_level <= 0:
            game_over_art()
            print("You ran out of Oxygen!!")
            
            break
        print(f"{CYAN}Oxygen Level: {oxygen_level:.0f} seconds{RESET}")
    
        try:
            choice = int(input("1.Move player\n2.View items in room\n3.View player inventory\n4.View remaining Oxygen level\n5.Quit:"))
        except ValueError:
            print("Please enter a valid input (1,2,3,4,5)")
            continue
        # Check how much time passed while the player was choosing
        seconds_passed = int(time.monotonic() - last_check)

        oxygen_level -= seconds_passed
        last_check += seconds_passed

        if oxygen_level <= 0:
            game_over_art()
            print("You ran out of Oxygen!!")
            break
        if choice == 1:
            current_location, move_counter = move_player(locations, current_location, move_counter, player_inventory)
            alien_location, move_counter, player_died = check_alien_encounter(current_location, alien_location, move_counter, locations, player_inventory)
            if player_died == True:
                game_over_art()
                game_over()
                break
            if alien_location == None:
                alien_points = 20
            if escape(current_location, player_inventory):
                oxygen_points = oxygen_level // 10
                final_score = item_points + alien_points + oxygen_points
                winner()
                print(f"Final score: {final_score} points")
                save_score(name, final_score)
                view_hall_of_fame()

                break

        elif choice == 2:
            item_points = view_room_items(locations,current_location,player_inventory, item_points )
        elif choice == 3:
            oxygen_level = view_inventory(player_inventory, oxygen_level)
        elif choice == 4:
            view_oxygen(oxygen_level)

        elif choice == 5:
            print("Returning to main menu")
            break

main_menu()    

