import random

def roll_dice():
    return random.randint(1, 6)

def dice_simulator():
    while True:
        print("\nRolling the dice...")
        print(f"The dice shows: {roll_dice()}")
        
        roll_again = input("Do you want to roll again? (yes/no): ").lower()
        if roll_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    dice_simulator()
