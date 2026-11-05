"""This module defines our Network class."""

from exceptions import TubeError
from heap import Heap
from line import Line
from prediction import Prediction
from station import Station
from trie import Trie


class Network:
    def __init__(self):
        """
        Initialises an empty network.
        """
        self.lines = {}
        self.stations = {}
        self.station_trie = Trie()
        # working backwards from queries we need in task 4:
        self.station_arrivals_pred = {}
        self.line_arrivals_pred = {}
        self.station_and_line_arrivals_pred = {}
        self.train_arrivals_pred = {}

    def add_line(self, line: Line) -> None:
        """
        Adds line to the network, indexed by its line_id.
        """
        self.lines[line.id] = line

    def get_line(self, line_id: str) -> Line:
        """
        Returns the line with the given identifier,
        Raises an appropriate exception if it is unknown.
        """
        if line_id in self.lines:
            return self.lines[line_id]
        raise TubeError(f"No such line: '{line_id}' in netwrok.")

    def add_station(self, station: Station) -> None:
        """
        Adds station to the network, indexed by its station_id, and makes its name available to station-prefix searches.
        """
        self.stations[station.station_id] = station
        self.station_trie.insert(station.station_name, station)

    def get_station(self, station_id: str) -> Station:
        """
        Returns the station with the given identifier,
        Raises an appropriate exception if it is unknown.
        """
        if station_id in self.stations:
            return self.stations[station_id]
        raise TubeError(f"No such station: '{station_id}' in netwrok.")

    def add_prediction(self, prediction: Prediction) -> None:
        """
        # Adds a prediction and
        # updates the information needed to support each of the arrival queries below. Predictions are ordered by their time_to_station value.
        """
        # create heap for unseen station
        if prediction.next_station_id not in self.station_arrivals_pred:
            self.station_arrivals_pred[prediction.next_station_id] = Heap()
        # add item to heap, key=time_to_station to order by it
        self.station_arrivals_pred[prediction.next_station_id].push(
            prediction.time_to_station, prediction)
        if prediction.line_id not in self.line_arrivals_pred:
            self.line_arrivals_pred[prediction.line_id] = Heap()
        self.line_arrivals_pred[prediction.line_id].push(
            prediction.time_to_station, prediction)
        if (prediction.next_station_id, prediction.line_id) not in self.station_and_line_arrivals_pred:
            self.station_and_line_arrivals_pred[(
                prediction.next_station_id, prediction.line_id)] = Heap()
        self.station_and_line_arrivals_pred[(prediction.next_station_id, prediction.line_id)].push(
            prediction.time_to_station, prediction)
        train_key = f"{prediction.vehicle_id}{prediction.line_id}"
        if train_key not in self.train_arrivals_pred:
            self.train_arrivals_pred[train_key] = Heap()
        self.train_arrivals_pred[train_key].push(
            prediction.time_to_station, prediction)

    ## Query methods:##

    def search_by_prefix(self, prefix: str) -> list[Station]:
        """
        Returns the stations for which the prefix 
        occurs at the beginning of any word in the station name.
        """
        return self.station_trie.search_by_prefix(prefix)

    def next_arrivals_by_station(self, station_id: str, k: int) -> list[Prediction]:
        """
        Returns the next k predictions for the specified station
        """
        return self.station_arrivals_pred[station_id].ksmallest(k)

    def next_arrivals_by_line(self, line_id: str, k: int) -> list[Prediction]:
        """
        Returns the next k predictions for the specified line
        """
        return self.line_arrivals_pred[line_id].ksmallest(k)

    def next_arrivals_by_station_and_line(self, station_id: str, line_id: str, k: int) -> list[Prediction]:
        """
        Returns the next k predictions for the specified station that belong to the specified line. 
        Raise an appropriate exception if the station or line is unknown, or if the line does not serve that station
        """
        if (station_id, line_id) not in self.station_and_line_arrivals_pred:
            raise TubeError(
                f"Line: {line_id} does not serve station: {station_id}.")
        return self.station_and_line_arrivals_pred[(station_id, line_id)].ksmallest(k)

    def next_stations_by_train(self, vehicle_id: str, line_id: str, k: int) -> list[Prediction]:
        """
        Returns the next k station predictions for the identified vehicle on the given line.
        """
        return self.train_arrivals_pred[f"{vehicle_id}{line_id}"].ksmallest(k)

    def __repr__(self) -> str:
        """
        Reports the number of lines and stations in the network.
        """
        return f"Network(stations_num:{len(self.stations.keys())}, lines_nums:{len(self.lines.keys())}"
