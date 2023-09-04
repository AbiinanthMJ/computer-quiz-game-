print("welcome to a computer ques  game ")
playing = input("do you want to play? type yes or no  ")
score = 0
if playing.lower() != 'yes':
    quit()
else:
    print("okie lets play a small game :)")

# taking answer from the user and checking if it is correct or not

answer = input("whats does cpu stands for? ")
if answer.lower() == "central processing unit":
    print('correct')
    score += 1
    print("your score is ", score)
else:
    print("incorrect")
answer2 = input("what does gpu stands for? ")
if answer2.lower() == 'graphics processing unit':
    print('correct')
    score += 1
    print("your score is", score)
else:
    print("incorrect")

answer3 = input("what does ram stands for? ")
if answer3.lower() == 'random access memory':
    print('correct')
    score += 1
    print("your score is", score)
else:
    print("incorrect")

answer4 = input("what does rom stands for? ")
if answer4.lower() == 'read only memory':
    print('correct')
    score += 1
    print(" your score is ", score)
else:
    print("incorrect")

answer5 = input("what does sd card stands for? ")
if answer5.lower() == 'secure digital':
    print('correct')
    score += 1
    print("your score is ", score)
else:
    print("incorrect")
print("you did "+str(score)+" answers correctly!")
print("thank you for playing this game")