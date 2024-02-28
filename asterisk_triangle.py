height=5
triangle = ""

for i in range(1, height + 1):
    # Adding spaces before the asterisks to create the triangle shape
    triangle += " " * (height - i)
    # Adding asterisks for each row
    triangle += "*" * (2 * i - 1)
    # Moving to the next line for the next row
    triangle += "\n"
print(triangle)
 
