import requests


def fetch_random_cat_image(api_key=None):
    """
    Делает запрос к TheCatAPI для получения случайного изображения кошки.
    :param api_key: Ключ API для авторизации (опционально).
    :return: Словарь с данными изображения или None в случае ошибки.
    """
    url = 'https://api.thecatapi.com/v1/images/search'
    headers = {'x-api-key': api_key} if api_key else {}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if isinstance(data, list) and data:
            return data[0]  # Возвращаем первый объект в списке
    return None
