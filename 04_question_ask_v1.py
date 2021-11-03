def quest_ask(question, answer):
    error = "Enter a number"
    valid = False
    while not valid:
        try:
            response = int(input(question))
            if response == answer:
                print("Correct")
                return response
            else:
                print("Incorrect")
                return response
        except ValueError:
            print(error)

# Main routine...

quest_ask("what is 2 x 4", 8)

