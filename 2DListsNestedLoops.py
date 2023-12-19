numberGrid = [
    
    [1, 2, 3], # Row 0
    [4, 5, 6], # Row 1
    [7, 8, 9], # Row 2
    [0]        # Row 3
    ]

print(numberGrid[0][0]) # Row 0, Column 0
print (numberGrid[2][1]) # Row 2, Column 1

for row in numberGrid:
    for col in row:
        print(col)