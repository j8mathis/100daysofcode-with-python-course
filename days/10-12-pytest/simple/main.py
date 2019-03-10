import requests
from datetime import datetime

def get_live_data(url):
    """
    This function pulls data from a http endpoint and loads each row into a dict and adds it to a list.
    :param (string) url: http endpoint containing the data
    :return: a list of dictionaries
    """

    resp = requests.get(url)
    resp.raise_for_status()

    live_data_raw = resp.json()
    live_data_list = live_data_raw.get('stationBeanList')
    now = str(datetime.now().isoformat())

    station_data = []
    for station in live_data_list:
        station_dict = {'station_id': station.get('id'), 'latitude': station.get('latitude'),
                        'longitude': station.get('longitude'), 'status': station.get('status'),
                        'station_name': station.get('stationName'), 'available_docks': station.get('availableDocks', 0),
                        'total_docks': station.get('totalDocks', 0),
                        'available_bikes': station.get('availableBikes', 0), 'load_datetime': now}

        station_data.append(station_dict)

    return station_data

