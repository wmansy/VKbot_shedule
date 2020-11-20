import schedule
import datetime
import time
import threading
import bs4 as bs4
import requests

import vk_api
from vk_api.utils import get_random_id
from vk_api.longpoll import VkLongPoll, VkEventType

import Keyboard
from Rasp import Rasp

# Авторизуемся как сообщество
vk = vk_api.VkApi(token='token')
vk_api = vk.get_api()
# Работа с сообщениями
longpoll = VkLongPoll(vk)
print("Server started")


def write_msg(id, message):
    vk_api.messages.send(peer_id=id, random_id=get_random_id(), message=message)


def send(z):
    date = datetime.datetime.today()  # + datetime.timedelta(hours=3)
    week = date.isocalendar()[1] % 2
    day = date.weekday()
    print(date)
    file = open("id.txt", "r").read().split("\n")
    for id in file:
        if id != "":
            if z == 0:
                write_msg(id, Rasp.day(week, day))
            elif not '--' in Rasp.shed[week, day, z]:
                write_msg(id, Rasp.shed[week, day, z])


def shed():
    schedule.every().day.at("06:00").do(send, 0)
    schedule.every().day.at("06:25").do(send, 1)
    schedule.every().day.at("08:15").do(send, 2)
    schedule.every().day.at("10:05").do(send, 3)
    schedule.every().day.at("12:15").do(send, 4)
    schedule.every().day.at("14:10").do(send, 5)

    while True:
        schedule.run_pending()
        time.sleep(5)


def eventt():
    try:
        while True:
            for event in longpoll.listen():
                if event.type == VkEventType.MESSAGE_NEW:
                    if event.to_me:
                        print(str(
                            datetime.datetime.today() + datetime.timedelta(
                                hours=3)) + f' New message from {event.user_id} ',
                              end='')

                        if str(event.text.lower()) == "начать" or str(event.text.lower()) == "start" or event.text == "#":
                            vk_api.messages.send(peer_id=event.user_id, random_id=get_random_id(),
                                                 keyboard=Keyboard.start().get_keyboard(),
                                                 message="Здравствуй, " + getUserName(event.user_id))
                        elif event.text == "info":
                            write_msg(event.user_id, "@ autor Mansy\n# Бот находится в режиме тестирования\n" +
                                      "# Проект был создан с целью напоминаия о предстоящих парах, подпишись на рассылку, чтобы быть в курсе\n" +
                                      "# Так же присутствует возможность узнавать расписание вручную, нажми на расписание\n" +
                                      "# Есть возможность узнавать информацию о преподователях\n" +
                                      "# Возможности бота небольшие, но вы можете это исправить")
                        elif event.text == "Расписание" or event.text == "&lt;-":
                            vk_api.messages.send(peer_id=event.user_id, random_id=get_random_id(),
                                                 keyboard=Keyboard.today().get_keyboard(),
                                                 message="Расписание на...")
                        elif event.text == "-&gt;":
                            vk_api.messages.send(peer_id=event.user_id, random_id=get_random_id(),
                                                 keyboard=Keyboard.weekday().get_keyboard(),
                                                 message="Какой день недели?")
                        elif event.text == "Подписаться на рассылку расписания":
                            if not str(event.user_id) in open('id.txt', 'r').read():
                                open('id.txt', 'a').write(str(event.user_id) + "\n")
                                write_msg(event.user_id, "Ты подписался на мою рассылку")
                            else:
                                write_msg(event.user_id, "Ты уже подписан на мою рассылку!")
                        elif event.text == "Отказаться от рассылки":
                            if str(event.user_id) in open('id.txt', 'r').read():
                                id = open('id.txt', 'r').readlines()
                                f = open('id.txt', 'w')
                                for line in id:
                                    if line != str(event.user_id) + "\n":
                                        f.write(line)
                                f.close()
                                write_msg(event.user_id, "Я убрал тебя из рассылки")
                            else:
                                write_msg(event.user_id,
                                          "Чтобы отказаться от рассылки, нужно сначала на нее подписаться, дубина")

                        elif str(event.text).lower() in Rasp.dday:
                            write_msg(event.user_id, Rasp.weekday(event.text.lower()))

                        elif str(event.text).lower() in "".join(Rasp.teachers).lower():
                            write_msg(event.user_id, Rasp.teacher(event.text.lower()))

                        elif event.text.lower() == "преподаватели":
                            write_msg(event.user_id, "Напиши мне его фамилию или предмет, который он ведет")
                        elif event.text == "show":
                            write_msg(event.user_id, open('id.txt', 'r').read())

                        print('Text: ', event.text)
                        print("-------------------")
    except Exception as e:
        print(e)
        eventt()


def getUserName(user_id):
    request = requests.get("https://vk.com/id" + str(user_id))
    bs = bs4.BeautifulSoup(request.text, "html.parser")

    user_name = cleanTag(bs.findAll("title")[0])

    return user_name.split()[0]


def cleanTag(string_line):
    result = ""
    not_skip = True
    for i in list(string_line):
        if not_skip:
            if i == "<":
                not_skip = False
            else:
                result += i
        else:
            if i == ">":
                not_skip = True

    return result


'''
class myThread1(threading.Thread):
    def init(self):
        threading.Thread.init(self)

    def run(self):
        event()


class myThread2(threading.Thread):
    def init(self):
        threading.Thread.init(self)

    def run(self):
        shed()

'''
if __name__ == '__main__':
    t = threading.Thread(target=shed, name="shed")
    t.start()

    eventt()
    '''
        # Создать потоки
    thread1 = myThread1()
    thread2 = myThread2()

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
    '''
