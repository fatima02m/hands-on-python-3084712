NAMES = ["John", "Paul", "George", "Ringo"]
AGES = [20, 21, 22, 23]

i = 0
while i < len(NAMES):
    print(NAMES[i], AGES[i])
    i += 1

#for each thing ('name') in NAMES, print the 'name'
for name in NAMES:
    print(name)

for name, age in zip(NAMES, AGES):
    print(f"{name} {age}")

for name in reversed(NAMES):
    print(name)

#won't take up space in memory
for i in range(5):
    print(i)

# enumerate -> tells which iteration you are on
#prints the index and then the name
for i, name in enumerate(NAMES):
    print(f"{i} {name}")
