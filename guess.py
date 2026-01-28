def get_guess():
    guess=input("Enter your guess: ")
    return guess

def main():
    guess=get_guess()
    if guess == "fifty":
        print("You guessed it right!")
    else:
        print("Incorrect, try again.")

main()
