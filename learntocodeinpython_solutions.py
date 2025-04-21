#CH4: Scope

#L1: Scope

def get_max_health(modifier, level):
    return modifier * level


my_modifier = 5
my_level = 10


max_health = get_max_health(my_modifier, my_level)


print(f"max_health is: {max_health}")


#L2: Global Scope

player_level = 4



def calculate_health(modifier):
    return player_level * modifier


def calculate_primary_stats(armor_bonus, modifier):
    return armor_bonus + modifier + player_level


print(f"Character has {calculate_health(10)} max health.")

print(f"Character has {calculate_primary_stats(3, 8)} primary stats.")



#L3: Scope Quiz

#Does the get_area_of_circle function have access to the pi variable?

#Yes, because the pi variable is in the global scope


#L4: Scope Quiz

#Can the area variable inside the get_area_of_circle function be accessed outside the function?

#No, variables defined inside a function are not accessible outside of it




#CH5: testing and debugging