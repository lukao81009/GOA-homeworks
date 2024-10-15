# 1) ====================================================

color = input("Enter color: ")

if color == "red":
    print("box #1")
elif color == "green":
    print("box #2")
elif color == "black":
    print("box #3")
else:
    print("unknown")

# 2) ====================================================

day = int(input('Enter day: '))
hour = int(input("Enter hour: "))

if 1 <= day <= 5 and 10 <= hour <= 21:
    print("Open")
elif day == 6 or day == 7:
    print("Closed")
else:
    print("Closed")

# 3) ====================================================

alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

index1 = int(input("Enter first number: "))
index2 = int(input("Enter seconde number: "))
index3 = int(input("Enter third number: "))

print(alpha[index1] + alpha[index2] + alpha[index3])

# 4) ====================================================

supported = ['Lights off', 'Lock the door', 'Open the door', 'Make coffee', 'Shut down']

command = input('Say word: ')

if command in supported:
    print("OK")
else:
    print("Unknown")

# 5) ====================================================

floors = int(input('Enter your floor: '))

for floor in range(5, floors + 1, 5):
    print(floor)

# 6) ====================================================

distance = 7425
speed = 550

flight_time = distance / speed

print(flight_time)

# 7) ====================================================

bill = float(input('Enter your bill: '))

tip = bill * 20 / 100

print(tip)