# functions go here

# checks users enter an integer
def num_check(question):
    while True:

        try:
            response = int(input(question))
            return response

        except ValueError:
            print("please enter an integer")


def not_blank(question):
    while True:
        response = input(question)

        # return the response if it's not blank
        if response != "":
            return response
        else:
            print("Sorry this can't be blank")


# checks users enter an integer to a given question
# Main routine goes here
tickets_sold = 0

while True:
    name = not_blank("Enter your name / xxx to quit: ")

    if name == "xxx":
        break

    age = int(input("Age: "))

    if 12 <= age <= 120:
        pass
    elif age < 120:
        print("sorry you are too young for this movie")
        continue
    else:
        print("?? that looks like a typo, please try again.")
        continue

    tickets_sold += 1

print(f"You sold {tickets_sold} tickets")
