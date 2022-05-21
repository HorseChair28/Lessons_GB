my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
answer = {}

for parts in my_list:
    correct_name = parts.split(' ')[-1].capitalize()
    print(f"Привет, {correct_name}!")