"""
Способ определения четности числа с помощью деления с остатком работает быстро и правильно,
 но это только в python, в таких ЯП как С++ и Pascal
 деление отрицательного нечетного числа на 2 даст -1, а не 1.
  При этом бинарное И (&) везде работает одинаково.
"""


def isEven(number):
    return number % 2 == 0


def isEvenBinary(number):
    return not number & 1


x = 11
print(isEven(x))
print(isEvenBinary(x))
