'''1) Написать код, который вычисляет сумму всех чисел, удовлетворяющих следующие условия:

    положительные целые числа от 1 до 1_000_000_002 (один миллиард два) включительно
    которые нацело (без остатка) делятся на 3 (пример: 3, 6, 9, ...)
    и которые не заканчиваются на 4 и 7 (пример заканчивающихся на 4 и 7: 24, 27, 54, 57 ...)
'''

num = 1_000_000_002
s = 0
for n in range(3, num + 1, 3): 
    if n % 10 != 4 and n % 10 != 7: 
        s += n 
print(s)

###

s_div3 = (3 + 1_000_000_002) / 2 * 1_000_000_002 / 3
s_div3_ends4 = (24 + 999_999_984)/ 2 * (999_999_984 + 6) / 30 
s_div3_ends7 = (27 + 999_999_987)/ 2 *(999_999_987 + 3) / 30
sum = s_div3 - s_div3_ends4 - s_div3_ends7

'''2) На вход поступает текстовый файл из 3-х тысяч строк
Формат файла:
    "арифметическая операция"    "целое число #1"    "целое число #2"
Разделитель - 4 пробела
Нужно подготовить текстовый файл из 1 строки.
Строка содержит набор из 3-х тысяч чисел, разделенных запятой. 
После последнего числа запятая не ставится.
каждое число - результат операции: 
    "результирующее целое число" = "целое число #1" применить "арифметическая операция" "целое число #2"'''
    
res1 = [] with open(path1) as inp:
    for line in inp:
        op, left, right = line.split()
        res1.append(eval(f'{left} {op} {right}'))
        with open(pathout, 'w') as ouf:
            ouf.write(','.join(map(str, res1)))
                
with open('input_file.txt') as inf:
    expressions = [[line.split()[i] for i in (1, 0 , 2)] for line in inf]
with open('output_.txt', 'w') as ouf:
    evaluated = (eval(' '.join(expr)) for expr in expressions)
    ouf.write(','.join(map(str, evaluated)) + '\n')
        
'''3) На вход поступает два текстовый файл из 3-х тысяч строк каждый.

    Первый файл содержит строки текста.   
     
    Второй файл содержит строки из двух целых неотрицательных чисел.
    Первое число в строке всегда меньше или равно второму.
    Числа всегда меньше длины соответствующей строки первого файла.
    Соответствующей - это значит 1-ая строка из 1-го файла соответствует 1-ой строке из 2-го файла, а 123-я строка из 1-го файла соответствует 123-ей строке из 2-го файла.
     
    Подготовить выходной файл, который состоит из подстрок 1-го входного файла.
    Подстроки разделены пробелами.
    Какие брать подстроки - написано во втором файле.
    В конце файла пробела нет.

Например:
    120 строка в 1-ом файле: JBOljrfkrfjgikenfjerkrkvkfKUGlknc
    120 строка во 2-ом файле: 13 27
Это значит 120 подстрока в результирующем файле это символы с 13 по 27, включая 13-ый и 27-ой символы.
Не забывайте, что нумерация символов в строке с 0.
Пример требуемой подстроки: kenfjerkrkvkfKU'''

lines, indices = open(r'import1.txt'), open(r'import2.txt')
out_file = open(r'output1.txt', 'w')
for line, inds in zip(lines, indices):
    ind1, ind2 = [int(ind) for ind in inds.split()]
    out_file.write(line[ind1 : ind2 + 1] + ' ')
out_file.write('\n')
lines.close(), indices.close(), out_file.close()

with open(r'import_file_2_1.txt') as inf: 
    lines = [line.strip() for line in inf]
with open(r'import_file_2_2.txt') as indsf: 
    indices = [[*map(int, indexes.split())] for indexes in indsf]
with open(r'output1_.txt', 'w') as outf:    
    newlines = (line[ind[0] : ind[1]+1] for line, ind in zip(lines, indices))
    outf.write(' '.join(newlines) + '\n')

'''4) На вход поступает строка.
В ней хранится набор химических символов (He, O, H, Mg, Fe, ...). Без пробелов.
Нужно расшифровать химические символы в название химических элементов.
Для удобства, прилагается json файл, который ставит в соответствие химическому символу его химическое название.
Как прочитать этот файл в словарь python (dict):

periodic_table = json.load(open('periodic_table.json'))

Пример входной строки:

NOTiFICaTiON

Пример выходной строки:

АзотКислородТитанФторЙодКальцийТитанКислородАзот'''

import json
periodic_table = json.load(open('periodic_table.json', encoding='utf-8'))
with open('import_file_3.txt') as inf: line = line1 = inf.read().strip()
for key in sorted(periodic_table.keys(), key=lambda x: len(x), reverse=True):
    line = line.replace(key, periodic_table[key])
with open('output2.txt', 'w') as ouf:
    ouf.write(line + '\n')

###

import re
outlist = [periodic_table[sub] for sub in re.findall(r'[A-Z][a-z]*', line1)]
with open('output2_.txt', 'w') as ouf:
    print(*outlist, file=ouf, sep='')
