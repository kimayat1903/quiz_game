print("Welcome to the computer quiz!")

name = input("Type your name: ")
print("Welcome to this quiz!")

playing = input("Do you want to play? (yes/no)")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play",name)
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does WWW stand for?  ")
if answer.lower() == "world wide web":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does OS stand for? ")
if answer.lower() == "operating system":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")