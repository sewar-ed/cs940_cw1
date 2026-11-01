"""This module defines our Network class."""
# TODO: Implement a Network class in network.py that stores the lines, stations, and live arrival
# predictions. Your implementation should use the Heap and Trie data structures developed in
# the preceding tasks where appropriate.
# Network must implement only a ‘single source-of-truth’ for lines and stations: lines are identified by line_id and stations by station_id. Any additional structures used to support the
# queries below must remain consistent when new data is added.

from ast import Raise

from ast import Raise
from typing import List

from line import Line
from prediction import Prediction
from station import Station


class Network:
    def __init__(self):
        # TODO: initialises an empty network
        pass

    def add_line(self, line: Line) -> None:
        # TODO: adds line to the network, indexed by its line_id
        pass

    def get_line(self, line_id: str) -> Line:
        # TODO: returns the line with the given identifier.
        # Raise an appropriate exception if it is unknown
        pass

    def add_station(self, station: Station) -> None:
        # TODO: adds station to the network, indexed by its station_id, and makes its name available to station-prefix searches. Station
        # names should be indexed in a consistent normalised form so that capitalisation and punctuation do not prevent sensible matches
        pass

    def get_station(self, station_id: str) -> Station:
        # TODO: returns the station with the
        # given identifier. Raise an appropriate exception if it is unknown
        pass

    def add_prediction(self, prediction: Prediction) -> None:
        # TODO: adds a prediction and
        # updates the information needed to support each of the arrival queries below. Predictions are ordered by their time_to_station value.
        # Hint: f'{prediction.vehicle_id}{prediction.line_id}' is a unique key to identify
        # a train
        pass

    ## Implement the following query methods:##

    def search_by_prefix(self, prefix: str) -> List[Station]:
        # TODO: returns the stations for
        # which the prefix occurs at the beginning of any word in the station name. Each station
        # must occur at most once, and results must be sorted lexicographically by station_name.
        # An empty prefix returns every station;
        # Hint: there are 24 stations that match with ‘park’, 12 stations that match with ‘road’,
        # and 11 stations that match with ‘south
        pass

    def next_arrivals_by_station(self, station_id: str, k: int) -> List[Prediction]:
        # TODO: returns the next k predictions for the specified station
        pass

    def next_arrivals_by_line(self, line_id: str, k: int) -> List[Prediction]:
        # TODO: returns the next k predictions for the specified line
        pass

    def next_arrivals_by_station_and_line(self, station_id: str, line_id: str, k: int) -> List[Prediction]:
        # TODO: returns the next k predictions for the specified station
        # that belong to the specified line. Raise an appropriate exception if the station or line is
        # unknown, or if the line does not serve that station;
        pass

    def next_stations_by_train(self, vehicle_id: str, line_id: str, k: int) -> List[Prediction]:
        # TODO: returns the next k station predictions for the identified vehicle on
        # the given line
        pass

    def __repr__(self) -> str:
        # TODO: All prediction-query results must be in non-decreasing order of time_to_station and must not
        # remove or reorder predictions stored by the network. Support k = -1 to request all matching
        # predictions, k=0 to request none, and reject other negative values. A valid query with no
        # matching predictions should return an empty list. You may define private helper methods and
        # auxiliary indexes, as long as you respect the public interface previously outlined.
        # Define __repr__ that reports the number of lines and stations in the network.
        pass
