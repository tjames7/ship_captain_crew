# attempt at creating a ship, captain, crew dice game
# there are 5 dice, must roll 6, 5, 4 in that order in 3 rolls
# once that hits, remaining rolls count as points

import random

class Dice:
    def __init__(self, sides=6):
        """
        Initialize a die with given number of sides (default is 6)
        """
        self.sides = sides
        self.current_value = None
    
    def roll(self):
        """
        Roll the die and return the random result
        """
        return random.randint(1, self.sides)
    
    def get_current_value(self):
        """
        Return the last rolled value, or None if never rolled
        """
        return self.current_value

def remove_specific_numbers(dice_roll, numbers_to_remove):
    """
    Remove ONE instance of each number in numbers_to_exclude from dice_roll
    """
    remaining = dice_roll.copy()  # Make a copy to avoid modifying the original
    
    for number in numbers_to_remove:
        if number in remaining:
            remaining.remove(number)  # This removes only the FIRST occurrence
    
    return remaining

# Example usage:
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# numbers_to_exclude = [3, 5, 8]

# new_list = remove_specific_numbers(my_list, numbers_to_exclude)
# print(f"Original list: {my_list}")
# print(f"Numbers to remove: {numbers_to_exclude}")
# print(f"Remaining numbers: {new_list}")

# Example usage:
if __name__ == "__main__":
    # Create 5 dice
    d1 = Dice()
    d2 = Dice()
    d3 = Dice()
    d4 = Dice()
    d5 = Dice()

# TJ Notes list
# I don't think my rolls while is working as intended at the moment
# Should I consider creating a running list of roll results to track whether I'm getting ship, captain, crew as the roll while loops runs?
# When I roll [1,5,5,6,4] it thinks I only have 1 for remaining points instead of 1 and 5 
# Above was fixed!
# When I roll Ship and Captain, it runs three dice roll after, but then when that doesn't hit for 4 it runs a five dice roll

rolls = 3
while rolls > 0:
    
    five_dice_roll  =  [d1.roll(), d2.roll(), d3.roll(), d4.roll(), d5.roll()]
    four_dice_roll  =  [d1.roll(), d2.roll(), d3.roll(), d4.roll()]
    three_dice_roll =  [d1.roll(), d2.roll(), d3.roll()]
    two_dice_roll   =  [d1.roll(), d2.roll()]

    #roll dice
    print(five_dice_roll)
    if 6 in five_dice_roll and 5 in five_dice_roll and 4 in five_dice_roll:
        print("You've got Ship, Captain, and Crew!")
        numbers_to_exclude = [6,5,4]
        remaining_points = remove_specific_numbers(five_dice_roll, numbers_to_exclude)
        print(remaining_points)
        choice = input(f"Your score is now {remaining_points}, would you like to stay or roll again? (stay/roll)").lower()
        choice = input("Do you want to continue? (yes/no): ").lower()
        if choice == "stay":
            print(f"Your score is {remaining_points}")
            # break
        elif choice == "roll":
            print(two_dice_roll)
            choice = input(f"Your score is now {two_dice_roll}, would you like to stay or roll again? (stay/roll)").lower()
            if choice == "stay":
                print(f"Your score is {two_dice_roll}")
            # break
            elif choice == "roll":
                print(two_dice_roll)
            print(f"Your score is now {two_dice_roll}")
        else:
            print("Please enter 'stay' or 'roll'")
    elif 6 in five_dice_roll and 5 in five_dice_roll:
        if rolls == 1:
            print("You were not able to get any points on your turn")
            break
        print("You've got Ship and Captain!")
        print(three_dice_roll)
        if 4 in three_dice_roll:
            print("You've got Ship, Captain, and Crew!") 
            numbers_to_exclude = [4]
            remaining_points = remove_specific_numbers(three_dice_roll, numbers_to_exclude)
            print(remaining_points)
            choice = input(f"Your score is now {remaining_points}, would you like to stay or roll again? (stay/roll)").lower()
            if choice == "stay":
                print(f"Your score is {remaining_points}")
                # break
            elif choice == "roll":
                print(two_dice_roll)
                print(f"Your score is now {two_dice_roll}")
        
    elif 6 in five_dice_roll:
        if rolls == 1:
            print("You were not able to get any points on your turn")
            break
        print("You've got Ship!")
        print(four_dice_roll)
        if 5 and 4 in four_dice_roll:
            print("You've got Ship, Captain, and Crew!")
            numbers_to_exclude = [5,4]
            remaining_points = remove_specific_numbers(four_dice_roll, numbers_to_exclude)
            print(remaining_points)
            choice = input(f"Your score is now {remaining_points}, would you like to stay or roll again? (stay/roll)").lower()
            if choice == "stay":
                print(f"Your score is {remaining_points}")
                # break
            elif choice == "roll":
                print(two_dice_roll)
                print(f"Your score is now {two_dice_roll}")
        if 5 in four_dice_roll:
            print("You've got Ship and Captain!")
            print(three_dice_roll)
            if 4 in three_dice_roll:
                print("You've got Ship, Captain, and Crew!")
                numbers_to_exclude = [4]
                remaining_points = remove_specific_numbers(three_dice_roll, numbers_to_exclude)
                print(remaining_points)
                print(f"Your score is {remaining_points}")
    else:
        print("Let's roll again")
    #logic

    rolls -= 1