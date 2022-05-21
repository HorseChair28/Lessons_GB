my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '-5', 'градусов']
for parts in range(len(my_list)):
    part = my_list.pop(0)
    if part.isdigit():
        my_list.append(f'"{int(part):02d}"')
    elif (part[0] == "-" or part[0] == "+") and part[1:].isdigit():
        my_list.append(f'"{part[0]}{int(part[1:]):02d}"')
    else:
        my_list.append(part)

print(' '.join(my_list))
