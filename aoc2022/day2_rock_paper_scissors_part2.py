from aocd import get_data

# Rock  defeats Scissors
# Scissors defeats Paper
# Paper defeats Rock

# A Rock (1)
# B Paper (2)
# C Scissors (3)

# X Loose
# Y Draw
# Z Win

scoring_combinations_part2 = {
    "A X": 3,  # rock vs scissors
    "A Y": 4,  # rock vs rock
    "A Z": 8,  # rock vs paper
    "B X": 1,  # paper vs rock
    "B Y": 5,  # paper vs paper
    "B Z": 9,  # paper vs scissors
    "C X": 2,  # scissors vs paper
    "C Y": 6,  # scissors vs scissors
    "C Z": 7   # scissors vs rock
}

input_data = get_data(day=2, year=2022)


def get_score(choice: str):
    return scoring_combinations_part2[choice]


score = 0

for data in input_data.split("\n"):
    score += get_score(data)

print(score)

