from aocd import get_data

# Rock  defeats Scissors
# Scissors defeats Paper
# Paper defeats Rock

# A Rock (1)
# B Paper (2)
# C Scissors (3)

# X Rock (1)
# Y Paper (2)
# Z Scissors (3)

scoring_combinations_part1 = {
    "A X": 4,  # rock vs rock
    "A Y": 8,  # rock vs paper
    "A Z": 3,  # rock vs scissors
    "B X": 1,  # paper vs rock
    "B Y": 5,  # paper vs paper
    "B Z": 9,  # paper vs scissors
    "C X": 7,  # scissors vs rock
    "C Y": 2,  # scissors vs paper
    "C Z": 6   # scissors vs scissors
}

input_data = get_data(day=2, year=2022)


def get_score(choice: str):
    return scoring_combinations_part1[choice]


score = 0

for data in input_data.split("\n"):
    score += get_score(data)

print(score)
