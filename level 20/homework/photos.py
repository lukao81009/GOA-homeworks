# 1) ====================================================================

alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

index1 = int(input("Enter first number: "))
index2 = int(input("Enter seconde number: "))
index3 = int(input("Enter third number: "))

print(alpha[index1] + alpha[index2] + alpha[index3])

# 2) ====================================================================

x = [42, 8, 7, 1, 0, 124, 8897, 555, 3, 67, 99]

num = int(input('Enter number to win prize: '))

if num in x:
    print("bingo")

# 3) ====================================================================

supported = ['Lights off', 'Lock the door', 'Open the door', 'Make coffee', 'Shut down']

command = input('Say word: ')

if command in supported:
    print("OK")
else:
    print("Unknown")