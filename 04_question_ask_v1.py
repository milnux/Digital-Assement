def ask(question, answer):
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

