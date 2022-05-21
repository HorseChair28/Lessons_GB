my_list = [57.8, 46.51, 97, 48.48, 911, 153.50, 66.69, 1232.33]
correct_list = []
for price in my_list:
    rub = int(price)
    kop = (price-rub)*100
    correct_list.append(f"{rub} руб  {kop:02.0f} коп")
print(correct_list)
print(id(my_list))
my_list.sort(key=None, reverse=True)
print(my_list)
print(id(my_list))
correct_list = []
for price in my_list:
    rub = int(price)
    kop = (price-rub)*100
    correct_list.append(f"{rub} руб  {kop:02.0f} коп")
print(correct_list[0:5])
















