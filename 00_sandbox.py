def conf_chkr(question, low, high):
    error = "Please enter an whole number between 1 and 10\n"

    valid = False
    while not valid:
        try:
            # ask the question
            confidence = int(input(question))
            # If math skills is 8 9 or 10 display hard questions
            if confidence >= 8 <= 10:
                print("great at maths")
            # if math skills is 4 5 6 or 7display medium questions
            elif confidence >= 4 <= 7:
                print("decent at maths")
            # If math skills is 1, 2 or 3, display easy questions
            elif confidence > 0 <= 3:
                print("not good at maths")
            else:
                print("[ERROR] Please put a whole number")
        except ValueError:
            print(error)
