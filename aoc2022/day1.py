from aocd import get_data, submit

calorie_data = get_data(day=1, year=2022)
calorie_data = calorie_data.split("\n\n")

calories = []

for data in calorie_data:
    calories.append(sum([int(x) for x in data.split()]))

print(max(calories))

# to submit data
# submit(max(calories), part="a", day=1, year=2022)
