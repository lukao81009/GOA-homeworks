
for i in range(10):
    print("hallo")

for i in range(1, 100, 5):
    print(i)


while True:
    print('hello')

i = 0
while i <= 10:
    print('hello')
    i += 1


# თუ ასაკი მეტია 20 ზე, მაშინ გამოიტანოსს, შენ ხარ სრულწლოვანი, ხოლო სხვა შემთხვევაში, გამოიტანოს, შენ ხარ არასრულწლოვანი.

True
if 25 > 20:
    print('შენ ხარ სრულწლოვანი')

# False
if 2 > 20:
    print('შენ ხარ სრულწლოვანი')
else:
    print('შენ ხარ არასრულწლოვანი')

age = 10

if age > 20:
    print('შენ ხარ სრულწლოვანი')
else:
    print('შენ ხარ არასრულწლოვანი')

age = int(input('Enter age: '))

if age > 20:
    print('შენ ხარ სრულწლოვანი')
else:
    print('შენ ხარ არასრულწლოვანი')

x = int(input('Enter x: '))
y = int(input('Enter y: '))

if True:
    print(x + y)
else:
    print('შენ ხარ არასრულწლოვანი')


temp = 40

if temp > 56:
    print('ძალიან ცხელა')
elif temp > 41:
    print('მეორედ მოწმდება და ძალიან ცხელია')
elif temp > 31:
    print('მესამედ მოწმდება და ძალიან ცხელია')
else:
    print('არ ცხელა')


text = input('enter word: ')

if text == 'start':
    print('თამაში დაიწყო')
elif text == 'stop':
    print('თამაი შეწყდა')
elif text == 'tie':
    print('თამაი ფრედ დასრულდა')

text = input('enter word: ')

if text == 'start' or text == 'stop' :
    print('თამაში ან დაიწყება ან გაჩერდება')