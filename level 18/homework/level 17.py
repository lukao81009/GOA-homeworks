# 1) დავალება
# ააგეთ პროგრამა, რომელიც მოსთხოვს მომხმარებელს, რომ შეიყვანეს რიცხვი 1 - 100 მდე.

# პროგრამის დანიშნულება არის ის, რომგამოიცნოს მომხმარებლის მიერ შემოტანილი რიცხვი, იმდენჯერ მიეცეს გამოცნობის შესაძლებლობა სანამ საბოლოოდ არ გამოიცნობს.


o = int(input('enter number: '))

if 1 < o and o < 100:
    print(True)
else:
    print (False)


number = int(input('input a number: '))
g  = 5
while number != g:
    number = int(input('input a number: '))


# 2) დავალება - 'FizzBuzz'
# FizzBuzz მიზანი:
# შექმენით პროგრამა, რომელიც ბეჭდავს რიცხვებს 1-დან 100-მდე. თუმცა 3-ის ჯერადებისთვის რიცხვის ნაცვლად დაბეჭდეთ „Fizz“, ხოლო 5-ის ჯერადებისთვის დაბეჭდეთ „Buzz“. 3-ისა და 5-ის ჯერადი რიცხვებისთვის დაბეჭდეთ "FizzBuzz".  მოთხოვნები: გამოიყენეთ მარყუჟი 1-დან 100-მდე რიცხვების გასამეორებლად.
# გამოიყენეთ პირობითი განცხადებები, რათა შეამოწმოთ რიცხვი იყოფა 3-ზე, 5-ზე ან ორივეზე. დაბეჭდეთ შესაბამისი სიტყვა ("Fizz", "Buzz" ან "FizzBuzz") ან ნომერი. 




for number in range(1, 10):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)









# 3) დავალება
# დაწერეთ პროგრამა სადაც შეამოწმეთ, სტუდენტმა ჩააბარა თუ არა ჩააბარა კურსი მათი გამოცდის ქულების მიხედვით. სთხოვეთ მომხმარებელს შეიყვანოს ქულები შუალედური გამოცდისთვის, დასკვნითი გამოცდისთვის და პროექტისთვის. დარწმუნდით, რომ მომხმარებელმა შეიყვანოს სწორი ქულები (პოზიტიური რიცხვები 0-დან 100-მდე) თითოეული კომპონენტისთვის.
# გამოიყენეთ შემდეგი შეფასების კრიტერიუმები: თუ საშუალო ქულა (20% შუალედური კურსისთვის, 40% საბოლოო და 40% პროექტისთვის) არის 70 ან მეტი, სტუდენტი გაივლის კურსს. თუ საშუალო ქულა 70-ზე დაბალია, სტუდენტი ვერ ახერხებს კურსის ჩაბარებას. აჩვენეთ მომხმარებლისთვის შეტყობინება, რომელშიც მითითებულია მისი გავლის/ჩავარდნის სტატუსი და გამოთვლილი საშუალო ქულა.


შუალედური_გამოცდის_ქულა = float(input("შუალედური გამოცდის ქულა: "))

საბოლოო_გამოცდის_ქულა = float(input("საბოლოო გამოცდის ქულა: "))
პროექტის_ქულა = float(input("პროექტის ქულა: "))



შუალედური = 0.2
საბოლოო = 0.4
პროექტი = 0.4

average_score = (შუალედური_გამოცდის_ქულა * შუალედური) + (საბოლოო_გამოცდის_ქულა * საბოლოო) + (პროექტის_ქულა * პროექტი)

average_score / 3

if average_score >= 70:
    print("კურსი ჩაბარდა!")
else:
    print("კურსი არ ჩაბარდა.")





# 4) დავალება
# დაწერეთ პროგრამა სადაც შეამოწმებთ, აქვს თუ არა ადამიანს მართვის მოწმობის აღების უფლება მისი ასაკისა და მართვის გამოცდილებიდან გამომდინარე. დარწმუნდით, რომ მომხმარებელი შეიყვანს თავისი ასაკს და წლების რაოდენობა, რომელსაც მანქანას მართავდა.მომხმარებელმა უნდა შეიყვანოს დადებითი მთელი რიცხვები ასაკისა და მართვის გამოცდილებისთვის. (დაგნა მოხდეს ოპერაციები)
# გამოიყენეთ შემდეგი საკვალიფიკაციო კრიტერიუმები: პირი უნდა იყოს მინიმუმ 18 წლის მართვის მოწმობის მისაღებად. თუ პირი 18 წლამდეა, მას არ შეეძლება მართვის მოწმობის აღება. თუ პირი არის 18 წლის ან მეტი, მას უნდა ჰქონდეს მინიმუმ 1 წლიანი მართვის გამოცდილება, რომ დაშვებული იყოს მართვის მოწმობის აღებისთვის.
# მომხმარებლისთვის აჩვენეთ შეტყობინება, რომელშიც მითითებულია მართვის მოწმობის მიღების უფლება.


age = int(input('enter your age: '))
experiens = int(input('enter your drivin year experiens: '))
if age > 17 and 0 < experiens:
    print('you can take driving licens')
else:
    print('you cannot take driving licens')












