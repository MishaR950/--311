# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pG2LoVI9hiOAh0dC4t82ion4alQGe1O0
"""

a = int(input())
if a == 1:
  print('Январь')
if a == 2:
  print('Февраль')
if a == 3:
  print('Март')
if a == 4:
  print('Апрель')
if a == 5:
  print('Май')
if a == 6:
  print('Июнь')
if a == 7:
  print('Июль')
if a == 8:
  print('Август')
if a == 9:
  print('Сентябрь')
if a == 10:
  print('Октябрь')
if a == 11:
  print('Ноябрь')
if a == 12:
  print('Декабрь')

a = int(input())
if a % 2 == 0:
  print(a,'Четное')
else:
  print(a,'Нечетное')

N = int(input())
if N > 40:
  print('stonks')
else:
  print('not stonks')

Year = int(input())
if Year % 4 == 0:
   print(True)
else:
  print(False)

a = False
n = int(input())
for i in range(2,n):
  if n % i == 0:
    a = False
    break
  else:
    a = True
print(a)

a = int(input())
b = int(input())
if a % b >= 3.6:
  a,b = b,a
elif b >= abs(-138/2)^1.3 or b <= abs((-69/28^5.1)*4):
  a,b = b,a
else: 
  print(a,b)