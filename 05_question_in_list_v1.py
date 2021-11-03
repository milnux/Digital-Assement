question_list = [["What is 8 x 4", 32], ["What is 5 x 2", 10]]

# Main routine
for question in question_list:
    print(question[0])
    answer = int(input("answer"))
    if answer == question[1]:
        print("Correct")
    else:
        print("Incorrect")
