lists = [1,2, 25, 75, 89, 100, 4766, 1, 3, 4, 5, 0, -1, -17, 4766]

for indexOut, x in enumerate(lists):
    for indexIn, y in enumerate(lists):
        if (x == y) and (indexOut != indexIn) and indexIn > indexOut:
            print(f'IndexOut {indexOut} IndexIn{indexIn} Value {x}')
            break