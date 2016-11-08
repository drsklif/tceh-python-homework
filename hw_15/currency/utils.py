from datetime import datetime, timedelta
import requests


def get_quotes(date_to = datetime.now()):
    date_from = int((date_to - timedelta(weeks=2)).timestamp()*1000)
    date_to = int(date_to.timestamp()*1000)

    params = {
        'classcode': 'cets',
        'securcode': 'usd000utstom',
        'mode': 'demo',
        'from': date_from,
        'to': date_to
    }

    try:
        response = requests.get('https://api.bcs.ru/stockchartdata/v1', params)
        data = response.json()['data']
        return data
    except:
        print('Cant get quotes')
