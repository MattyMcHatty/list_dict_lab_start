# counter = 0
# number = 5
# while (counter < number):
#     print(f"Counter is {counter}")
#     counter = counter + 1

# print('Loop has finished')

# numbers = [1, 2, 3, 4, 5]
# total = 0

# for number in numbers:
#     total = total + number
# print(total)

chickens = [
  {"name": "Margaret", "age": 2, "eggs": 0},
  {"name": "Hetty", "age": 1, "eggs": 2},
  {"name": "Henrietta", "age": 3, "eggs": 1},
  {"name": "Hen Solo", "age": 2, "eggs": 0},
  {"name": "Cluck Norris", "age": 5, "eggs": 1},
]

total_eggs = 0

for chicken in chickens:
    total_eggs += chicken['eggs']
    chicken['eggs'] = 0

for chicken in chickens:
    if chicken['name'][0] == 'H':
        print('Woo Hoo')
