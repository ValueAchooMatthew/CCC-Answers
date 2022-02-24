text = input()

happyFaces = text.count(":-)")
sadFaces = text.count(":-(")

if happyFaces == 0 and sadFaces == 0:
    print("none")

elif happyFaces > sadFaces:
    print("happy")

elif happyFaces < sadFaces:
    print("sad")

else:
    print("unsure")
