from floodsystem.station import MonitoringStation
from floodsystem.geo import (stations_by_distance, stations_within_radius, 
rivers_with_station, stations_by_river, rivers_by_station_number)
from haversine import haversine


def test_stations_by_distance():
    test = "test_text"
    s1 = MonitoringStation(test, test, test, (52.3053, -0.1218), test, test, test)
    s2 = MonitoringStation(test, test, test, (52.0053, -1.1218), test, test, test)
    s3 = MonitoringStation(test, test, test, (50.3053, -0.1218), test, test, test)

    stations = [s1, s2, s3]
    p = (52.2053, 0.1218)

    s_by_d = stations_by_distance(stations, p)
    for i in range(len(s_by_d) - 1):
        assert s_by_d[i + 1][1] >= s_by_d[i][1]


def test_stations_within_radius():
    test = "test_text"
    s1 = MonitoringStation(test, test, test, (52.3053, -0.1218), test, test, test)
    s2 = MonitoringStation(test, test, test, (52.0053, -1.1218), test, test, test)
    s3 = MonitoringStation(test, test, test, (50.3053, -0.1218), test, test, test)

    stations = [s1, s2, s3]
    p = (52.2053, 0.1218)
    r = 100

    s_w_r = stations_within_radius(stations, p, r)
    assert s_w_r == [s1, s2]


def test_rivers_with_station():
    test = "test_text"
    s1 = MonitoringStation(test, test, test, test, test, "River1", test)
    s2 = MonitoringStation(test, test, test, test, test, "River2", test)
    s3 = MonitoringStation(test, test, test, test, test, "River3", test)

    stations = [s1, s2, s3]
    r_w_s = rivers_with_station(stations)
    assert isinstance(r_w_s, set)
    assert r_w_s == {"River1", "River2", "River3"}


def test_stations_by_river():
    test = "test_text"
    s1 = MonitoringStation(test, test, "Station1", test, test, "River1", test)
    s2 = MonitoringStation(test, test, "Station2", test, test, "River1", test)
    s3 = MonitoringStation(test, test, "Station3", test, test, "River2", test)
    s4 = MonitoringStation(test, test, "Station4", test, test, "River3", test)
    s5 = MonitoringStation(test, test, "Station5", test, test, "River3", test)

    stations = [s1, s2, s3, s4, s5]
    s_b_r = stations_by_river(stations)
    assert isinstance(s_b_r, dict)
    assert s_b_r["River1"] == ["Station1", "Station2"]
    assert s_b_r["River2"] == ["Station3"]
    assert s_b_r["River3"] == ["Station4", "Station5"]


def test_rivers_by_station_number():
    test = "test_text"
    s1 = MonitoringStation(test, test, "Station1", test, test, "River1", test)
    s2 = MonitoringStation(test, test, "Station2", test, test, "River1", test)
    s3 = MonitoringStation(test, test, "Station3", test, test, "River1", test)
    s4 = MonitoringStation(test, test, "Station4", test, test, "River2", test)
    s5 = MonitoringStation(test, test, "Station5", test, test, "River2", test)
    s6 = MonitoringStation(test, test, "Station6", test, test, "River3", test)
    s7 = MonitoringStation(test, test, "Station7", test, test, "River3", test)
    s8 = MonitoringStation(test, test, "Station8", test, test, "River4", test)

    stations = [s1, s2, s3, s4, s5, s6, s7, s8]
    r_s_n = rivers_by_station_number(stations, 2)
    assert r_s_n == [('River1', 3), ('River2', 2), ('River3', 2)]
