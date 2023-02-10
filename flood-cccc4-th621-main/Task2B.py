from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold


def run():
    stations = build_station_list()
    update_water_levels(stations)
    tol = 3

    level_over_tol = stations_level_over_threshold(stations, tol)

    for i in level_over_tol:
        print("{} {}" .format(i[0].name, i[1]))


if __name__ == "__main__":
    run()
