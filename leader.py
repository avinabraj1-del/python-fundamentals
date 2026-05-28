import random

# Load leaderboard from file
def load_leaderboard():
    leaderboard = {}

    try:
        with open("leaderboard.txt", "r") as file:
            for line in file:
                name, score = line.strip().split(":")
                leaderboard[name] = int(score)
    except FileNotFoundError:
        pass

    return leaderboard


# Save leaderboard to file
def save_leaderboard(leaderboard):
    with open("leaderboard.txt", "w") as file:
        for name, score in leaderboard.items():
            file.write(f"{name}:{score}\n")


leaderboard = load_leaderboard()


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

    save_leaderboard(leaderboard)

    again = input("Play again? (yes/no): ").lower()

    if again != "yes":
        print("\nLeaderboard:")

        for name, score in leaderboard.items():
            print(name, ":", score)

        break
