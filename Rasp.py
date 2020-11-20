import datetime
import numpy as np


class Rasp:
    shed = np.array([[
        ["Понедельник",
         "|09:30-11:05| Программная инженирия л.р.\nhttps://us04web.zoom.us/j/5417715940?pwd=S3dEY2VvKzR6eHA5NWs3cDFFa3F0UT09",
         "|11:20-12:55| Программная инженирия л.р. \nhttps://us04web.zoom.us/j/5417715940?pwd=S3dEY2VvKzR6eHA5NWs3cDFFa3F0UT09",
         "|13:10-14:45| Цифровые технологии Smart City л.р. \n`the link is missing",
         "|15:25-17:00| -----",
         "|17:15-18:50| Физическая культура ДО \nlms.mtuci.ru/lms/mod/bigbluebuttonbn/view.php?id=16886&group=0"],
        ["Вторник (дистанционно)",
         "|09:30-11:05| Технологии нечеткого управления лек.\nhttps://us04web.zoom.us/j/4678454922?pwd=dXlCK1B0OXVJVzg5QTdyQ0VKNGZwdz09",
         "|11:20-12:55| ----Сетевые технологии лек.\nhttps://us04web.zoom.us/j/4678454922?pwd=dXlCK1B0OXVJVzg5QTdyQ0VKNGZwdz09",
         "|13:10-14:45| Цифровые технологии пр.з. \n`the link is missing",
         "|15:25-17:00| Микропроцессоры в РСУ пр.з. \n`the link is missing",
         "|17:15-18:50| Технология Базы Данных лек.\nhttps://us02web.zoom.us/j/78142002672?pwd=bGRGWDlWWFJIL1hlaGNXVWFlTjZQZz09"],
        ["Среда",
         "|09:30-11:05| Сетевые технологии лаб. \nhttps://us04web.zoom.us/j/4678454922?pwd=dXlCK1B0OXVJVzg5QTdyQ0VKNGZwdz09",
         "|11:20-12:55| Технологии нечеткого управления лаб. \nhttps://us04web.zoom.us/j/4678454922?pwd=dXlCK1B0OXVJVzg5QTdyQ0VKNGZwdz09",
         "|13:10-14:45| Технология баз данных лаб. \nhttps://us04web.zoom.us/j/6771401873?pwd=QUU3ZTRaRnhZSnR1eHFMbTc2Rzg5dz09",
         "|15:25-17:00| -----",
         "|17:15-18:50| -----"],
        ["Четверг (дистанционно)",
         "|09:30-11:05| ТНУ пр.з.\nhttps://us04web.zoom.us/j/4678454922?pwd=dXlCK1B0OXVJVzg5QTdyQ0VKNGZwdz0'",
         "|11:20-12:55| ТАУ л.р.\nhttps://us04web.zoom.us/j/6874235879?pwd=Nnl0NmcxUlIxdFI2eElPNnBZcm8rQT09",
         "|13:10-14:45| ТАУ лек.\nhttps://us04web.zoom.us/j/6874235879?pwd=Nnl0NmcxUlIxdFI2eElPNnBZcm8rQT09",
         "|15:25-17:00| Физическая культура\nlms.mtuci.ru/lms/mod/bigbluebuttonbn/view.php?id=16886&group=0",
         "|17:15-18:50| -----"],
        ["Пятница (дистанционно)",
         "|09:30-11:05| Экология л.р.\nhttps://us04web.zoom.us/j/2823911433?pwd=VExFN1ViZWRyeS94eU5wVDc1cWhoUT09",
         "|11:20-12:55| Экология л.р.\nhttps://us04web.zoom.us/j/2823911433?pwd=VExFN1ViZWRyeS94eU5wVDc1cWhoUT09",
         "|13:10-14:45| Микропроцессоры в РСУ л.р. \n`the link is missing",
         "|15:25-17:00| Микропроцессоры в РСУ л.р. \n`the link is missing",
         "|17:15-18:50| -----"],
        ["Суббота (дистанционно)",
         "|09:30-11:05| Программная инженерия лек.\nhttps://us04web.zoom.us/j/5417715940?pwd=S3dEY2VvKzR6eHA5NWs3cDFFa3F0UT09",
         "|11:20-12:55| -----",
         "|13:10-14:45| Экология лек.\nhttps://us04web.zoom.us/j/2823911433?pwd=VExFN1ViZWRyeS94eU5wVDc1cWhoUT09",
         "|15:25-17:00| Микропроцессоры в РСУ лек. \n`the link is missing",
         "|17:15-18:50| -----"]],
        [["Понедельник",
          "|09:30-11:05| -----",
          "|11:20-12:55| -----",
          "|13:10-14:45| Цифровые технологии Smart City л.р. \n`the link is missing",
          "|15:25-17:00| -----",
          "|17:15-18:50| Физическая культура ДО\n https://lms.mtuci.ru/lms/my/"],
         ["Вторник (дистанционно)",
          "|09:30-11:05| Цифровые технологии Smart City лек. \n`the link is missing",
          "|11:20-12:55| Сетевые технологии лек.\nhttps://us04web.zoom.us/j/4678454922?pwd=dXlCK1B0OXVJVzg5QTdyQ0VKNGZwdz09",
          "|13:10-14:45| Программная инженерия пр.з\nhttps://us04web.zoom.us/j/5417715940?pwd=S3dEY2VvKzR6eHA5NWs3cDFFa3F0UT09",
          "|15:25-17:00| Микропроцессоры в РСУ пр.з \n`the link is missing",
          "|17:15-18:50| Технология Базы Данных лек.\nhttps://us02web.zoom.us/j/78142002672?pwd=bGRGWDlWWFJIL1hlaGNXVWFlTjZQZz09"],
         ["Среда",
          "|09:30-11:05| -----",
          "|11:20-12:55| Технологии нечеткого управления л.р.\nhttps://us04web.zoom.us/j/4678454922?pwd=dXlCK1B0OXVJVzg5QTdyQ0VKNGZwdz09",
          "|13:10-14:45| Технология баз данных л.р. \nhttps://us04web.zoom.us/j/6771401873?pwd=QUU3ZTRaRnhZSnR1eHFMbTc2Rzg5dz09",
          "|15:25-17:00| -----",
          "|17:15-18:50| -----"],
         ["Четверг (дистанционно)",
          "|09:30-11:05| ТАУ пр.з.\nhttps://us04web.zoom.us/j/6874235879?pwd=Nnl0NmcxUlIxdFI2eElPNnBZcm8rQT09",
          "|11:20-12:55| ТАУ л.р.\nhttps://us04web.zoom.us/j/6874235879?pwd=Nnl0NmcxUlIxdFI2eElPNnBZcm8rQT09",
          "|13:10-14:45| ТАУ лек.\nhttps://us04web.zoom.us/j/6874235879?pwd=Nnl0NmcxUlIxdFI2eElPNnBZcm8rQT09",
          "|15:25-17:00| Физическая культура\nlms.mtuci.ru/lms/mod/bigbluebuttonbn/view.php?id=16886&group=0",
          "|17:15-18:50| -----"],
         ["Пятница (дистанционно)",
          "|09:30-11:05| -----",
          "|11:20-12:55| -----",
          "|13:10-14:45| Технология Базы Данных пр.з.\nhttps://us04web.zoom.us/j/6771401873?pwd=QUU3ZTRaRnhZSnR1eHFMbTc2Rzg5dz09",
          "|15:25-17:00| Технология Базы Данных пр.з.\nhttps://us04web.zoom.us/j/6771401873?pwd=QUU3ZTRaRnhZSnR1eHFMbTc2Rzg5dz09",
          "|17:15-18:50| -----"],
         ["Суббота (дистанционно)",
          "|09:30-11:05| Программная инженерия лек.\nhttps://us04web.zoom.us/j/5417715940?pwd=S3dEY2VvKzR6eHA5NWs3cDFFa3F0UT09",
          "|11:20-12:55| -----",
          "|13:10-14:45| Экология лек.\nhttps://us04web.zoom.us/j/2823911433?pwd=VExFN1ViZWRyeS94eU5wVDc1cWhoUT09",
          "|15:25-17:00| Микропроцессоры в РСУ лек. \n`the link is missing",
          "|17:15-18:50| -----"]]
    ])

    dday = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "неделя", "2 - неделя",
            "пн", "вт", "ср", "чт", "пт", "сб",
            "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "week",
            "сегодня", "завтра"]

    teachers = ["Шукенбаев Айрат Бисенгалеевич\nshukenbaev@mail.ru\nПрограммная инженирия\n https://us04web.zoom.us/j/5417715940?pwd=S3dEY2VvKzR6eHA5NWs3cDFFa3F0UT09~ПИ Щука",
                "Безумнов Данил Николаевич\nd.n.bezumnov@mtuci.ru\nЦифровые технологии Smart City\nМикропроцессоры в РСУ\nthe link is missing~Безумноу смарт сити",
                "Ларин Александр Иванович\na.i.larin@mtuci.ru\nТехнологии нечеткого управление\nСетевые технологии\nhttps://us04web.zoom.us/j/4678454922?pwd=dXlCK1B0OXVJVzg5QTdyQ0VKNGZwdz09#ТНУ",
                "Воронов Вячеслав Игоревич\nТехнологии базы данных\nhttps://us02web.zoom.us/j/78142002672?pwd=bGRGWDlWWFJIL1hlaGNXVWFlTjZQZz09~воронцов бд",
                "Белов Никита Вадимович\nn.v.belov@mtuci.ru\nТехнологии базы данных л.р.\nhttps://us04web.zoom.us/j/6771401873?pwd=QUU3ZTRaRnhZSnR1eHFMbTc2Rzg5dz09~бд белоу",
                "Верба Вера Алексеевна\nverba@list.ru\nТАУ\nhttps://us04web.zoom.us/j/6874235879?pwd=Nnl0NmcxUlIxdFI2eElPNnBZcm8rQT09",
                "Ерофеева Виктория Вячеславовна\nЭкология\nhttps://us04web.zoom.us/j/2823911433?pwd=VExFN1ViZWRyeS94eU5wVDc1cWhoUT09~эко",
                "Корнеев Руслан Кто то тамович\n89654416870@mail.ru\nФизическая культура\nhttps://lms.mtuci.ru/lms/my/~физра физ ра лмс"]

    def teacher(name):
        for i in Rasp.teachers:
            if name in i.lower():
                return (i.split("~")[0])


    def day(x, y):
        a = ''
        for i in Rasp.shed[x, y, 0::]:
            if not '--' in i:
                a += i.split("\n")[0] + '\n'
        return a

    def tomorrow(x, y):
        a = ''
        if y == 6:
            y = 0
        elif y == 5:
            return "Завтра у тебя выходной)"
        for i in Rasp.shed[x, y, 0::]:
            if not '--' in i:
                a += i.split("\n")[0] + '\n'
        return a

    def week(x):
        y = 0
        a = ''
        while y < 6:
            for i in Rasp.shed[x, y, 0::]:
                if not '--' in i:
                    a += i.split("\n")[0] + '\n'
            y += 1
            a += '\n'
        return a

    @staticmethod
    def twoWeek():
        x = 0
        y = 0
        a = ''
        while x < 2:
            a += '\n ' + '`````````````````````````' + '\n '
            while y < 6:
                for i in Rasp.shed[x, y, 0::]:
                    if not '--' in i:
                        a += i.split("\n")[0] + '\n'
                y += 1
                a += '\n'
            x += 1
            y = 0
        return a




    def weekday(message):
        date = datetime.datetime.today() + datetime.timedelta(hours=3)
        week = date.isocalendar()[1] % 2
        day = date.weekday()

        if message == Rasp.dday[0] or message == Rasp.dday[8] or message == Rasp.dday[14]:
            return Rasp.day(week, 0)
        elif message == Rasp.dday[1] or message == Rasp.dday[9] or message == Rasp.dday[15]:
            return Rasp.day(week, 1)
        elif message == Rasp.dday[2] or message == Rasp.dday[10] or message == Rasp.dday[16]:
            return Rasp.day(week, 2)
        elif message == Rasp.dday[3] or message == Rasp.dday[11] or message == Rasp.dday[17]:
            return Rasp.day(week, 3)
        elif message == Rasp.dday[4] or message == Rasp.dday[12] or message == Rasp.dday[18]:
            return Rasp.day(week, 4)
        elif message == Rasp.dday[5] or message == Rasp.dday[13] or message == Rasp.dday[19]:
            return Rasp.day(week, 5)
        elif message == Rasp.dday[6] or message == Rasp.dday[20]:
            return Rasp.week(week)
        elif message == Rasp.dday[7]:
            if week == 0:
                week = 1
            else:
                week = 0
            return Rasp.week(week)
        elif message.lower() == Rasp.dday[21]:
            if day == 6:
                return "Сегодня у тебя выходной)"
            return Rasp.day(week, day)
        elif message.lower() == Rasp.dday[22]:
            day+=1
            if day == 6:
                return "Завтра у тебя выходной)"
            elif day == 7:
                day = 0
            return Rasp.day(week, day)










