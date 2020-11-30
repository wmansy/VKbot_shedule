import schedule
import datetime
import time
import threading

import vk_api
from vk_api.utils import get_random_id
from vk_api.longpoll import VkLongPoll, VkEventType
import bs4 as bs4
import requests

import Keyboard
import Rasp

'''
@author shaidullin
@author aaaa1231
'''


class Main(object):

    def __init__(self, token):
        vk = vk_api.VkApi(token=token)
        self.longpoll = VkLongPoll(vk)
        self.vk_api = vk.get_api()
        self.ttime = time.time()
        print("Server started")

    def send_msg(self, userId, message):
        self.vk_api.messages.send(peer_id=userId, random_id=get_random_id(), message=message)

    def send_msg_k(self, userId, keyboard, message):
        self.vk_api.messages.send(peer_id=userId, random_id=get_random_id(), keyboard=keyboard.get_keyboard(),
                                  message=message)

    def mailing(self, z):
        date = datetime.datetime.today() + datetime.timedelta(hours=3)
        weekNum = date.isocalendar()[1] % 2
        dayNum = date.weekday()
        print(date)
        if dayNum < 6:
            file = open("id.txt", "r").read().split("\n")
            for id in file:
                if id != "":
                    if z == 0:
                        self.send_msg(id, Rasp.day(weekNum, dayNum))
                    elif '--' not in Rasp.shed[weekNum, dayNum, z]:
                        if weekNum == 1 and dayNum == 0:
                            time.sleep(1600)
                        self.send_msg(id, Rasp.shed[weekNum, dayNum, z])

    def timetable(self):
        # время указано в UTC
        schedule.every().day.at("06:00").do(self.mailing, 0)
        schedule.every().day.at("06:25").do(self.mailing, 1)
        schedule.every().day.at("08:15").do(self.mailing, 2)
        schedule.every().day.at("10:05").do(self.mailing, 3)
        schedule.every().day.at("12:15").do(self.mailing, 4)
        schedule.every().day.at("14:10").do(self.mailing, 5)

        while True:
            schedule.run_pending()
            time.sleep(45)

    def waiting_msg(self):
        try:

            for event in self.longpoll.listen():
                if event.type == VkEventType.MESSAGE_NEW:
                    if event.to_me:
                        self.respond(event.user_id, str(event.text.lower()))
        except Exception as e:
            print(e)
            self.waiting_msg()

    def respond(self, user_id, msg):
        # date = (datetime.datetime.today() + datetime.timedelta(hours=3)).strftime("%d.%m.%Y.%H:%M:%S")
        print(time.ctime() + f' New message from: {user_id}\nText: {msg}')

        if msg == "начать" or msg == "start" or msg == "#":
            self.send_msg_k(user_id, Keyboard.start(), "Здравствуй, " + self.getUserName(user_id))

        elif msg == "info":
            self.send_msg(user_id, "autor @shaidulllin\n" +
                          "# Проект был создан с целью напоминаия о предстоящих парах, подпишись на рассылку, чтобы быть в курсе\n" +
                          "# Так же присутствует возможность узнавать расписание вручную, нажми на расписание\n" +
                          "# Есть возможность узнавать информацию о преподователях\n" +
                          "# Возможности бота небольшие, но вы можете это исправить")
        elif msg == "расписание" or msg == "&lt;-":
            self.send_msg_k(user_id, Keyboard.today(), "Расписание на...")

        elif msg == "-&gt;":
            self.send_msg_k(user_id, Keyboard.weekday(), "Какой день недели?")

        elif msg == "подписаться на рассылку расписания":
            if not str(user_id) in open('id.txt', 'r').read():
                open('id.txt', 'a').write(str(user_id) + "\n")
                self.send_msg(user_id, "Ты подписался на мою рассылку")
            else:
                self.send_msg(user_id, "Ты уже подписан на мою рассылку!")

        elif msg == "отказаться от рассылки":
            if str(user_id) in open('id.txt', 'r').read():
                id = open('id.txt', 'r').readlines()
                f = open('id.txt', 'w')
                for line in id:
                    if line != str(user_id) + "\n":
                        f.write(line)
                f.close()
                self.send_msg(user_id, "Я убрал тебя из рассылки")
            else:
                self.send_msg(user_id, "Чтобы отказаться от рассылки, нужно сначала на нее подписаться, дубина")

        elif msg in Rasp.dayWeek:
            self.send_msg(user_id, Rasp.weekday(msg))

        elif msg in Rasp.fullteach1() and msg !="":
            self.send_msg(user_id, Rasp.teacher(msg))

        elif msg == "преподаватели":
            self.send_msg(user_id, Rasp.fullteach())

        elif msg == "show":
            self.send_msg(user_id, open('id.txt', 'r').read())

        elif msg == '0':
            self.send_msg(user_id, '{:.9}'.format(str(datetime.timedelta(seconds=(time.time() - self.ttime)))))

        else:
            self.send_msg(user_id, "?")

        print("-------------------")

    @staticmethod
    def getUserName(user_id):
        request = requests.get("https://vk.com/id" + str(user_id))
        bs = bs4.BeautifulSoup(request.text, "html.parser")
        result = ""
        for i in list(bs.findAll("title")[0]):
            if i != '<':
                result += i
            elif i == '>':
                break
        return result.split()[0]


if __name__ == '__main__':


    bot = Main("Mytoken")

    t1 = threading.Thread(target=bot.timetable, name="timetable")
    t2 = threading.Thread(target=bot.waiting_msg, name="waiting_msg")

    t1.start()
    t2.start()
