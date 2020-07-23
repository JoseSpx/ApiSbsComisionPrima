from flask import Blueprint, request, jsonify
from app.helpers.web_scrapping import get_webpage_identifiers, get_html_from_page
from app.models.sbs_comision import SbsComision
import datetime
import json


sbs_bp = Blueprint('sbs', __name__)


@sbs_bp.route('/comision-prima', methods=['GET'])
def get_comision_prima():
    now = datetime.datetime.now()
    year = str(now.year)
    month = str(now.month)
    month = '0' + month if len(month) == 1 else month
    period = request.args.get('periodo', year + '-' + month)

    identifiers = get_webpage_identifiers(period)
    html = get_html_from_page(identifiers)
    rows = html.findAll('tr', attrs={'class': 'JER_filaContenido'})

    list_data = []
    for row in rows:
        data = row.findAll('td')
        model = SbsComision(clean_data(data[0]), clean_data(data[1]), clean_data(data[2]),
                            clean_data(data[3]), clean_data(data[4]),
                            clean_data(data[5]), clean_data(data[6]), clean_data(data[7]))
        list_data.append(model.serialize())

    response = jsonify(list_data)
    response.status_code = 200
    return response


def clean_data(data):
    data = data.string.strip()
    if data == '':
        return '0.00'
    return data.replace('%', '').replace(',', '')
