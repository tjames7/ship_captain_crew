import random

def roll_dice(n):
    return [random.randint(1, 6) for _ in range(n)]

def remove_specific_numbers(dice_roll, numbers_to_remove):
    remaining = dice_roll.copy()
    for number in numbers_to_remove:
        if number in remaining:
            remaining.remove(number)
    return remaining

if __name__ == "__main__":
    rolls_remaining = 3
    ship = captain = crew = False
    score = []

    while rolls_remaining > 0:
        if not ship:
            dice = roll_dice(5)
            print(f"Rolling 5 dice: {dice}")
        elif ship and not captain:
            dice = roll_dice(4)
            print(f"Rolling 4 dice: {dice}")
        elif ship and captain and not crew:
            dice = roll_dice(3)
            print(f"Rolling 3 dice: {dice}")
        else:
            dice = roll_dice(2)
            print(f"Rolling for points: {dice}")
        
        rolls_remaining -= 1

        if not ship and 6 in dice:
            ship = True
            print("You've got the Ship!")
            dice.remove(6)
        
        if ship and not captain and 5 in dice:
            captain = True
            print("You've got the Captain!")
            dice.remove(5)
        
        if ship and captain and not crew and 4 in dice:
            crew = True
            print("You've got the Crew!")
            dice.remove(4)
            score = dice  # remaining dice count as points
        elif ship and captain and crew:
            score = dice  # update score if crew already found
        
        if ship and captain and crew:
            # Ask to reroll for more points if rolls remain
            if rolls_remaining > 0:
                print(f"Current score dice: {score}")
                choice = input(f"You have {rolls_remaining} roll(s) left. Would you like to roll remaining dice again for more points? (stay/roll): ").lower()
                if choice == "stay":
                    break
                # else: loop continues and rerolls 2 dice
            else:
                print("No rolls left!")
                break

    if ship and captain and crew:
        print(f"Final score: {sum(score)} from dice {score}")
    else:
        print("You did not get Ship, Captain, and Crew in time. No score.")
