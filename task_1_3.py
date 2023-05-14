# -*- coding: utf-8 -*-
"""task_1.3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OEWG6Dwq-4bZLtsk21L1N8-iQRAxPxk8
"""

# Напишите скрипт, который принимает от пользователя номер месяца, 
# а возвращает количество дней в нем.
# Результат проверки вывести на консоль
# Допущение: в феврале 28 дней
# Если номер месяца некорректен - сообщить об этом

# Например,
    # Введите номер месяца: 3
    # Вы ввели март. 31 дней

    # Введите номер месяца: 2
    # Вы ввели февраль. 28 дней

    # Введите номер месяца: 15
    # Такого месяца нет!

months= [['Январь',31],
        ['Февраль',28],
        ['Март',31],
        ['Апрель',30],
        ['Май',31],
        ['Июнь',30],
        ['Июль',31],
        ['Август',31],
        ['Сентябрь',30],
        ['Октябрь',31],
        ['Ноябрь',30],
        ['Декабрь',31]
         ]

try:
  number=int(input('Введите номер месяца'))
  print(f'Вы ввели {months[number-1][0]}.{months[number-1][1]} дней')
   
except:
  print('Такого месяца нет! Введи число от 1 до 12')



#for ind, month in enumerate(months):
  #ind +=1