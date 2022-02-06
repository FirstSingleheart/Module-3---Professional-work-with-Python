import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from VK_Auth_group import group_token
from working_with_db import engine, Session, write_msg, register_user, add_user, add_user_photos, add_to_black_list, \
    check_db_user, check_db_black, check_db_favorites, check_db_master, delete_db_blacklist, delete_db_favorites
from bot_function import search_users, json_create, get_photo, sort_likes

vk = vk_api.VkApi(token=group_token)
longpoll = VkLongPoll(vk)

# Для работы с БД
session = Session()
connection = engine.connect()


def loop_bot():
    for vk_event in longpoll.listen():
        if vk_event.type == VkEventType.MESSAGE_NEW:
            if vk_event.to_me:
                message_text = vk_event.text
                return message_text, vk_event.user_id


def menu_bot(id_num):
    write_msg(id_num,
              f"Добро пожаловать в стартовое меню бота 'Vkinder'\n"
              f"Если это первый запуск - сначала нужно зарегистрироваться\n"
              f"Для регистрации введите - 'да'\n"
              f"Если вы уже зарегистрированы - можно сразу приступать к поиску анкет\n"
              f"Что-бы перейти в избранное нажмите - '2'\n"
              f"Что-бы перейти в черный список - '0'\n")


def show_info():
    write_msg(user_id, f'Это была последняя анкета.'
                       f'Перейти в избранное - 2'
                       f'Перейти в черный список - 0'
                       f'Меню бота - Vkinder')


def reg_new_user_msg(id_num):
    write_msg(id_num, 'Вы успешно зарегистрировались')
    write_msg(id_num, f"\n Vkinder - активация бота\n")
    register_user(id_num)


def go_to_favorites(ids):
    all_users = check_db_favorites(ids)
    write_msg(ids, f'Избранные анкеты:')
    for nums, users in enumerate(all_users):
        write_msg(ids, f'{users.first_name}, {users.second_name}, {users.link}')
        write_msg(ids, f'1 - Удалить анкету из избранного, 0 - Далее\n q - Выход')
        msg_texts, user_ids = loop_bot()
        if msg_texts == '0':
            if nums >= len(all_users) - 1:
                write_msg(user_ids, f'Это была последняя анкета\n'
                                    f'Vkinder - вернуться в меню\n')
        # Удаляем запись из бд "избранное"
        elif msg_texts == '1':
            delete_db_favorites(users.vk_id)
            write_msg(user_ids, f'Выполнено.')
            if nums >= len(all_users) - 1:
                write_msg(user_ids, f'Это была последняя анкета\n'
                                    f'Vkinder - вернуться в меню\n')
        elif msg_texts.lower() == 'q':
            write_msg(ids, f'\n Vkinder - активация бота\n')
            break


def go_to_blacklist(ids):
    all_users = check_db_black(ids)
    write_msg(ids, f'Анкеты в черном списке:')
    for num, user in enumerate(all_users):
        write_msg(ids, f'{user.first_name}, {user.second_name}, {user.link}')
        write_msg(ids, f'1 - Удалить анкету из черного списка, 0 - Далее \n q - Выход')
        message_text, user_ids = loop_bot()
        if message_text == '0':
            if num >= len(all_users) - 1:
                write_msg(user_ids, f'Это была последняя анкета\n'
                                    f'Vkinder - вернуться в меню\n')
        # Удаляем запись из бд "черный список"
        elif message_text == '1':
            print(user.id)
            delete_db_blacklist(user.vk_id)
            write_msg(user_ids, f'Выполнено')
            if num >= len(all_users) - 1:
                write_msg(user_ids, f'Это была последняя анкета\n'
                                    f'Vkinder - вернуться в меню\n')
        elif message_text.lower() == 'q':
            write_msg(ids, f'\n Vkinder - активация бота\n')
            break


if __name__ == '__main__':
    while True:
        msg_text, user_id = loop_bot()
        if msg_text == "VKinder":
            menu_bot(user_id)
            msg_text, user_id = loop_bot()
            # Регистрация пользователя в БД:
            if msg_text.lower() == 'да':
                reg_new_user_msg(user_id)
            # Поиск анкет:
            elif len(msg_text) > 1:
                gender = 0
                if msg_text[0:7].lower() == 'девушка':
                    gender = 1
                elif msg_text[0:7].lower() == 'мужчина':
                    gender = 2
                age_min = msg_text[8:10]
                if int(age_min) < 18:
                    write_msg(user_id, f'Вы же хотели написать 18? ведь так? Выставлен возраст - 18 лет :)')
                    age_min = 18
                age_max = msg_text[11:14]
                if int(age_max) >= 100:
                    write_msg(user_id, f'Геронтофилия? Давайте не будем заходить дальше хотя - бы 99 лет :)')
                    age_max = 99
                city = msg_text[14:len(msg_text)].lower()
                # Ищем анкеты
                profiles = search_users(gender, int(age_min), int(age_max), city)
                json_create(profiles)
                current_user_id = check_db_master(user_id)
                # Производим отбор анкет
                for human in range(len(profiles)):
                    dating_user, blocked_user = check_db_user(profiles[human][3])
                    # Получаем фото и сортируем по лайкам
                    user_photo = get_photo(profiles[human][3])
                    if user_photo == 'нет доступа к фото' or dating_user is not None or blocked_user is not None:
                        continue
                    sorted_user_photo = sort_likes(user_photo)
                    # Выводим отсортированные данные по анкетам
                    write_msg(user_id, f'\n{profiles[human][0]}  {profiles[human][1]}  {profiles[human][2]}', )
                    try:
                        write_msg(user_id, f'фото:',
                                  attachment=','.join
                                  ([sorted_user_photo[-1][1], sorted_user_photo[-2][1],
                                    sorted_user_photo[-3][1]]))
                    except IndexError:
                        for photo in range(len(sorted_user_photo)):
                            write_msg(user_id, f'фото:',
                                      attachment=sorted_user_photo[photo][1])
                    # Ждем пользовательский ввод
                    write_msg(user_id, '1 - Добавить, 2 - Заблокировать, 0 - Далее, \n q - выход из поиска')
                    msg_text, user_id = loop_bot()
                    if msg_text == '0':
                        # Проверка на последнюю запись
                        if human >= len(profiles) - 1:
                            show_info()
                    # Добавляем пользователя в избранное
                    elif msg_text == '1':
                        # Проверка на последнюю запись
                        if human >= len(profiles) - 1:
                            show_info()
                            break
                        # Пробуем добавить анкету в БД
                        try:
                            add_user(user_id, profiles[human][3], profiles[human][1],
                                     profiles[human][0], city, profiles[human][2], current_user_id.id)
                            # Пробуем добавить фото анкеты в БД
                            add_user_photos(user_id, sorted_user_photo[0][1],
                                            sorted_user_photo[0][0], current_user_id.id)
                        except AttributeError:
                            write_msg(user_id, 'Вы не зарегистрировались!\n Введите Vkinder для перезагрузки бота')
                            break
                    # Добавляем пользователя в черный список
                    elif msg_text == '2':
                        # Проверка на последнюю запись
                        if human >= len(profiles) - 1:
                            show_info()
                        # Блокируем
                        add_to_black_list(user_id, profiles[human][3], profiles[human][1],
                                          profiles[human][0], city, profiles[human][2],
                                          sorted_user_photo[0][1],
                                          sorted_user_photo[0][0], current_user_id.id)
                    elif msg_text.lower() == 'q':
                        write_msg(user_id, 'Введите Vkinder для активации бота')
                        break
            # Переходим в избранное
            elif msg_text == '2':
                go_to_favorites(user_id)
            # Переходим в черный список
            elif msg_text == '0':
                go_to_blacklist(user_id)
