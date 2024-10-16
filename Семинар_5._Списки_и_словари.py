# Задача 1.

# Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.

# Найдите количество и выведите его.


# Решение:

# list_1 = [1, 2, 3, 4, 5]
# k = 3
list_2 = []

# Введите ваше решение ниже

for i in range(len(list_1)):
    if list_1[i] == k:
        list_2.append(list_1[i])

print(len(list_2))


# Задача 3. 
# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.

# В случае с английским алфавитом очки распределяются так:

# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:

# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.


# Напишите программу, которая вычисляет стоимость введенного пользователем слова k и выводит его. Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

# Решение:

# k = 'ноутбук'

# Введите ваше решение ниже

this_dict = {
    1: "AEIOULNSTRАВЕИНОРСТ",
    2: "DGДКЛМПУ",
    3: "BCMPБГЁЬЯ",
    4: "FHVWYЙЫ",
    5: "KЖЗХЦЧ",
    8:  "JXШЭЮ",
    10: "QZФЩЪ"
}

res = sum(([key for letter in k.upper() for key, value in this_dict.items() if letter in value]))

print(res)
