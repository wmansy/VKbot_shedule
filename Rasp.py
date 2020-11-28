import datetime
import numpy as np
import re

shed = np.array([[
    ["Понедельник",
     "|09:30-11:05| -----",
     "|11:20-12:55| -----",
     "|13:10-14:45| Цифровые технологии Smart City л.р. \n--",
     "|15:25-17:00| Программная инженерия л.р.\nhttps://us04web.zoom.us/j/5417715940?pwd=S3dEY2VvKzR6eHA5NWs3cDFFa3F0UT09",
     "|17:15-18:50| Физическая культура ДО \nlms.mtuci.ru/lms/mod/bigbluebuttonbn/view.php?id=16886&group=0"],
    ["Вторник",
     "|09:30-11:05| Технологии нечеткого управления лек.\nhttps://us04web.zoom.us/j/4678454922?pwd=dXlCK1B0OXVJVzg5QTdyQ0VKNGZwdz09",
     "|11:20-12:55| Сетевые технологии лек.\nhttps://us04web.zoom.us/j/4678454922?pwd=dXlCK1B0OXVJVzg5QTdyQ0VKNGZwdz09",
     "|13:10-14:45| Цифровые технологии пр.з. \n--",
     "|15:25-17:00| Микропроцессоры в РСУ пр.з. \n--",
     "|17:15-18:50| Технология Базы Данных лек.\nhttps://us02web.zoom.us/j/78142002672?pwd=bGRGWDlWWFJIL1hlaGNXVWFlTjZQZz09"],
    ["Среда",
     "|09:30-11:05| Сетевые технологии лаб. \nhttps://us04web.zoom.us/j/4678454922?pwd=dXlCK1B0OXVJVzg5QTdyQ0VKNGZwdz09",
     "|11:20-12:55| Технологии нечеткого управления лаб. \nhttps://us04web.zoom.us/j/4678454922?pwd=dXlCK1B0OXVJVzg5QTdyQ0VKNGZwdz09",
     "|13:10-14:45| Технология баз данных лаб. \nhttps://us04web.zoom.us/j/6771401873?pwd=QUU3ZTRaRnhZSnR1eHFMbTc2Rzg5dz09",
     "|15:25-17:00| -----",
     "|17:15-18:50| -----"],
    ["Четверг",
     "|09:30-11:05| ТНУ пр.з.\nhttps://us04web.zoom.us/j/4678454922?pwd=dXlCK1B0OXVJVzg5QTdyQ0VKNGZwdz0",
     "|11:20-12:55| ТАУ л.р.\nhttps://us04web.zoom.us/j/6874235879?pwd=Nnl0NmcxUlIxdFI2eElPNnBZcm8rQT09",
     "|13:10-14:45| ТАУ лек.\nhttps://us04web.zoom.us/j/6874235879?pwd=Nnl0NmcxUlIxdFI2eElPNnBZcm8rQT09",
     "|15:25-17:00| Физическая культура\nlms.mtuci.ru/lms/mod/bigbluebuttonbn/view.php?id=16886&group=0",
     "|17:15-18:50| -----"],
    ["Пятница",
     "|09:30-11:05| Экология л.р.\nhttps://us04web.zoom.us/j/2823911433?pwd=VExFN1ViZWRyeS94eU5wVDc1cWhoUT09",
     "|11:20-12:55| Экология лек.\nhttps://us04web.zoom.us/j/2823911433?pwd=VExFN1ViZWRyeS94eU5wVDc1cWhoUT09",
     "|13:10-14:45| Микропроцессоры в РСУ л.р. \n--",
     "|15:25-17:00| Микропроцессоры в РСУ л.р. \n--",
     "|17:15-18:50| -----"],
    ["Суббота",
     "|09:30-11:05| Программная инженерия лек.\nhttps://us04web.zoom.us/j/5417715940?pwd=S3dEY2VvKzR6eHA5NWs3cDFFa3F0UT09",
     "|11:20-12:55| -----",
     "|13:10-14:45| -----",
     "|15:25-17:00| Микропроцессоры в РСУ лек. \n--",
     "|17:15-18:50| -----"]],
    [["Понедельник",
      "|09:30-11:05| -----",
      "|11:20-12:55| -----",
      "|13:10-14:45| Цифровые технологии Smart City л.р. \n--",
      "|15:50-17:20| Программная инженерия л.р.\nhttps://us04web.zoom.us/j/5417715940?pwd=S3dEY2VvKzR6eHA5NWs3cDFFa3F0UT09\n--",
      "|17:15-18:50| Физическая культура ДО\nlms.mtuci.ru/lms/mod/bigbluebuttonbn/view.php?id=16886&group=0"],
     ["Вторник",
      "|09:30-11:05| Цифровые технологии Smart City лек. \n--",
      "|11:20-12:55| Сетевые технологии лек.\nhttps://us04web.zoom.us/j/4678454922?pwd=dXlCK1B0OXVJVzg5QTdyQ0VKNGZwdz09",
      "|13:10-14:45| Программная инженерия пр.з\nhttps://us04web.zoom.us/j/5417715940?pwd=S3dEY2VvKzR6eHA5NWs3cDFFa3F0UT09",
      "|15:25-17:00| Микропроцессоры в РСУ пр.з \n--",
      "|17:15-18:50| Технология Базы Данных лек.\nhttps://us02web.zoom.us/j/78142002672?pwd=bGRGWDlWWFJIL1hlaGNXVWFlTjZQZz09"],
     ["Среда",
      "|09:30-11:05| -----",
      "|11:20-12:55| Технологии нечеткого управления л.р.\nhttps://us04web.zoom.us/j/4678454922?pwd=dXlCK1B0OXVJVzg5QTdyQ0VKNGZwdz09",
      "|13:10-14:45| Технология баз данных л.р. \nhttps://us04web.zoom.us/j/6771401873?pwd=QUU3ZTRaRnhZSnR1eHFMbTc2Rzg5dz09",
      "|15:25-17:00| -----",
      "|17:15-18:50| -----"],
     ["Четверг",
      "|09:30-11:05| ТАУ пр.з.\nhttps://us04web.zoom.us/j/6874235879?pwd=Nnl0NmcxUlIxdFI2eElPNnBZcm8rQT09",
      "|11:20-12:55| ТАУ л.р.\nhttps://us04web.zoom.us/j/6874235879?pwd=Nnl0NmcxUlIxdFI2eElPNnBZcm8rQT09",
      "|13:10-14:45| ТАУ лек.\nhttps://us04web.zoom.us/j/6874235879?pwd=Nnl0NmcxUlIxdFI2eElPNnBZcm8rQT09",
      "|15:25-17:00| Физическая культура\nlms.mtuci.ru/lms/mod/bigbluebuttonbn/view.php?id=16886&group=0",
      "|17:15-18:50| -----"],
     ["Пятница",
      "|09:30-11:05| Экология л.р.\nhttps://us04web.zoom.us/j/2823911433?pwd=VExFN1ViZWRyeS94eU5wVDc1cWhoUT09",
      "|11:20-12:55| Экология лек.\nhttps://us04web.zoom.us/j/2823911433?pwd=VExFN1ViZWRyeS94eU5wVDc1cWhoUT09",
      "|13:10-14:45| Технология Базы Данных пр.з.\nhttps://us04web.zoom.us/j/6771401873?pwd=QUU3ZTRaRnhZSnR1eHFMbTc2Rzg5dz09",
      "|15:25-17:00| Технология Базы Данных пр.з.\nhttps://us04web.zoom.us/j/6771401873?pwd=QUU3ZTRaRnhZSnR1eHFMbTc2Rzg5dz09",
      "|17:15-18:50| -----"],
     ["Суббота",
      "|09:30-11:05| Программная инженерия лек.\nhttps://us04web.zoom.us/j/5417715940?pwd=S3dEY2VvKzR6eHA5NWs3cDFFa3F0UT09",
      "|11:20-12:55| -----",
      "|13:10-14:45| -----",
      "|15:25-17:00| Микропроцессоры в РСУ лек. \n--",
      "|17:15-18:50| -----"]]
])
teachers = [
    ["Шукенбаев Айрат Бисенгалеевич", "shukenbaev@mail.ru", "Программная инженирия",
     "https://us04web.zoom.us/j/5417715940?pwd=S3dEY2VvKzR6eHA5NWs3cDFFa3F0UT09", "~ ПИ Щука"],
    ["Безумнов Данил Николаевич", "d.n.bezumnov@mtuci.ru", "Цифровые технологии Smart City", "Микропроцессоры в РСУ",
     "the link is missing", "~ Безумноу смарт сити "],
    ["Ларин Александр Иванович", "a.i.larin@mtuci.ru", "Технологии нечеткого управление", "Сетевые технологии",
     "https://us04web.zoom.us/j/4678454922?pwd=dXlCK1B0OXVJVzg5QTdyQ0VKNGZwdz09", "~ ТНУ"],
    ["Воронов Вячеслав Игоревич", "Технологии базы данных",
     "https://us02web.zoom.us/j/78142002672?pwd=bGRGWDlWWFJIL1hlaGNXVWFlTjZQZz09", " ~ воронцов бд"],
    ["Белов Никита Вадимович", "n.v.belov@mtuci.ru", "Технологии базы данных л.р.",
     "https://us04web.zoom.us/j/6771401873?pwd=QUU3ZTRaRnhZSnR1eHFMbTc2Rzg5dz09", " ~ бд белоу"],
    ["Верба Вера Алексеевна", "verba@list.ru", "ТАУ",
     "https://us04web.zoom.us/j/6874235879?pwd=Nnl0NmcxUlIxdFI2eElPNnBZcm8rQT09"],
    ["Ерофеева Виктория Вячеславовна", "Экология",
     "https://us04web.zoom.us/j/2823911433?pwd=VExFN1ViZWRyeS94eU5wVDc1cWhoUT09"],
    ["Корнеев Руслан", "89654416870@mail.ru", "Физическая культура", "https://lms.mtuci.ru/lms/my/",
     " ~ физра лмс"]
]

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
