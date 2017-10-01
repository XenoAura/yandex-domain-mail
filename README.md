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
```python
create_mail(login, password)
```
Удаление ящика
```python
delete_mail(login)
```
Изменение атрибутов пользователя(фио, секретный вопрос и т.п.) полный список:

https://tech.yandex.ru/pdd/doc/reference/email-edit-docpage/
```python
edit_mail(login, args)
```
Получение списка всех ящиков домена
```python
get_mails()
```
Получение всех рассылок домена
```python
get_mailing_list()
```
Получение всех списков рассылок и участников в них.
```python
get_mailing_lists_subscribers()
```
Создание ящика и заполнение его информацией(фио, секретный вопрос и т.п.)

params передается в виде словаря: {'iname': 'Иванов', 'fname': 'Иван'}
```python
create_active_mail(login, password, params)
```

Методы для работы с DNS
----
Подробности о работе с DNS в yandex.pdd можно прочитать в документации:

https://tech.yandex.ru/pdd/doc/concepts/api-dns-docpage/


Получение списка всех DNS-записей домена
```python
get_dns_records()
```
Удаление DNS записи
```python
delete_dns_record(record_id)
```
Добавление DNS записи
```python
add_dns_record(record_id, **kwargs)
```
Редактирование DNS записи
```python
edit_dns_record(record_id, **kwargs)
```


По всем вопросам:
https://t.me/XenoAura
