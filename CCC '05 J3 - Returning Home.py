instruction = ""

reverse = []

while instruction != "SCHOOL":
    instruction = input()
    if instruction == "R":
        reverse.append("LEFT")
    elif instruction  == "L":
        reverse.append("RIGHT")
    else:
        reverse.append(instruction)

for i in range(-2, -len(reverse), -2):
    print("Turn", reverse[i], "onto", reverse[i-1], "street.")

print("Turn", reverse[0], "into your HOME.")



