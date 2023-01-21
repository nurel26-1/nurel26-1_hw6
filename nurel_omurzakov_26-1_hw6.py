import re

while True:
    answer = int(input('1) Names and surnames\n '
                        '2) Emails\n '
                        '3) Files\n '
                        '4) Colors\n '
                        '5) Exit\n '
                        'CHOOSE NUMBER: '))
    if answer == 1:
        with open('MOCK_DATA.txt', 'r', encoding='utf-8') as file:
            text = file.read()
            names = re.findall(r"[A-Z][a-z-]+\s+[a-zA-Z][a-zA-Z- ']*", text)
            with open('names.txt', 'w', encoding='utf-8') as file:
                file.write(str(', ').join(names))
    elif answer == 2:
        with open('MOCK_DATA.txt', 'r', encoding='utf-8') as file:
            text = file.read()
            emails = re.findall(r'[a-z|\d]+@[a-z|\d-]+\.[a-z]{2,3}\.?[a-z]*', text)
            with open('emails.txt', 'w', encoding='utf-8') as file:
                file.write(str(', ').join(emails))
    elif answer == 3:
        with open('MOCK_DATA.txt', 'r', encoding='utf-8') as file:
            text = file.read()
            files = re.findall(r'[A-Z][a-zA-Z]*\.[a-z\d]{3,4}', text)
            with open('files.txt', 'w', encoding='utf-8') as file:
                file.write(str(', ').join(files))
    elif answer == 4:
        with open('MOCK_DATA.txt', 'r', encoding='utf-8') as file:
            text = file.read()
            colors = re.findall(r'#[\d|a-z]{6}', text)
            with open('colors.txt', 'w', encoding='utf-8') as file:
                file.write(str(', ').join(colors))
    elif answer == 5:
        break
