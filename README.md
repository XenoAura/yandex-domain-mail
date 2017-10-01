# yandex-domain-mail

Библиотека для работы с API сервиса доменной почты yandex.ru

### Установка

```python
pip install yandex-domain-mail
```

### Пример

```python
from yandex_domain_mail import DomainMail
token = '<SECRET_TOKEN>'        # токен полученый от яндекс
domain = 'example.com'          # домен делегированный яндекс почте
app = DomainMail(token, domain) 
app.create_mail('логин', 'пароль') # создание ящика
app.get_mails()                 # список зарегистрированных почт

```

Методы
----

Создание ящика
`create_mail(login, password)`
Удаление ящика
`delete_mail(login)`
Получение списка доменов пользователя.
`get_domains()`
Изменение атрибутов пользователя(фио, секретный вопрос и т.п.) полный список:

https://tech.yandex.ru/pdd/doc/reference/email-edit-docpage/
`edit_mail(login, args)`
Получение списка всех ящиков домена
`get_mails()`
Получение всех рассылок домена
`get_mailing_list()`
Получение всех списков рассылок и участников в них.
`get_mailing_lists_subscribers()`
Создание ящика и заполнение его информацией(фио, секретный вопрос и т.п.)

params передается в виде словаря: {'iname': 'Иванов', 'fname': 'Иван'}
`create_active_mail(login, password, params)`

Методы для работы с DNS
----
Подробности о работе с DNS в yandex.pdd можно прочитать в документации:

https://tech.yandex.ru/pdd/doc/concepts/api-dns-docpage/


Получение списка всех DNS-записей домена
`get_dns_records()`
Удаление DNS записи
`delete_dns_record(record_id)`
Добавление DNS записи
`add_dns_record(record_id, **kwargs)`
Редактирование DNS записи
`edit_dns_record(record_id, **kwargs)`


По всем вопросам:
https://t.me/XenoAura
