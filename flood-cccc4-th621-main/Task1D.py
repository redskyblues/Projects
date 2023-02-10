from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river


def run():

    stations = build_station_list()
    stationed_river = list(rivers_with_station(stations))
    stationed_river.sort()
    print(len(stationed_river))
    print(stationed_river[:10])

    river_station = stations_by_river(stations)
    print(sorted(river_station['River Aire']))
    print(sorted(river_station['River Cam']))
    print(sorted(river_station['River Thames']))


if __name__ == "__main__":
    run()
