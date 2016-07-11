# yandex-domain-mail
*version 0.1 alpha*

Обертка над сервисом доменной почты yandex.ru

### Установка

```python
pip install git+https://github.com/XenoAura/yandex-domain-mail.git
```

### Пример

```python
from yandex_domain_mail import DomainMail
token = '...SECRET...TOKEN...'  # токен полученый от яндекс
domain = 'example.com'          # домен делегированный яндекс почте
app = DomainMail(token, domain)
app.create_mail('логин', 'пароль') # создание ящика
app.get_mails()   # получение списка ящиков

```

Остальные методы
----
create_mail(login, password)
: Создание ящика

delete_mail(login)
: Удаление ящика

edit_mail(login, args)
: Изменение атрибутов пользователя(фио, секретный вопрос и т.п.) полный список:
: https://tech.yandex.ru/pdd/doc/reference/email-edit-docpage/

get_mails()
: Получение списка всех ящиков домена

get_mailing_list()
: Получение всех рассылок домена

get_mailing_lists_subscribers()
: Получение всех списков рассылок и участников в них.

create_active_mail(login, password, params)
: Создание ящика и заполнение его информацией(фио, секретный вопрос и т.п.)
: params передается в виде словаря: {'iname': 'Иванов', 'fname': 'Иван'}


### PS
Документация не вся.
Принимается любая помощь.

По вопросам работы библиотеки можно стучать сюда: впашке.ком/visual
