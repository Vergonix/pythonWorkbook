d = {"a": 1, "b": 2, "c": 3}
d1 = {k:v for (k, v) in d.items() if v <= 1}
print(d1)
