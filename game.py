import random

def play_game():
    number = random.randint(1, 10)
    attempts = 0
    max_attempts = 5

    print("\n🎯 Guess the number between 1 to 10")
    print(f"You have {max_attempts} attempts")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess == number:
                print(f"🎉 Correct! You guessed in {attempts} attempts")
                return
            elif guess < number:
                print("📉 Too Low!")
            else:
                print("📈 Too High!")

        except ValueError:
            print("⚠️ Please enter a valid number")

    print(f"❌ Game Over! The number was {number}")


# 🔁 Replay feature
while True:
    play_game()
    again = input("Do you want to play again? (yes/no): ").lower()
    if again != "yes":
        print("👋 Thanks for playing!")
        break
