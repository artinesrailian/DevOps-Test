# This function prompts for a number from the user and prints the square of the number to the output
def square():
    # Checks if the user input is integer or not, if it's a string then will show the Error message and prompt again for the number.
    while True:
        try:
            user_num = int(input("Please insert a number: "))
        except:
            print ('Error: Your input was not an integer number!')
            continue
        else:
            square = user_num ** 2
            break

    print(f"The square of {user_num} = {square}")
