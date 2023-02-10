from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations


def run():

    stations = build_station_list()
    inconsistent = inconsistent_typical_range_stations(stations)
    inconsistent_names = []

    for station in inconsistent:
        inconsistent_names.append(station.name)

    print(sorted(inconsistent_names))


if __name__ == "__main__":
    run()
