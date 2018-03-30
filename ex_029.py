from math import pi

def sphere_liquid_volume(height, r=10):
    liquid_volume = (4 * pi * r**3)/3 - (pi * height**2 * (3 * r - height))/3
    return liquid_volume

print(sphere_liquid_volume(2))
