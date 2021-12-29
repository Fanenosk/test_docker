import requests


def get_quote():
    host = 'https://favqs.com/api/qotd'
    headers = {'authorization': '75d736f00e07d2d418cf67cb144f832f',
               'content-type': 'application/json'}

    response = requests.get(url=host).json()
    return response['quote']['body']


if __name__ == '__main__':
    quote = get_quote()