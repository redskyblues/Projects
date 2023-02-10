# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine


def stations_by_distance(stations, p):

    distances = []

    for curr_station in stations:
        co_ord = curr_station.coord
        curr_distance = haversine(co_ord, p)
        distances.append((curr_station, curr_distance))

    return sorted_by_key(distances, 1)


def stations_within_radius(stations, centre, r):

    stations_within_radius = []

    for curr_station in stations:
        co_ord = curr_station.coord
        curr_distance = haversine(co_ord, centre)
        if curr_distance < r:
            stations_within_radius.append(curr_station)

    return stations_within_radius


def rivers_with_station(stations):
    rivers = set()
    for station in stations:
        rivers.add(station.river)
    return rivers


def stations_by_river(stations):
    stations_of_river = {}
    river_in_dict = []
    for station in stations:
        if station.river in river_in_dict:
            stations_of_river[station.river].append(station.name)
        else:
            river_in_dict.append(station.river)
            stations_of_river[station.river] = [station.name]
    return stations_of_river


def rivers_by_station_number(stations, N):
    stations_of_river = stations_by_river(stations)
    river_and_no = []
    for key in stations_of_river:
        no_stations = len(stations_of_river[key])
        river_and_no.append((key, no_stations))

    sort_by_no = sorted_by_key(river_and_no, 1, True)
    trunc_sort = sort_by_no[:N]
    total_length = N
    while sort_by_no[total_length][1] == sort_by_no[N - 1][1]:
        trunc_sort.append(sort_by_no[total_length])
        total_length += 1

    return trunc_sort
