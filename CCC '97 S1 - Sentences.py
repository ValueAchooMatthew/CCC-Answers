n = int(input())

for i in range(n):
    numSubjects = int(input())
    numVerbs = int(input())
    numObjects = int(input())
    
    subjects = []
    verbs = []
    objects = []
    
    for s in range(numSubjects):
        objects.append(input())
    
    for v in range(numVerbs):
        verbs.append(input())
    
    for o in range(numObjects):
        subjects.append(input())
        
    for obj in objects:
        for verb in verbs:
            for subject in subjects:
                print(obj, verb, subject +".")
