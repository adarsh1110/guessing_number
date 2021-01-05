winning_num=5
print("\t \t ***WELCOME TO GUESSING NUMBER GAME***")
print("your have 5 life to guessing right number ")
guess_num=1

while(guess_num<=5):
    choice = int(input("Guest your number between '1 to 10':- "))
    if choice>10:
        print("Please enter number between \"1 to 10\" only")
    else:
        if choice<winning_num:
            print("your choice is too low, plz enter higher number")
        elif choice>winning_num:
            print("your choice is too high, plz enter lower number")
        else:
            print("Congratulation...you are WINNER")
            print("your take", guess_num, "guesses")
            break
        print(5-guess_num, "life left")
        guess_num=guess_num+1
if(guess_num>5):
    print("GAME OVER...")