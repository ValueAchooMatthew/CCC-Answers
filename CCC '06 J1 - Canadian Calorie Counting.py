burgers = [461, 431, 420, 0]
sides = [100, 57, 70, 0]
drinks = [130, 160, 118, 0]
desserts = [167, 266, 75, 0]

burger, side, drink, dessert = int(input()), int(input()), int(input()), int(input())

calories = burgers[burger - 1] + sides[side - 1] + drinks[drink - 1] + desserts[dessert - 1]

print("Your total Calorie count is", str(calories) +".")