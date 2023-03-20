# functions go here

# checks users enter an integer to a given question
# Main routine goes here
tickets_sold = 0

while True:

    try:
        response = int(input(question))
        return response

    except ValueError:
        print("please enter an integer")

name = input("Enter your name / xxx to quit: ")

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






