name = input("What's your name?")

score = input("What question would you like to answer, " + name + "? Pick a number from 1 to 2.")

if score == 2:
    questiontwo()
elif score == 1:
    question()


strikes = 0

def end():

    if playing == False:
        print("You lose")
    else:
        print ("You win")
        

def get_guess():
    guess = input("Enter a number, from 1-2.")
    return guess


def question(score):

    if score == 2:
        print("What team did Kobe Bryant play for during his career?")
    guess = input()

    if guess == "Lakers":
        print("You win") 
    else:
        return strikes + 1
    

def questiontwo(score):
    print("What number did Michael Jordan wear?")
    guess = input()

    if guess is "23":
        print("You win")
    else:
        print("You lose")

        


#def play_again():
    #while True:
        #decision = input("Wanna play again, " + name + "(y/n)")

        #if decision == 'y' or decision == 'yes':
            #return True
        #elif decision == 'n' or decision == 'no':
            #return False
        #else:
            #print("I don't understand. Enter 'y' or 'n' please.")

