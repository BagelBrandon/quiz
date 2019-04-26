
name = input("What's your name?")

strikes = 0
score = 0

def intro():
    print("It's QuizTime! Today's quiz is about the NBA.")


def end():

    if playing == False:
        print("You lose")
    else:
        print ("You win")


def question():    
    print("What team did Kobe Bryant play for during his career?")
    guess = input()

    if guess == "Lakers":
        return score + 1 
    else:
        return strikes + 1

def questiontwo():
    print("What number did Michael Jordan wear?")
    guess2 = input()
        
    if guess2 == "23":
        return strikes + 0
    else:
        return score + 1


#def play_again():
    #while True:
        #decision = input("Wanna play again, " + name + "(y/n)")

        #if decision == 'y' or decision == 'yes':
            #return True
        #elif decision == 'n' or decision == 'no':
            #return False
        #else:
            #print("I don't understand. Enter 'y' or 'n' please.")

def play():
    
    if strikes > 0:
        playing = False
    else:
        playing = True

        
    if score == 1:
        questiontwo()
    if score == 0:
        question()
    




        

intro()

playing = True

while playing:
    play()
