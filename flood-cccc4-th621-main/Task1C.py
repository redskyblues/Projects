from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list


def run():

    stations = build_station_list()
    cambridge = (52.2053, 0.1218)
    stations_in_radius = stations_within_radius(stations, cambridge, 10)

    x = []
    for i in stations_in_radius:
        x.append(i.name)

    x.sort()
    print(x)


if __name__ == "__main__":
    run()
