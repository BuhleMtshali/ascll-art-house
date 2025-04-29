#creating the house pattern

# 1. Roof height
roof_height = 5

# 2. House width (widest part of the roof, same width as the base of walls)
base_width = roof_height * 2 - 1

# 3. Wall height
wall_height = 5

# 4. Drawing the roof
for i in range(roof_height):
    spaces = roof_height - i - 1
    stars = i * 2 + 1
    print(" " * spaces + "*" * stars)

# 5. Drawing the walls
for i in range(wall_height):
    print("*" + " " * (base_width - 2) + "*")

# 6. Drawing the bottom (floor of the house)
print("*" * base_width)
