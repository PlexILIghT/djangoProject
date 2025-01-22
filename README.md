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
- Под юзеров выделено отдельное приложение user, где я определил модель (на основе джанговского юзера), добавил ссыли для регистрации (включив джанговские приколюхи).
Для каждой операции реализован отдельный эндпоинт:
/register - C
/login - R
/profile - R, U
/delete - D

## Задача 5. TODO.
Это что, мне теперь и API для него писать?


..Прочитав задание, у меня было двоякое чувство. А что именно нужно:
- CRUD как для API? То есть ссылки, которыми будет пользоваться приложение/админ с нужными правами доступа. Но такое уже реализовано в админке. Там можно и удалить, и добавить, и изменить пользователя. Как-то странно делать то, что уже есть. Да, это немного другое, тут API, но мы же делаем сайт? Ну да, в теории, это учебный проект, и полезно будет и API написать, но и в крупных проетах всё построено на API. Ладно, хорош рассуждений. Всё равно это сейчас никто не увидит, писать надо.