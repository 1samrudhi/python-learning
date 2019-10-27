# print("SAMRUDHI PETKAR")
# print(" o ------")
# print(",    ||   ||")
# print("<3  " *10)

# name = "John Smith"
# age = 25
# is_new_patient = True

# name = input('What is your name? ')
# colour = input("what is your favourite color? ")
# print(name + '\'s favourite colour is ' + colour)

# wt_pound = input("What is your weight in pounds? ")
# wt_kg = 0.45 * int(wt_pound)
# print(wt_kg)

#course = "Learn python's course at CODEKUL"




# command = ""
# car_start = False
# car_stop = True
# while True:
#     command = input("> ").lower()
#     if command == "help":
#         print("""
# start - start the engine
# stop - stop the engine
# quit - to exit
# """ )
#     elif command == "start":
#         if not car_start:
#             print("Car started")
#             car_start = True
#         else:
#             print("Car is already started")
#     elif command == "stop":
#         if car_stop:
#             print("Car stopped")
#             car_stop = False
#         else:
#             print("Car is already stopped")
#     elif command == "quit":
#         print("exit")
#         break
#     else:
#         print("I don't understand that")



#
# numbers = [2,2,2,2,5]
#
# for x_count in numbers:
#     Output = ""
#     for count in range(x_count):
#         Output += 'x'
#     print(Output)



# number = [-1, -17, -90, -87]
# largest = 0
# for item in number:
#     if item > largest:
#         largest = item
# print(largest)


lists = [1,2, 25, 75, 89, 100, 4766, 1, 3, 4, 5, 0, -1, -17, 4766]

for indexOut, x in enumerate(lists):
    for indexIn, y in enumerate(lists):
        if (x == y) and (indexOut != indexIn) and indexIn > indexOut:
            print(f'IndexOut {indexOut} IndexIn{indexIn} Value {x}')
            break


























