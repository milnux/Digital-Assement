# Main routine goes here



end_game = ""
while end_game != "xxx":
    math_skills = int(input("How confident are you in maths on a scale of 1 to 10?"))
# If math skills 10

    if math_skills <= 3:
        print("bad at maths")
    elif math_skills > 4 < 6:
        print("decent at maths")
    elif math_skills >= 7:
        print("good at maths")
    else:
        end_game = "xxx"
