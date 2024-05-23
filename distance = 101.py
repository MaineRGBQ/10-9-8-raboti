#distance = 10
#total_distance = 0
#
#for i in range(7):
#    total_distance += distance
#    distance *= 1.1
#
#print(f"Суммарный путь спортсмена за 1 неделю: {total_distance} км")


#input_string = input("Введите строку из слов, разделенных пробелами: ")
#words = input_string.split()
#reversed_words = words[::-1]
#reversed_string = " ".join(reversed_words)
#print("Новая строка с переставленными словами:") 
#print(reversed_string)


#text =str(input("Введите слова через пробел: "))
#new_text = ", ".join(text.split())
#print(new_text)


#str1 = input("Введите первую строку: ") 
#str2 = input("Введите вторую строку: ")
#if str1[-1] == str2[0]: print("ВЕРНО") 
#else: print("НЕВЕРНО")


#word = input("Введите слово: ")
#if len(word) < 4: print("НЕТ") 
#else: print("Четвертая буква:", word[3])


#while True:
#    word = input("Введите слово: ")
#    if word[0] not in ['с', 'С']:
#        break
#    print(word)


#text = input("Введите строку: ") 
#result = ""
#for char in text: result += char * 2
#print("Результат:", result)


#words = input("Введите строку слов, разделенных пробелами: ")
#words_list = words.split()
#longest_word = ''
#for word in words_list: 
#    if len(word) > len(longest_word): 
#        longest_word = word
#print(longest_word)


#input_string = input("Введите строку: ")
#filtered_string = ""
#for char in input_string:
#    if char != " " and char not in filtered_string:
#        filtered_string += char
#print(filtered_string)


#s = input("Введите строку: ")
#s = s.strip()
#s = ' '.join(s.split())
#print("Нормированная строка:", s)


#set1 = {3, 7, 9, 15, 21} 
#set2 = {5, 9, 15, 20, 25}
#unique_nums_set1 = set(set1) 
#unique_nums_set2 = set(set2)
#print("Уникальные числа в первом множестве:", unique_nums_set1) 
#print("Уникальные числа во втором множестве:", unique_nums_set2)
#common_nums = sorted(unique_nums_set1.intersection(unique_nums_set2)) 
#print("Числа, которые входят как в первое, так и во второе множество в порядке возрастания:", common_nums)


#sequence = input("Введите последовательность символов: ")
#unique_set = set()
#for char in sequence: unique_set.add(char)
#print("Множество уникальных символов:", unique_set)


for i in range(10): 
    print(i)


for i in range(26): 
    if i <= 5 or (i >= 10 and i <= 15): 
        print(chr(65+i))


for i in range(5, 10): 
    print(i) 
    print('+') 
    print('-') 
    print('*') 
    print('/')


print('+') 
print('-') 
print('*') 
print('/') 
print(',') 
print('.') 
print(';') 
print(':')


print('.') 
print(',') 
print(';') 
print(':') 
print('<') 
print('>') 
print('==') 
print('!=')


print('+')
print('-') 
print('*') 
print('/') 
print('%') 
print('//')


for i in range(14): 
    if i >= 5: 
        print(chr(69+i))


print('+') 
print('-') 
print('*') 
print('/') 
print('%') 
print('//') 
print('<') 
print('>') 
print('==') 
print('!=')


for i in range(10): 
    print(i) 
    print('+') 
    print('-') 
    print('*') 
    print('/')


for i in range(26): 
    if (i <= 5) or (i >= 23): 
        print(chr(65+i))

