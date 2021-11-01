def conf_chkr(question, low, high):
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
                print("[ERROR] Please put a whole number")
            # if the user types in different data value, display error message
        except ValueError:
            print(error)


skill_level = conf_chkr("How confident are you in maths?", 0, 10)

# If math skills is 8 9 or 10 display hard questions
if skill_level >= 8 <= 10:
    print("hard questions")

# if math skills is 4 5 6 or 7display medium questions
elif skill_level >= 4 <= 7:
    print("medium questions")

# If math skills is 1, 2 or 3, display easy questions
elif skill_level > 0 <= 3:
    print("easy questions")

