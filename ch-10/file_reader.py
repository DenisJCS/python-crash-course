filename = '../../python-crash-course_resources/pcc/chapter_10/pi_million_digits.txt'

with open(filename) as file_object:
    # contents = file_object.read()
    # print(contents.rstrip())

    # for line in file_object:
    #     print(line.rstrip())

    lines = file_object.readlines()

    pi_string = ''

for line in lines:
    pi_string += line.rstrip()

birthday = input("Enter bday as mmddyy:\n")

if birthday in pi_string:
    print('Bday appear in pi!')
else:
    print('No bday in pi!')

