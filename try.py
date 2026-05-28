import random

leaderboard = {}

def play_game():
    number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = int(input("Guess a number (1-100): "))
        attempts += 1

        if guess < number:
            print("Too low")
        elif guess > number:
            print("Too high")
        else:
            print("Correct!")
            return attempts


while True:
    score = play_game()

    name = input("Enter your name: ")
    leaderboard[name] = score

    again = input("Play again? (yes/no): ").lower()

    if again != "yes":
        print("\nLeaderboard:")

        for name, score in leaderboard.items():
            print(name, ":", score)

        break
    
def save_leaderboard(leaderboard):
    with open("leaderboard.txt", "w") as file:
        for name, score in leaderboard.items():
            file.write(f"{name}: {score}\n")
            