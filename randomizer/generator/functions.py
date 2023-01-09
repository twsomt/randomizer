import requests
import time
import random
# критический тест на 0 лайков, 0 комментов, 0 репостов, 0 подписчиков


def get_winner():
    url = 'https://vk.com/wall-177150330_6606'
    qty_winners = 1
    token = 'vk1.a.dzBtvqC_ZKVp2adsEs5wWQ0GOKeZW3jRWgyQVri8x5XwrJ3WMqDnQswXXlt2yJZsultnd6FTqlBtllZYQAU-AEXfUR2XYMq-ujDo8ul61fHeKM285GPtopLt1DlMaZDnel-JBA8gqRwqjE3wji5RbO11GFnnYoQXufdGjU1a-S_ktRcWp_0NhJeH33DFwLQHiFiLyJ2bxtP3q2hpTVjGIQ'
    is_subscribers = True
    try:
        print('Подождите, пожалуйста. Сейчас будет происходить магия.')
        time.sleep(0.3)
        version = 5.131  # надо ли получать версию?

        def check_input_data(url, qty_winners=1):
            return 'https://vk.com/' in url and isinstance(qty_winners, int)

        def check_output_data(len_parc):
            return len_parc >= 1

        #  проверка входящих данных
        if not check_input_data(url, qty_winners):
            print('Некорректные входные данные')
            return -1

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
        print('Собираем лайки ...')
        get_likes_users()

        # притянуть комменты
        print('Собираем комменты ...')
        get_comments_users()

        # притянуть репосты
        print('Собираем репосты ...')
        get_reposts_users()

        #  проверка выходящих данных
        if not check_output_data(len(participants)):
            print('На посте отсутствует активность')
            return -1

        qty_winners = min(len(participants), qty_winners)
        # объявляем победителя
        if qty_winners == 1:
            print('Победитель найден!')
            print('Вот ссылка на его страницу:')
        else:
            print('Победители найдены!')
            print('Вот ссылки на их страницы:')


        if is_subscribers:
            res = set()
            for _ in range(len(participants)):

                id = random.sample(participants, 1)
                x = id[0]['id']
                print(x)
                
                if is_sub(x):
                    res.add(f'https://vk.com/id{x}')

                if len(res) == qty_winners:
                    break
            res = list(res)
        else:
            winner_id = random.sample(participants, qty_winners)
            res = []

            for i in range(qty_winners):
                win_id = winner_id[i]['id']
                res.append(f'https://vk.com/id{win_id}')
        return res
    except:
        print('Произошла непредвиденная ошибка')
        return -1
