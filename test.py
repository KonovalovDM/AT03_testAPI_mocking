import pytest
from main import fetch_random_cat_image

def test_fetch_random_cat_image_success(mocker):
    mock_get = mocker.patch('main.requests.get')

    # Создаем мок-ответ для успешного запроса
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = [
        {
            'id': 'bbl',
            'url': 'https://cdn2.thecatapi.com/images/bbl.jpg',
            'width': 500,
            'height': 334
        }
    ]

    api_key = 'test_api_key'
    result = fetch_random_cat_image(api_key)

    assert result == {
        'id': 'bbl',
        'url': 'https://cdn2.thecatapi.com/images/bbl.jpg',
        'width': 500,
        'height': 334
    }

def test_fetch_random_cat_image_failure(mocker):
    mock_get = mocker.patch('main.requests.get')

    # Создаем мок-ответ для неуспешного запроса
    mock_get.return_value.status_code = 404

    api_key = 'test_api_key'
    result = fetch_random_cat_image(api_key)

    assert result is None
