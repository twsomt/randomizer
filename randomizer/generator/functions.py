'''
коды ошибок
-1 на посте отсутствует автивность
-2 некорректные входные данные
'''

import requests
import time
import random
# критический тест на 0 лайков, 0 комментов, 0 репостов, 0 подписчиков


def get_winner(url, token, qty_winners=3, is_subscribers=True):
    '''
    Функция определяет победителя (побетелей) из поста Вконтакте
    и возвращает список:
    [
        ['айди1', 'ссылкаВК1', 'фото1', 'имя1', 'фамилия1'], # победитель1
        ['айди2', 'ссылкаВК2', 'фото2', 'имя2', 'фамилия2'], # победитель2
        ['айди3', 'ссылкаВК3', 'фото3', 'имя3', 'фамилия3'], # победитель3
        ]
    '''
    
    url = url.replace('https://m.vk.com/', 'https://vk.com/')
    time.sleep(0.3)
    version = 5.131  # надо ли получать версию?

    def check_input_data(url, qty_winners=1):
        return 'https://vk.com/' in url and isinstance(qty_winners, int)

    def check_output_data(len_parc):
        return len_parc >= 1

    #  проверка входящих данных
    if not check_input_data(url, qty_winners):
        return -2

    item_id = int(url[url.rfind('_') + 1:])
    owner_id = int(url[url.find('-'): url.rfind('_')])
    participants = []  # айди, имя, фамилия, тип участия, вес участия

    def get_likes_users():
        weigth = 1  # вес участия
        offset = 0
        while True:
            try:
                time.sleep(0.34)
                response = requests.get('https://api.vk.com/method/likes.getList',
                                        params={
                                            'access_token': token,
                                            'v': version,
                                            'type': 'post',
                                            'owner_id': owner_id,
                                            'item_id': item_id,
                                            'page_url': url,
                                            'extended': 1,
                                            'offset': offset
                                        }
                                        )

                data = response.json()['response']['items']
                if not data:  # если закончились лайки, прерываем цикл запросов
                    break
                for i in data:
                    participants.append({'id': i['id'],
                                        'first_name': i['first_name'],
                                            'last_name': i['last_name'],
                                            'type': 'like',
                                            'weigth': weigth}
                                        )
                offset += 100
            except Exception as e:
                print(e.code)
                print(e.message)

    def get_comments_users():
        weigth = 1  # вес участия
        offset = 0
        while True:
            try:
                time.sleep(0.34)
                response = requests.get('https://api.vk.com/method/wall.getComments',
                                        params={
                                            'access_token': token,
                                            'v': version,
                                            'owner_id': owner_id,
                                            'post_id': item_id,
                                            'extended': 1,
                                            'count': 100,
                                            'offset': offset
                                        }
                                        )
                data = response.json()['response']['items']
                if not data:  # если закончились комменты, прерываем цикл запросов
                    break
                for i in data:
                    participants.append({'id': i['from_id'],
                                        'first_name': 'ИмяИмя',
                                            'last_name': 'ФамилияФамилия',
                                            'type': 'comment',
                                            'weigth': weigth}
                                        )
                offset += 100
            except Exception as e:
                print(e.code)
                print(e.message)

    def get_reposts_users():
        weigth = 1  # вес участия
        offset = 0
        while True:
            try:
                time.sleep(0.34)
                response = requests.get('https://api.vk.com/method/likes.getList',
                                        params={
                                            'access_token': token,
                                            'v': version,
                                            'type': 'post',
                                            'owner_id': owner_id,
                                            'item_id': item_id,
                                            'page_url': url,
                                            'extended': 1,
                                            'offset': offset,
                                            'filter': 'copies'
                                        }
                                        )

                data = response.json()['response']['items']
                if not data:  # если закончились репосты, прерываем цикл запросов
                    break
                for i in data:
                    participants.append({'id': i['id'],
                                        'first_name': i['first_name'],
                                            'last_name': i['last_name'],
                                            'type': 'repost',
                                            'weigth': weigth}
                                        )
                offset += 100
            except Exception as e:
                print(e.code)
                print(e.message)


    def is_sub(id_user):
        try:
            time.sleep(0.34)
            response = requests.get('https://api.vk.com/method/groups.isMember',
                                        params={
                                            'access_token': token,
                                            'v': version,
                                            'group_id': abs(owner_id),
                                            'user_id': id_user,
                                        }
                                        )
            return response.json()['response']

        except Exception as e:
            print(e.code)
            print(e.message)


    # притянуть лайки
    get_likes_users()

    # притянуть комменты
    get_comments_users()

    # притянуть репосты
    get_reposts_users()

    #  проверка выходящих данных
    if not check_output_data(len(participants)):
        return -1

    # берем за основу меньшее из нужного кол-ва победителей и общего числа участников
    qty_winners = min(len(participants), qty_winners)


    # формируем список победителей без повторений
    res = set()
    for _ in range(len(participants)):

        id = random.sample(participants, 1)
        x = id[0]['id']  # вытягиваем айди из сложенного списка парципантов с доп параметрами. пока что только айди
        
        if is_subscribers:
            if is_sub(x):
                res.add(f'{x}')
        else:
            res.add(f'{x}')

        if len(res) == qty_winners:
            break
    
    # передаем список победителей дальше
    res = list(res)

    # получаем фото имена и фамилии победителей
    def get_fname_l_name_photo(res):
        time.sleep(0.34)
        response = requests.get('https://api.vk.com/method/users.get',
                                params={
                                    'access_token': token,
                                    'v': version,
                                    'user_ids': ', '.join(list(map(str, res))),
                                    'fields': 'photo_50',
                                }
                                )
        data = response.json()['response']

        res = []
        for i in data:
            res.append([value for key, value in i.items() if key in ('id', 'photo_50', 'first_name', 'last_name')])

        # добавляем в результат ссылки на страницы победителей
        for i in range(len(res)):
            res[i].insert(1, f'https://vk.com/id{res[i][0]}/')

        return res             

    return get_fname_l_name_photo(res)

# url, token, qty_winners=3, is_subscribers=True)
# тесты
# url = 'https://m.vk.com/wall-53141502_214585'
# qty_winners = 3
# is_subscribers = True

# y = get_winner(url, token, qty_winners, is_subscribers)
# if isinstance(y, list):
#     for i in y:
#         print(i)
#         print()
# else:
#     print(y)