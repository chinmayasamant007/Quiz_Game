print("Welcome to my Computer Game")





playing = input("Do you want to play (y/n)? \n:")
if playing.lower() != "yes":
    quit()
print("Okay let's play:")
score = 0
answer = input("what does CPU stands for? \n:")
if answer.lower()=="central processing unit":
    print("Congratulations you got a correct answer")
    score += 1
else:
    print("incorrect!")

answer = input("what does GPU stands for? \n:")
if answer.lower()=="graphic processing unit":
    print("Congratulations you got a correct answer")
    score += 1
else:
    print("incorrect!")

answer = input("what does RAM stands for? \n:")
if answer.lower()=="random access memory":
    print("Congratulations you got a correct answer")
    score += 1
else:
    print("incorrect!")

answer = input("what does PSU stands for? \n:")
if answer.lower()=="power supply":
    print("Congratulations you got a correct answer")
    score += 1
else:
    print("incorrect!")
print("you got " + str(score)+ " out of 4")
