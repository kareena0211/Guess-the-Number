import random

top_of_range = input("Type a Number ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please Enter the Number larger than 0 : ")
        quit()
else:
    print("Please type a Number Next time")
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Enter Number for guess :- ")
    print()
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time :- ")
        print()
        continue
    if user_guess == random_number:
        print("yeah! you Got it 🥳 ")
        print()
        break
    elif user_guess > random_number:
        print("you are above the number  ")
        print()
    else:
        print("You are below the number  ")
        print()

print("You got it in", guesses, "guesses 😊 ")
