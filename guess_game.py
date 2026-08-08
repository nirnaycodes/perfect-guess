import random

# a = random.randint(1,101)
# print("WELOME TO GUESS GAME")
# input("Press Enter to start ")

def guess():
    # a = random.randint(1,101)
    a = random.randint(1,101)
    print("WELOME TO GUESS GAME")
    input("Press Enter to start ")
    
    
    def main():
        b = int(input("Guess your number between (1-100): "))

        if (a == b):
            print(f'''This is a perfect guess.
            computer's number was {a}''')
            c = input("Press Enter to play again or type EXIT to exit: ")
            if (c == ""):
                guess()
            
            
            else:
                exit()
        

        elif (a>b):
            print("Your number is smaller than computer's number.")
            main()

        elif (a<b):
            print("Your number is greater than computer's number.")
            main()

        else:
            return

    main()

guess()