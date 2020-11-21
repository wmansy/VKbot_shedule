import datetime
import numpy as np

shed = np.array([[
    ["Понедельник",
     "|09:30-11:05| Программная инженирия л.р.\nhttps://us04web.zoom.us/j/5417715940?pwd=S3dEY2VvKzR6eHA5NWs3cDFFa3F0UT09",
     "|11:20-12:55| Программная инженирия л.р. \nhttps://us04web.zoom.us/j/5417715940?pwd=S3dEY2VvKzR6eHA5NWs3cDFFa3F0UT09",
     "|13:10-14:45| Цифровые технологии Smart City л.р. \n--",
     "|15:25-17:00| -----",
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
     "|09:30-11:05| ТНУ пр.з.\nhttps://us04web.zoom.us/j/4678454922?pwd=dXlCK1B0OXVJVzg5QTdyQ0VKNGZwdz0'",
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
      "|15:25-17:00| -----",
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
    "Шукенбаев Айрат Бисенгалеевич\nshukenbaev@mail.ru\nПрограммная инженирия\nhttps://us04web.zoom.us/j/5417715940?pwd=S3dEY2VvKzR6eHA5NWs3cDFFa3F0UT09~ПИ Щука",
    "Безумнов Данил Николаевич\nd.n.bezumnov@mtuci.ru\nЦифровые технологии Smart City\nМикропроцессоры в РСУ\nthe link is missing~Безумноу смарт сити",
    "Ларин Александр Иванович\na.i.larin@mtuci.ru\nТехнологии нечеткого управление\nСетевые технологии\nhttps://us04web.zoom.us/j/4678454922?pwd=dXlCK1B0OXVJVzg5QTdyQ0VKNGZwdz09#ТНУ",
    "Воронов Вячеслав Игоревич\nТехнологии базы данных\nhttps://us02web.zoom.us/j/78142002672?pwd=bGRGWDlWWFJIL1hlaGNXVWFlTjZQZz09~воронцов бд",
    "Белов Никита Вадимович\nn.v.belov@mtuci.ru\nТехнологии базы данных л.р.\nhttps://us04web.zoom.us/j/6771401873?pwd=QUU3ZTRaRnhZSnR1eHFMbTc2Rzg5dz09~бд белоу",
    "Верба Вера Алексеевна\nverba@list.ru\nТАУ\nhttps://us04web.zoom.us/j/6874235879?pwd=Nnl0NmcxUlIxdFI2eElPNnBZcm8rQT09",
    "Ерофеева Виктория Вячеславовна\nЭкология\nhttps://us04web.zoom.us/j/2823911433?pwd=VExFN1ViZWRyeS94eU5wVDc1cWhoUT09~эко",
    "Корнеев Руслан Кто то тамович\n89654416870@mail.ru\nФизическая культура\nhttps://lms.mtuci.ru/lms/my/~физра физ ра лмс"]
dayWeek = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "неделя", "2 - неделя",
           "пн", "вт", "ср", "чт", "пт", "сб",
           "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "week",
           "сегодня", "завтра"]


def teacher(name):
    for i in teachers:
        if name in i.lower():
            return i.split("~")[0]


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
        return day(weekNum, dayNum)


if __name__ == '__main__':
    a = weekday('2 - неделя')
    date = datetime.datetime.today() + datetime.timedelta(hours=3)
    #a = date.isocalendar()[1] % 2
    print(a)
