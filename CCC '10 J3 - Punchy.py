A = 0
B = 0


while True:
    instruction = input()
    if instruction[0] == "1":
        if instruction[2] == "A":
            A = int(instruction[4:])
        else:
            B = int(instruction[4:])
    elif instruction[0] == "2":
        if instruction[2] == "A":
            print(str(A))
        else:
            print(str(B))
    elif instruction[0] == "3":
        if instruction[2] == "A":
            if instruction[-1] == "A":
                A = 2*A
            else:
                A = A + B 
        else:
            if instruction[-1] == "A":
                B = B + A
            else:
                B = 2*B 
    elif instruction[0] == "4":
        if instruction[2] == "A":
            if instruction[-1] == "A":
                A = A**2
            else:
                A = A * B 
        
        else:
            if instruction[-1] == "A":
                B = B * A
            else:
                B = B ** 2 
    elif instruction[0] == "5":
        if instruction[2] == "A":
            if instruction[-1] == "A":
                A = 0
            else:
                A = A - B 
        else:
            if instruction[-1] == "A":
                B = B - A
            else:
                B = 0 
    
    elif instruction[0] == "6":
        if instruction[2] == "A":
            if instruction[-1] == "A":
                A = 1
            else:
                A = A // B
        else:
            if instruction[-1] == "A":
                B = B // A
            else:
                B = 1
    
    else:
        break
