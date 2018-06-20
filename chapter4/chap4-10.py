# Slices

cubes = [n**3 for n in range(1, 11)]

print("The first 3 items in the list are: ")
print(cubes[:3])

print("Three items from the middle of the list are ")
print(cubes[len(cubes)//3: 2*len(cubes)//3])

print("The last three items from the list are ")
print(cubes[-3:])