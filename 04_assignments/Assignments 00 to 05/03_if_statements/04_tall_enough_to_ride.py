MINIMUM_HEIGHT: int = 50  # arbitrary units :)

def tall_enough_extension():
    while True:
        user_input = input("How tall are you? ")
        if user_input == "":
            print("Exiting program. Have a great day at the park!")
            break
        try:
            height = float(user_input)
            if height >= MINIMUM_HEIGHT:
                print("You're tall enough to ride!")
            else:
                print("You're not tall enough to ride, but maybe next year!")
        except ValueError:
            print("Please enter a valid number for your height.")

# There is no need to edit code beyond this point
if __name__ == '__main__':
    tall_enough_extension()
