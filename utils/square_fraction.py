# Checks if the square result has fraction and throws error.
def square_fraction(user_num, square_result):
    if (square_result).is_integer():
        print(f"The square of {int(user_num)} = {int(square_result)}")
    else:
        print ('Error: The outcome of your square calculation is not a whole number.')
