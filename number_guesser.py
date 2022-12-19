import random

#random.randrange(start, stop)   -------> from start to stop-1
#random.randrange(stop)  ------> from 0 to stop-1

#random.randint(start, stop)   -------> from start to stop

top_of_range = input("Type a number: ")

if top_of_range.isdigit():     #if .isdigit() returns true --> next line is executed
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("please type a number larger than zero next time")
        quit()

else:
    print("please type a number next time")
    quit()

random_number = random.randint(0,top_of_range)
#print(random_number)
guesses = 0
while True:
    guesses += 1
    user_guess = int(input("Make a guess: "))
     

    if user_guess == random_number:
        print("Yayy !! You got this right \n")
        break

    elif user_guess > random_number:
        print("You were above the number ")

    else:
        print("You were below the number ")
        

print("You got it in ", guesses, " guesses")   
    