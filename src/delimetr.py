"""
Операции с системами исчисления
Далее СИ - система исчисления
"""

import decimal


def from_decimal_to_any(a: int, base: int) -> int:
    """
    Перевод числа из десятичной СИ в любую другую с основанием от 2 до 10

    Параметры
    ----------
    a : int
        число в десятичной СИ

    base : int
        число основания переводимой СИ

    Возвращаемые данные
    -------
    int
        Число в новой СИ
    """
    # Проверка кода, необязательная для работы алгоритма
    if a < 0:  # Проверка на неотрицательность чисел
        raise TypeError("Number less than zero")
    if base <= 1 or base > 10:  # проверка основания СИ больше единицы
        raise TypeError("The basis of the calculation system is not positional")

    char: str = ""

    while a // base != 0:  # пока целая часть от числа не равна нулю
        char += str(a % base)  # прибавляем остаток от деления в итоговый результат
        a //= base  # заменяем переменную "a" на целую часть от числа
    char += str(a % base)  # добавляем последнюю цифру

    return int(char[::-1])  # переворачиваем число и из str переводим в int


def from_any_to_decimal(a: int, base: int) -> int:
    """
    Перевод из любой СИ с основанием от 2 до 9 в десятичную СИ

    Параметры
    ----------
    a : int
        число в начальной СИ
    base : int
        основание начальной СИ

    Возвращаемые данные
    -------
    int
        число в десятичной СИ
    """
    # Проверка кода, необязательна для работы алгоритма
    if a < 0:  # Проверка на неотрицательность чисел
        raise TypeError("Number less than zero")
    if base <= 1 or base > 10:  # проверка основания СИ больше единицы
        raise TypeError("Incorrect base")


    number: int = 0
    str_a: str = str(a)  # начальное сичло в виде строки
    lenght: int = len(str_a) - 1  # длина всего числа начиная с нуля

    for num in str_a:
        number += int(num) * pow(base, lenght)  # стандартный перевод: n * base**lenght
        lenght -= 1  # минусуем длину, так как одно число уже посчитано

    return number
