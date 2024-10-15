# 1)მნიშვნელობების დამატება და შეცვლა სიაში
# შექმენი სია სახელწოდებით numbers, რომელიც შეიცავს 5 რიცხვს.
# სიის ბოლოს დაამატე ორი ახალი რიცხვი.
# შეცვალე სიის მესამე ელემენტი ნებისმიერი სხვა რიცხვით.
# დაბეჭდე სიის ყველა ელემენტი ინდივიდუალურად.

numbers = [1, 2, 0, 4, 5]

numbers.append(6)
numbers.append(7)

numbers[2] = 3

print(numbers)


# 2) not და in keyword-ების გამოყენება სიაში
# შექმენი სია სახელწოდებით fruits, რომელიც შეიცავს რამდენიმე ხილის დასახელებას.
# შეამოწმე, არის თუ არა apple სიის ნაწილი. თუ არაა, დაამატე იგი.
# გამოყენებით not in, დარწმუნდი რომ banana არ არის სიაში და დაბეჭდე შესაბამისი შეტყობინება.

fruits = ["orange", "grape", "mango", "pear"]

if "apple" not in fruits:
    fruits.append("apple")

print(fruits)
print("apple" in fruits)
print("banana" not in fruits)