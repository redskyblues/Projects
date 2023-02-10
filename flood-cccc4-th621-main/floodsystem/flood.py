from .utils import sorted_by_key


def stations_level_over_threshold(stations, tol):
    over_tol = []

    for station in stations:

        if station.typical_range_consistent() and station.latest_level is not None:
            if station.relative_water_level() > tol:
                over_tol.append((station, station.relative_water_level()))
        else:
            pass

    return sorted_by_key(over_tol, 1, True)


def stations_highest_rel_level(stations, N):

    all_stations = []

    for station in stations:

        if station.typical_range_consistent() and station.latest_level is not None:
            all_stations.append((station, station.relative_water_level()))
        else:
            pass

    highest_stations = []

    for station in sorted_by_key(all_stations, 1, True)[:N]:
        highest_stations.append(station[0])

    return highest_stations
