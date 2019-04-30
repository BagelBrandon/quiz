name = input("What's your name?")

print("What question would you like to answer, " + name + "? Pick a number from 1 to 2.")
score = input()
strikes = 0


def intro():
    print("It's QuizTime! Today's question is about the NBA.")

    
def end():

    print("Thank you for playing" + name + "!")
    decision = input()
        
def question(score):
    print("What number did Michael Jordan wear?")
    guess = input()

    if guess == "23":
        print("You win")
    else:
        print("You lose")

        


def play_again():
    while True:
        decision = input("Wanna play again, " + name + "(y/n)")

        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
            return False
        else:
            print("I don't understand. Enter 'y' or 'n' please.")

def play():
    if score == "2":
        print("What number did MJ wear")
    elif score == "1":
        print("What team did Kobe Bryant play for?")




intro()
      
question(score)
play_again()
