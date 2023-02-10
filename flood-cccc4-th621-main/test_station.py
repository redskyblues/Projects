# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation, inconsistent_typical_range_stations


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town


def test_typical_range_consistent():
    test = "test_text"
    s1 = MonitoringStation(test, test, test, test, (-2.3, 3.4445), test, test)
    s2 = MonitoringStation(test, test, test, test, None, test, test)
    s3 = MonitoringStation(test, test, test, test, (2.3, -3.4445), test, test)

    assert s1.typical_range_consistent() is True
    assert s2.typical_range_consistent() is False
    assert s3.typical_range_consistent() is False


def test_inconsistent_typical_range_stations():
    test = "test_text"
    s1 = MonitoringStation(test, test, test, test, (-2.3, 3.4445), test, test)
    s2 = MonitoringStation(test, test, test, test, None, test, test)
    s3 = MonitoringStation(test, test, test, test, (2.3, -3.4445), test, test)
    s4 = MonitoringStation(test, test, test, test, (3.3, 10.4), test, test)
    s5 = MonitoringStation(test, test, test, test, None, test, test)
    s6 = MonitoringStation(test, test, test, test, (5, -5), test, test)

    stations = [s1, s2, s3, s4, s5, s6]

    i_tr = inconsistent_typical_range_stations(stations)

    assert i_tr == [s2, s3, s5, s6]


def test_relative_water_level():
    test = "test_text"
    s1 = MonitoringStation(test, test, test, test, (-2.3, 3.4445), test, test)
    s1.latest_level = 3.0
    assert round(s1.relative_water_level(), 3) == 0.923

    s2 = MonitoringStation(test, test, test, test, None, test, test)
    s2.latest_level = 3.0
    assert s2.relative_water_level() is None

    s3 = MonitoringStation(test, test, test, test, (2.3, -3.4445), test, test)
    s3.latest_level = 3.0
    assert s3.relative_water_level() is None

    s4 = MonitoringStation(test, test, test, test, (3.3, 10.4), test, test)
    s4.latest_level = 15
    assert round(s4.relative_water_level(), 3) == 1.648
