d = dict(a = list(range(1, 11)), b = list(range(11, 21)), c = list(range(21, 31)))
for item in d.items():
    print(str(item[0]) + " has value " + str(item[1]))
