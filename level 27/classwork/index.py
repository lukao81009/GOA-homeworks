# string functions

# ==================

# format() - დავაპორმატოთ ცვლადები, უფრო დეტალუკად: მნიშვნელობები ჩავაშენოთ სხვა მნიშვნელობებში ან ცვლადებში.

# basic way

# name = 'Davit'
# last_name = 'Janezashvili'

# info = 'Hello my name is ' + name + ' ' + 'my last name is' + ' ' + last_name
# print(info)



# format()

# name = 'Davit'
# last_name = 'Janezashvili'

# info = 'Hello my name is {0} my last name is {1} .format(name, last_name)
# print(info)


# some = '{x} {y}'.format(x=10, y=12)

# print(some)

# =============
# third way - simple & comfortable

# name = 'Davit'
# last_name = 'Janezashvili'
# num = 100
#                           'Davit'                'Janezashvili'
# info = f'Hallo my name is {name} and last name is {last_name} aaand {num}'
# print(info)



# nm = 'Dt'
# num = 1


# info = 'my nm is' + nm + 'my age is' + num
# print(info)


# =================================================================

# join() - სიის შემთხვევაში, სიაში არსებული მნიშვნელობები გარდაიქმნება სტრინგად და სტრინგებს ერთმანეთისგან გამოვყოფთ რაიმე ნებისმიერი სიმბოლით/ასოგერით/რიცხვით


# values = ['dato', 'gio', 'dachi']

# without embbed list

# values = ['dato', 'gio', 'dachi']

# new_list = ' -! '.join(values)
# print(values)

# with embbed list

# values =' cool '.join(['dato', 'gio', 'dachi'])
# print(values)




# strr = ' :) '.join('Hello World!')
# print(strr)


x = 'H#el#l#o####'

# remove all '#'

# new_x = x.split('#')
# print(new_x)




# x = 'Hello'
# print(x)




# strr = 's---o---m-e -t----x--t'

# new_strr = strr.split('-')

# convert_list_to_str = ''.join(new_strr)

# print(convert_list_to_str)



# strr = 'dadadadada ananaanananababababb mamamma babababa'

# new_str = strr.split('a', 15)

# convert_list_to_str = ''.join(new_str)

# print(convert_list_to_str)


# =================================================================
# replace() - სტრინგში შევცვალოთ სიტყვა სხვა სიტყვით

# txt = 'Hello Group 34'

# new_txt = txt.replace('34', '32')
# print(new_txt)


# =================================================================
# lower() - აპატარავებს ასობგერებს
# upper() - ადიდებს ასობგერებს


# x = 'HELLO'
# y = 'word'

# print(x.lower())
# print(y.upper())