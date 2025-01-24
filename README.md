# djangoProject
 
## Задача 1.
Чтобы запустить сервер для доустпа к нему устройств достаточно запустить его на порту своей машины.
```py manage.py runserver 0.0.0.0:8000```
(Что именно имелось в виду не знаю, но таким образом буквально можно выйти в массы, что ещё нужно). На локалхосте с помощью ```python manage.py runserver localhost:8000``` или 127.0.0.1:8000

## Задача 2.
/image из приложения "images" - GET запрос чтобы получить все картинки с описанием с сервера. Если залить картинки (на данный момент только через админку), то они отобразятся там со своим описанием (если дано).
/redirected - GET endpoint.

## Задача 3.
- Под него выделено отдельное приложениее "misc".

Доступ через главную страницу сайта.
Один метод task3, действующий в соответствии с типом запроса. Если метод GET, то перекинет на страницу которая скажет какой метод запроса был использован (GET). В случае POST - перекинет на страницу которая перенаправит на страницу "redirected", уже с GET запросом.

## Задача 4.
- Под юзеров выделено отдельное приложение user, где я определил модель (на основе джанговского юзера), добавил ссыли для регистрации (включив джанговские приколюхи). (url: сайт/users)
Для каждой операции реализован отдельный эндпоинт:
/register - C
/login - R
/profile - R, U
/delete - D

## Задача 5. 
- Под задание выделено приложение api. (url: сайт/api)
С ЮРЛами:
user/ - возвращает json со всеми пользователями
user/id - пользователь по айдиишнику
user/create - принимает данные с именем, почтой, паролем, создаёт пользователя и возвращает его айдишник
user/id/update - принимает PUT запрос с новыми данными на замену.
user/id/delete - удаляет пользотвателя

## Задача Картинки.
- Под них выделено отдельное приложениее images. (url: сайт/image/) - рут
Чтобы всё посмотреть, нужно залить картинку через админку.
Все картинки с возможностью лайкнуть отображаются в руте приложения.
Обработка лайков через url.
Был сделан стайлинг для профиля и галереи.
При лайке картинки счётчик поднимается. Можно убрать лайк.
Лайкнутые картинки отображаются в профиле. Там же можно и убрать лайк. Картинка пропадёт из профиля.

## Задача 8.
Я разверну в Railway по советам от друзей.