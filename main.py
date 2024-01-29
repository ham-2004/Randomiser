import random

def dice():
    number = random.randint(1, 6)
    print("You Rolled: ", number)

def main():
    while True:
        print("1. Roll Dice")
        print("2. Exit")
        user_choice = input("What do you want to do?")

        if user_choice == "1":
            dice()
        elif user_choice == "2":
            break
        else:
            print("Invalid Choice! Please Try Again.")

if __name__ == "__main__":
    main()