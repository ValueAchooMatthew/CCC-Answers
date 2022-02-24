H = int(input())

for i in range(1, H+2, 2):
    rowStart = "*" * i
    rowEnd = "*" * i
    spaces = (2 * H) - (len(rowStart) + len(rowEnd))
    spaces = " " *spaces
    print(rowStart +spaces +rowEnd) 
    

for i in range(H-2, 0, -2):
    rowStart = "*" * i
    rowEnd = "*" * i
    spaces = (2 * H) - (len(rowStart) + len(rowEnd))
    spaces = " " *spaces
    print(rowStart +spaces +rowEnd) 