# Imports go here...

# Functions go here ...

def instructions():
    # Display instructions
    print(statement_generator("How To Play", "*"))
    return ""


def difficulty():
    math_skills = int(input("How confident are you in maths on a scale of 1 to 10?"))
    # If math skills is 1, 2 or 3, display easy questions
    if math_skills >= 7 <= 10:
        print("great at maths")
    # if math skills is 4 5 or 6, display medium questions
    elif math_skills >= 4 <= 6:
        print("decent at maths")
    # if math skills is 8 9 or 10, display hard questions
    elif math_skills > 0 <= 3:
        print("not good at maths")
    else:
        print("[ERROR] Please put a whole number")

    return ""


def statement_generator(statement, decoration):
    sides = decoration * 3

    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""


# Main routine goes here...
