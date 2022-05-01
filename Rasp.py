import datetime
import numpy as np
import re

dayWeek = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье", "неделя", "2 - неделя",
           "пн", "вт", "ср", "чт", "пт", "сб", "вс",
           "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "week",
           "сегодня", "завтра"]


def teacher(name):
    for i in teachers:
        for j in i:
            if name in j.lower():
                return ("\n".join(i).split("~")[0])


def fullteach():
    res = ""
    for i in teachers:
        for j in i:
            if not "~" in j:
                res += j
                res += "\n"
        res += "\n"
    return res


def fullteach1():
    res = ""
    for i in teachers:
        for j in i:
            res += j
            res += "\n"
        res += "\n"

    return re.sub('\d|[A-z]|\W', '', res).lower()


def day(x, y):
    res = ''
    for i in shed[x, y, 0::]:
        if '---' not in i:
            res += i.split("\n")[0] + '\n'
    return res


def week(x):
    res = ''
    for y in range(6):
        for i in shed[x, y, 0::]:
            if '---' not in i:
                res += i.split("\n")[0] + '\n'
        res += '\n'
    return res


def twoWeek():
    res = ''
    for x in range(2):
        res = '`````````````````````````' + '\n '
        for y in range(6):
            for i in shed[x, y, 0::]:
                if '---' not in i:
                    res += i.split("\n")[0] + '\n'
            res += '\n'
    return res


def weekday(message):
    date = datetime.datetime.today() + datetime.timedelta(hours=3)
    weekNum = date.isocalendar()[1] % 2
    dayNum = date.weekday()
    if message == 'понедельник' or message == 'пн' or message == 'monday':
        return day(weekNum, 0)
    elif message == 'вторник' or message == 'вт' or message == 'tuesday':
        return day(weekNum, 1)
    elif message == 'среда' or message == 'ср' or message == 'wednesday':
        return day(weekNum, 2)
    elif message == 'четверг' or message == 'чт' or message == 'thursday':
        return day(weekNum, 3)
    elif message == 'пятница' or message == 'пт' or message == 'friday':
        return day(weekNum, 4)
    elif message == 'суббота' or message == 'сб' or message == 'saturday':
        return day(weekNum, 5)
    elif message == 'воскресенье' or message == 'вс' or message == 'sunday':
        return "Сегодня у тебя выходной)"
    elif message == 'неделя' or message == 'week':
        return week(weekNum)
    elif message == '2 - неделя':
        if weekNum == 0:
            weekNum = 1
        else:
            weekNum = 0
        return week(weekNum)
    elif message == 'сегодня':
        if dayNum == 6:
            return "Сегодня у тебя выходной)"
        return day(weekNum, dayNum)
    elif message == 'завтра':
        dayNum += 1
        if dayNum == 6:
            return "Завтра у тебя выходной)"
        elif dayNum == 7:
            dayNum = 0
            if weekNum == 0:
                weekNum = 1
            else:
                weekNum = 0
        return day(weekNum, dayNum)
