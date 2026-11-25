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


