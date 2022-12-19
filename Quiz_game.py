print("Welcome to the quiz")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()  #terminate the program

print("Okay!  Let's Play :)")
score = 0

print("\n-----First Question----")
ans = input("What does CPU stand for? ")
if ans.lower() == "central processing unit":
    print("Correct !")
    score += 1
else:
    print("Incorrect !!!")

print("\n-----Second Question----")
ans = input("What does GPU stand for? ")
if ans.lower() == "graphics processing unit":
    print("Correct !")
    score += 1
else:
    print("Incorrect !!!")


print("\n-----Third Question----")
ans = input("What does RAM stand for? ")
if ans.lower() == "random access memory":
    print("Correct !")
    score += 1
else:
    print("Incorrect !!!")

print("\n-----Fourth Question----")
ans = input("What does ROM stand for? ")
if ans.lower() == "read only memory":
    print("Correct !")
    score += 1
else:
    print("Incorrect !!!")

print("\n-----Fifth Question----")
ans = input("What does AI stand for? ")
if ans.lower() == "artificial inteligence":
    print("Correct !")
    score += 1
else:
    print("Incorrect !!!")

if score<1:
    print("\n--------> You got " + str(score) + " question correct !\n")
    print(str((score/5) * 100) +" %\n")

else:
    print("\n--------> You got " + str(score) + " questions correct !\n")
    print(str((score/5) * 100) +" %\n")