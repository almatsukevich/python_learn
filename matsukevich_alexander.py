phrase = 'Не знаю, как там в Лондоне, я не была. Может, там собака — друг чело'\
         'века. А у нас управдом — друг человека!'
print('Шаг1 - Количество символов - ', len(phrase))
print('Шаг2 - Развернутая строка - ', phrase[::-1])
print('Шаг3 - Каждое слово с большой буквы - ', phrase.title())
print('Шаг4 - Все буквы прописные - ', phrase.upper())
print('Шаг5 - Число вхождений подстроки: \n\t"нд" - ', phrase.count('нд'), 
      ';\n\t"ам" - ', phrase.count('ам'), ';\n\t"о" - ', phrase.count('о'), ';')
print('Шаг6 - Собственные упражнения:')
print('Разделение строки на предложения и вывод списком:')
print('\t', '\n\t' .join(phrase.split('.')))
print('Извлечение среза и повторение 3 раза: \n\t', phrase[0:9]*3)
print('Шаг7 - Исходная строка - ', phrase)