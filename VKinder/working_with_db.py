import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from VK_Auth_group import group_token
from random import randrange
import sqlalchemy as sq
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError, InvalidRequestError

# Подключение к БД
Base = declarative_base()
engine = sq.create_engine('postgresql://user@localhost:5432/vkinder_db', client_encoding='utf8')
Session = sessionmaker(bind=engine)

# Для работы с ВК
vk = vk_api.VkApi(token=group_token)
longpoll = VkLongPoll(vk)

# Для работы с БД
session = Session()
connection = engine.connect()


# Пользователь бота ВК
class User(Base):
    __tablename__ = 'user'
    id = sq.Column(sq.Integer, primary_key=True, autoincrement=True)
    vk_id = sq.Column(sq.Integer, unique=True)


# Анкеты добавленные в избранное
class DatingUser(Base):
    __tablename__ = 'dating_user'
    id = sq.Column(sq.Integer, primary_key=True, autoincrement=True)
    vk_id = sq.Column(sq.Integer, unique=True)
    first_name = sq.Column(sq.String)
    second_name = sq.Column(sq.String)
    city = sq.Column(sq.String)
    link = sq.Column(sq.String)
    id_user = sq.Column(sq.Integer, sq.ForeignKey('user.id', ondelete='CASCADE'))


# Фото избранных анкет
class Photos(Base):
    __tablename__ = 'photos'
    id = sq.Column(sq.Integer, primary_key=True, autoincrement=True)
    link_photo = sq.Column(sq.String)
    count_likes = sq.Column(sq.Integer)
    id_dating_user = sq.Column(sq.Integer, sq.ForeignKey('dating_user.id', ondelete='CASCADE'))


# Анкеты в черном списке
class BlackList(Base):
    __tablename__ = 'black_list'
    id = sq.Column(sq.Integer, primary_key=True, autoincrement=True)
    vk_id = sq.Column(sq.Integer, unique=True)
    first_name = sq.Column(sq.String)
    second_name = sq.Column(sq.String)
    city = sq.Column(sq.String)
    link = sq.Column(sq.String)
    link_photo = sq.Column(sq.String)
    count_likes = sq.Column(sq.Integer)
    id_user = sq.Column(sq.Integer, sq.ForeignKey('user.id', ondelete='CASCADE'))


"""
ФУНКЦИИ РАБОТЫ С БД
"""


# Удаление анкеты из черного списка
def delete_db_blacklist(ids):
    current_user = session.query(BlackList).filter_by(vk_id=ids).first()
    session.delete(current_user)
    session.commit()


# Удаление анкеты из избранного
def delete_db_favorites(ids):
    current_user = session.query(DatingUser).filter_by(vk_id=ids).first()
    session.delete(current_user)
    session.commit()


# проверка регистрации пользователя бота в БД
def check_db_master(ids):
    current_user_id = session.query(User).filter_by(vk_id=ids).first()
    return current_user_id


# проверка наличие анкеты в бд
def check_db_user(ids):
    dating_user = session.query(DatingUser).filter_by(vk_id=ids).first()
    blocked_user = session.query(BlackList).filter_by(vk_id=ids).first()
    return dating_user, blocked_user


# Проверка наличия пользователя в черном списке
def check_db_black(ids):
    current_users_id = session.query(User).filter_by(vk_id=ids).first()
    # Находим все анкеты в черном списке, которые добавил пользователь
    all_blacklist_users = session.query(BlackList).filter_by(id_user=current_users_id).all()
    return all_blacklist_users


# Проверка наличия анкеты в избранном
def check_db_favorites(ids):
    current_users_id = session.query(User).filter_by(vk_id=ids).first()
    # Находим все анкеты в избранном, которые добавил пользователь
    all_favorites_users = session.query(DatingUser).filter_by(id_user=current_users_id).all()
    return all_favorites_users


# Отправка сообщения пользователю
def write_msg(user_id, message, attachment=None):
    vk.method('messages.send',
              {'user_id': user_id,
               'message': message,
               'random_id': randrange(10 ** 7),
               'attachment': attachment})


# Регистрация пользователя
def register_user(vk_id):
    try:
        new_user = User(vk_id=vk_id)
        session.add(new_user)
        session.commit()
        return True
    except (IntegrityError, InvalidRequestError):
        return False


# Сохранение анкеты в БД
def add_user(event_id, vk_id, first_name, second_name, city, link, id_user):
    try:
        new_user = DatingUser(vk_id=vk_id,
                              first_name=first_name,
                              second_name=second_name,
                              city=city,
                              link=link,
                              id_user=id_user)
        session.add(new_user)
        session.commit()
        write_msg(event_id, 'Анкета добавлена в избранное')
        return True
    except (IntegrityError, InvalidRequestError):
        write_msg(event_id, 'Анкета уже в избранном')
        return False


# Сохранение в БД фото из добавленной анкеты
def add_user_photos(event_id, link_photo, count_likes, id_dating_user):
    try:
        new_user = Photos(link_photo=link_photo, count_likes=count_likes, id_dating_user=id_dating_user)
        session.add(new_user)
        session.commit()
        write_msg(event_id, 'Фотография сохранена в избранном')
        return True
    except (IntegrityError, InvalidRequestError):
        write_msg(event_id, 'Невозможно добавить эту фотографию (уже сохранена)')
        return False


# Добавление анкеты в черный список
def add_to_black_list(event_id, vk_id, first_name, second_name, city, link, link_photo, count_likes, id_user):
    try:
        new_user = BlackList(vk_id=vk_id,
                             first_name=first_name,
                             second_name=second_name,
                             city=city,link=link,
                             link_photo=link_photo,
                             count_likes=count_likes,
                             id_user=id_user)
        session.add(new_user)
        session.commit()
        write_msg(event_id, 'Анкета занесена в черный список')
        return True
    except (IntegrityError, InvalidRequestError):
        write_msg(event_id, 'Анкета уже в черном списке')
        return False


if __name__ == '__main__':
    Base.metadata.create_all(engine)