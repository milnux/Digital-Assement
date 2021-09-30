
end_game = ""

# Main routine goes here
while end_game != "xxx":
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
