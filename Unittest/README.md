## Домашнее задание к лекции 4. «Tests»

### **_Задача №1 unit-tests_**

Из курса «Python: программирование на каждый день и сверхбыстрое прототипирование» необходимо протестировать программу 
по работе с бухгалтерией [Лекции 2.1](https://github.com/FirstSingleheart/Module-3---Professional-work-with-Python/blob/master/Unittest/src.py). 

- Следует протестировать основные функции по получению информации о документах, добавлении и удалении элементов из словаря.

#### _**Рекомендации по тестам.**_

1. Если у вас в функциях информация выводилась `print`, то теперь её лучше возвращать `return` чтобы можно было протестировать.
2. `input` можно "замокать" с помощью `unittest.mock.patch`, если с этим будут проблемы, то лучше переписать функции так, 
чтобы данные приходили через параметры.

- ### [_Решение Задачи № 1_](https://github.com/FirstSingleheart/Module-3---Professional-work-with-Python/blob/master/Unittest/Test_SRC.py)
- ### [_Альтернативное Решение Задачи № 1_](https://github.com/FirstSingleheart/Module-3---Professional-work-with-Python/blob/master/Unittest/Test_alt._src.py)

### **_Задача №2 Автотест API Яндекса_**

Проверим правильность работы `Яндекс.Диск REST API`. Написать тесты, проверяющие создание папки на Диске.
Используя библиотеку `requests` напишите `unit-test` на верный ответ и возможные отрицательные тесты на ответы с ошибкой.

Пример положительных тестов:


- _Код ответа соответствует 200._
- _Результат создания папки - папка появилась в списке файлов._

- ### [_Решение Задачи № 2_](https://github.com/FirstSingleheart/Module-3---Professional-work-with-Python/blob/master/Unittest/Test_Yandex_service.py)

### _**Задача №3. Дополнительная (не обязательная)**_

Применив `selenium`, напишите `unit-test` для авторизации на Яндексе по **_url_**: https://passport.yandex.ru/auth/

**Домашнее задание сдается ссылкой на репозиторий [BitBucket](https://bitbucket.org/) или [GitHub](https://github.com/)**