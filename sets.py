#dictionaries tuples and sets
#order of union

neptune = {86, 84, 2, 1, 2, 96, 17, 52, 20, 6, 26, 1, 3, 8}

venus = {2, 3, 8, 592, 6462, 91, 86}

print(neptune)

print(neptune|venus)
print(venus|neptune)

print(neptune & venus)
print(venus - neptune)
print(venus ^ neptune)