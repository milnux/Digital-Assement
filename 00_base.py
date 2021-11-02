# Imports go here...

# Functions go here ...

def instructions():
    # Display instructions
    print(statement_generator("How To Play", "*"))
    return ""


def difficulty(question, low, high):
    error = "Please enter an whole number between 1 and 10\n"

    valid = False
    while not valid:
        try:
            # ask the question
            confidence = int(input(question))

            # if the amount is too low/too high, give an error message
            if low < confidence <= high:
                return confidence
            else:
                print(error)
            # if the user types in different data value, display error message
        except ValueError:
            print(error)


def statement_generator(statement, decoration):
    sides = decoration * 3

    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""


# Main routine goes here...
