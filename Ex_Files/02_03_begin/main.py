
#creating lists
NAMES = ["John", "Paul", "George", "Ringo"]
AGES = [20, 21, 22, 23]

#using lists
JOHN = NAMES[0]
PAUL = NAMES[1]

#from index 0 till 2 (not including 2)
JOHN_PAUL = NAMES[:2]
#everything to the right of index 2
GEORGE_RINGO = NAMES[2:]
#Names[start:stop:counter]
REVERSE = NAMES[::-1]
EVERY_OTHER = NAMES[::2]

print(sum(AGES))
print(min(AGES))
print(max(AGES))

print(JOHN_PAUL)
print(GEORGE_RINGO)
print(REVERSE)
