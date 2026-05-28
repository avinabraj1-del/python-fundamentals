leaderboard = {
    "Avina": 499,
    "Dina": 620,
    "Sara": 404
}
file = open("leaderboard.txt", "w")
for name, score in leaderboard.items():
    file.write(f"{name}: {score}\n")

file.close()

print ("Leaderboard saved!")

with open("leaderboard.txt", "r") as file:
    contents = file.read()
    print(contents)
    
