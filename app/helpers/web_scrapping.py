from app import app
from bs4 import BeautifulSoup
import requests


def get_webpage_identifiers(period):
    url = app.config['SBS_ROUTE']
    response = requests.get(url)
    html_info = BeautifulSoup(response.content, 'html.parser')

    view_state = html_info.find('input', {'name': '__VIEWSTATE'}).get('value')
    view_state_generator = html_info.find('input', {'name': '__VIEWSTATEGENERATOR'}).get('value')
    event_validation = html_info.find('input', {'name': '__EVENTVALIDATION'}).get('value')

    return {
        '__VIEWSTATE': view_state,
        '__VIEWSTATEGENERATOR': view_state_generator,
        '__EVENTVALIDATION': event_validation,
        'cboPeriodo': period,
        'btnConsultar': 'Buscar+Datos',
    }


def get_html_from_page(identifiers):
    url = app.config['SBS_ROUTE']
    response_new = requests.post(url, data=identifiers)
    html = BeautifulSoup(response_new.content, 'html.parser')
    table = html.find('table')
    return table
