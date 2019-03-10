from main import get_live_data

def test_answer():
    i = get_live_data('https://feeds.divvybikes.com/stations/stations.json')
    assert type([]) == type(i)

