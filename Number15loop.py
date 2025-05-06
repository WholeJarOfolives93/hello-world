# Define a list of 15 numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# loop through list of numbers and determine which numbers are even or odd

for number in numbers:
    if number % 2 == 0: # Even number check

       print(f"{number} is even.") # Print if even
    else:  # Otherwise, it's odd

        print(f"{number} is odd.") #Print if odd
