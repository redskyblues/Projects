from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level


def test_stations_level_over_threshold():
    test = "test_text"
    s1 = MonitoringStation(test, test, test, test, (-5, 5), test, test)
    s2 = MonitoringStation(test, test, test, test, (-5, 5), test, test)
    s3 = MonitoringStation(test, test, test, test, (-5, 5), test, test)
    s4 = MonitoringStation(test, test, test, test, (-5, 5), test, test)
    s5 = MonitoringStation(test, test, test, test, (-5, 5), test, test)
    s1.latest_level = 2
    s2.latest_level = -2
    s3.latest_level = 6
    s4.latest_level = 20
    s5.latest_level = 25
    stations = [s1, s2, s3, s4, s5]

    l_o_t = stations_level_over_threshold(stations, 1.2)
    assert (s4, 2.5) in l_o_t
    assert (s5, 3.0) in l_o_t


def test_stations_highest_rel_level():
    test = "test_text"
    s1 = MonitoringStation(test, test, test, test, (-5, 5), test, test)
    s2 = MonitoringStation(test, test, test, test, (-5, 5), test, test)
    s3 = MonitoringStation(test, test, test, test, (-5, 5), test, test)
    s4 = MonitoringStation(test, test, test, test, (-5, 5), test, test)
    s5 = MonitoringStation(test, test, test, test, (-5, 5), test, test)
    s1.latest_level = 2
    s2.latest_level = -2
    s3.latest_level = 30
    s4.latest_level = 10
    s5.latest_level = 25
    stations = [s1, s2, s3, s4, s5]

    h_r_l = stations_highest_rel_level(stations, 4)

    assert h_r_l == [s3, s5, s4, s1]
