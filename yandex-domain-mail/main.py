# -*- coding: utf-8 -*-
import requests
import json


class DomainMail(object):

    api_url = 'https://pddimp.yandex.ru/api2/admin/'   #ссылка доступа к API

    def __init__(self, token, domain):
        """
        :param token: токен выданный яндексом
        :param domain: домен
        """
        self.headers = {'PddToken': token}
        self.domain = domain
        self.domain_info()

    def api_method(self, method, values=None):
        if not values:
            values = {}
        values.update({'domain': self.domain})
        request_url = self.api_url + 'email/'
        post_methods = ['add', 'del', 'edit']
        get_methods = ['list?', 'ml/list?', 'ml/subscribers?']
        if method in post_methods:
            response = requests.post(request_url+method, data=values, headers=self.headers)
        elif method in get_methods:
            response = requests.get(request_url+method, data=values, headers=self.headers)
        else:
            raise Exception("NotMethodName: ".format(method))
        return json.loads(response.text)

    def domain_info(self):
        """
        Проверяет статус регистрации домена
        :return:
        """
        request_url = self.api_url + 'domain/'
        values = {'domain': self.domain}
        response = requests.get(request_url+'registration_status?', data=values, headers=self.headers).text
        if 'bad_token' in response:
            raise Exception('Bad token!!!')
        elif 'added' in response:
            print("Домен {} зарегистрирован на yandex почте.".format(self.domain))
        else:
            raise Exception('Неизвестная ошибка')


    def create_mail(self, login, password):
        """
        Создание ящика
        :param login: логин пользователя
        :param password: пароль пользователя
        :return:
        """
        #TODO добавить проверку на существование ящика, и возвращать значение в случае успешного создания
        values = {'login': login, 'password': password}
        response = self.api_method('add', values=values)
        print(response)

    def delete_mail(self, login):
        """
        Удаление ящика
        :param login:  логин пользователя
        :return:
        """
        #TODO добавить проверку успешного удаления и существования ящика
        values = {'login': login}
        response = self.api_method('del', values=values)
        print(response)

    def edit_mail(self, login, params=None):
        """
        Метод редактирования ящика путем инъекции данных через словарь params
        :param login: логин пользователя
        :param params: параметры которые необходимо внести в профиль
        :return:
        """
        values = {'login': login}
        if params:
            values.update(params)
        response = self.api_method('edit', values=values)
        return response['account']


    def get_mails(self):
        """
        Метод получения списка почтовых ящиков
        в зависимости от количества страниц, делает дополнительные запросы к api
        для получения полного списка
        :return: список ящиков
        """
        on_page = 100
        values = {'on_page': on_page}
        response = self.api_method('list?', values=values)
        account_list = response['accounts']
        pages = response['pages']

        if pages <= 1:
            return account_list

        for page_num in range(2, pages + 1):
            values['page'] = page_num
            response = self.api_method('list?', values=values)
            account_list += response['accounts']

        return account_list


    def get_mailing_list(self):
        """
        Метод получения списков рассылки
        :return:
        """
        mailinglist = []
        response = self.api_method('ml/list?')
        for maillist in response['maillists']:
            mailinglist.append(maillist['maillist'])
        return mailinglist

    def _get_subscribers(self, maillist):
        """
        Метод получения списка подписчиков списка рассылки
        :param maillist: список рассылки
        :return: список участников рассылки
        """
        values = {'maillist': maillist}
        subscribers = []
        response = self.api_method('ml/subscribers?', values=values)
        for subscriber in response['subscribers']:
            subscribers.append(subscriber)
        return subscribers

    def get_mailing_lists_subscribers(self):
        """
        Возвращает список рассылок и подписчиков рассылок
        {рассылка: [подписчики, ...], ...}
        :return:
        """
        result = {}
        for mail_list in self.get_mailing_list():
            result[mail_list] = self._get_subscribers(mail_list)
        return result

    def _params_injection(self, params=None):
        """
        Вставляет определенные значения полей пользователю
        Используется для добавления имени, фимилии и секретного вопроса созданному пользователю
        :param params: словать значений полей(фио, секретный вопрос и т.п.)
        :return:
        """
        default = {'hintq': 'Введите ваше любимое случайное число', 'hinta': '123четыре'}
        if params:
            params.update(default)
        else:
            params = default
        print(params)
        return params

    def create_active_mail(self, login, password, params):
        """
        Создает почтовый ящик, устанавливает имя, фамилию и секретный вопрос,
        Делает запись в data.txt
        :param login:
        :param password:
        :param params:
        :return:
        """
        self.create_mail(login, password)
        self.edit_mail(login, self._params_injection(params))
        self._create_data_file(login, password, params)

    def _create_data_file(self, login, password, params):
        with open('data.txt', 'a', encoding='UTF-8') as f:
            f.write('Данные для входа в доменную почту'+'\n')
            f.write(params['iname']+' '+params['fname']+'\n')
            f.write('Логин: '+login+'@dezgp.ru'+'\n')
            f.write('Пароль: '+password+'\n')
            f.write('Ссылка для входа: yandex.ru'+'\n\n')
