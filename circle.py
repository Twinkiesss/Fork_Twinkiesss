import math


def area(r):
    '''Принимает число r, возвращает площадь круга с радиусом r. Example: r = 2 => S = pi * 4 ~ 12,56'''
    return math.pi * r * r


def perimeter(r):
    '''Принимает число r, возвращает периметр круга. Example: r = 2 => P = pi * 4 ~ 12,56'''
    return 2 * math.pi * r

