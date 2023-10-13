import random
def get_user_choice():
    while True:
        user_ = input("Choose Rock, Paper, or Scissors: ").strip().lower()
        if user_ in ['rock', 'paper', 'scissors']:
            return user_
        else:
            print("Invalid choice. Please choose Rock, Paper, or Scissors.")
def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])
def determine_winner(user_, computer_):
    if user_ == computer_:
        return "It's a tie!"
    elif (user_ == 'rock' and computer_ == 'scissors') or \
         (user_ == 'scissors' and computer_ == 'paper') or \
         (user_== 'paper' and computer_ == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"
def main():
    while True:
        user_ = get_user_choice()
        computer_ = get_computer_choice()
        print(f"You chose {user_}. Computer chose {computer_}.")
        result = determine_winner(user_, computer_)
        print(result)
        play_again = input("Play again? (y/n): ").strip().lower()
        if play_again != "y":
            print("Thanks for playing!")
            break
if __name__ == "__main__":
    main()