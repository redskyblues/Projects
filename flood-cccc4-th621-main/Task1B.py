from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance


def run():

    stations = build_station_list()
    cambridge = (52.2053, 0.1218)
    station_distances = stations_by_distance(stations, cambridge)

    x = []
    for a in station_distances:
        station = a[0]
        x.append((station.name, station.town, a[1]))

    closest = x[:10]
    furthest = x[-10:]
    print(closest)
    print(furthest)


if __name__ == "__main__":
    run()
