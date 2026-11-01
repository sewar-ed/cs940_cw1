"""This module defines a Prediction class."""


from exceptions import TubeError
from station import Station


class Prediction:

    def __init__(self, vehicle_id: str, naptan_id: str, line_id: str,
                 platform_name: str, destination_id: str, time_to_station: int,
                 current_location: str):
        """
        Init prediction object.
        """
        self.train_id = vehicle_id
        self.next_station_id = naptan_id
        self.line_id = line_id
        self.platform_name = platform_name
        self.destination_id = destination_id
        if time_to_station < 0:
            raise TubeError(
                f"Invalid time to station: {time_to_station}.")
        self.time_to_station = time_to_station
        self.current_location = current_location

    def __lt__(self, other: Station):
        """
        Compares two predictions based on time to station, uses id as tie breaker.
        """
        # Approach 1:
        # if self.time_to_station == other.time_to_station:
        # return self.train_id < other.train_id
        # return self.time_to_station < other.time_to_station
        # Approach 2: using lex. comparison of tuples
        # python doc: https://docs.python.org/3/reference/expressions.html#comparisons
        # ids will be compared only if times are equal.
        return (self.time_to_station, self.train_id) < (other.time_to_station, other.train_id)

    def __repr__(self):
        return (f"Prediction('{self.train_id}', '{self.next_station_id}', "
                f"'{self.line_id}', '{self.platform_name}', "
                f"'{self.destination_id}', '{self.time_to_station}', "
                f"'{self.current_location}')")
