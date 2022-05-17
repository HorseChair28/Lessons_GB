duration = int(input("Введите интервал в секундах:"))
day = (duration // 86400)
hour = (duration // (60 * 60) - 24 * day)
minutes = (duration // 60 % 60)
seсonds = duration % 60
print("Ответ:", day, "дн", hour, "час", minutes, "мин", seсonds, "сек")
