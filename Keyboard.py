from vk_api.keyboard import VkKeyboard, VkKeyboardColor

def start():
    '''
    Blue - RIMARY
    Red - NEGATIVE
    Green - POSITIVE
    White - SECONDARY
    '''

    keyboard1 = VkKeyboard(one_time=False)

    keyboard1.add_button('info', color=VkKeyboardColor.POSITIVE)
    keyboard1.add_button('Расписание', color=VkKeyboardColor.PRIMARY)
    keyboard1.add_button('Преподаватели', color=VkKeyboardColor.PRIMARY)
    keyboard1.add_line()
    keyboard1.add_button('Подписаться на рассылку расписания', color=VkKeyboardColor.PRIMARY)
    keyboard1.add_line()
    keyboard1.add_button('Отказаться от рассылки', color=VkKeyboardColor.NEGATIVE)

    return keyboard1


def weekday():
    keyboard2 = VkKeyboard(one_time=False)

    keyboard2.add_button('Понедельник', color=VkKeyboardColor.SECONDARY)
    keyboard2.add_button('Вторник', color=VkKeyboardColor.SECONDARY)
    keyboard2.add_button('Среда', color=VkKeyboardColor.SECONDARY)
    keyboard2.add_line()
    keyboard2.add_button('Четверг', color=VkKeyboardColor.SECONDARY)
    keyboard2.add_button('Пятница', color=VkKeyboardColor.SECONDARY)
    keyboard2.add_button('Суббота', color=VkKeyboardColor.SECONDARY)
    keyboard2.add_line()
    keyboard2.add_button('Неделя', color=VkKeyboardColor.PRIMARY)
    keyboard2.add_button('2 - неделя', color=VkKeyboardColor.PRIMARY)
    keyboard2.add_button('<-', color=VkKeyboardColor.POSITIVE)

    return keyboard2


def today():
    keyboard3 = VkKeyboard(one_time=False)

    keyboard3.add_button('Сегодня', color=VkKeyboardColor.SECONDARY)
    keyboard3.add_button('Завтра', color=VkKeyboardColor.SECONDARY)
    keyboard3.add_line()
    keyboard3.add_button('Неделя', color=VkKeyboardColor.PRIMARY)
    keyboard3.add_button('#', color=VkKeyboardColor.PRIMARY)
    keyboard3.add_button('->', color=VkKeyboardColor.POSITIVE)

    return keyboard3
