import random


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
# using random.int and format
# able to randomise the numbers used quiz
end = ""
while end != "xxx":
    number_1 = random.randint(0, 15)
    number_2 = random.randint(0, 15)
    product = number_1 * number_2

    quest_ask()
    int(input(" {} x {} = ".format(number_1, number_2,)))
