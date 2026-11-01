"""This module defines a Station class."""

import json
import math
import re
from typing import List

from exceptions import TubeError
# The 11 Tube lines are the Bakerloo, Central, Circle, District, Hammersmith & City, Jubilee,
# Metropolitan, Northern, Piccadilly, Victoria, and Waterloo & City
# TO-DO: ask if this can be done (???)
TUBE_LINES = ['bakerloo', 'central', 'circle', 'district', 'hammersmith-city',
              'jubilee', 'metropolitan', 'northern', 'piccadilly', 'victoria', 'waterloo-city']
MAX_LAT, MIN_LAT = 90, -90
MAX_LON, MIN_LON = 180, -180
R = 6371.0  # given radius.


class Station:

    def __init__(self, station_id: str, station_name: str, interchange_lines: List, zones: str, lat: float, lon: float):
        """Init station object."""
        self.station_id, self.station_name = station_id, station_name
        # Split zones either by + or / and keep order.
        self.zones = re.split(r'\+ | /', zones)
        # Get id per line if it exists
        self.interchange_lines_ids = [line['id']
                                      for line in interchange_lines if 'id' in line]
        # Check if lat and lon are within normal bounds.
        if lat < MIN_LAT or lat > MAX_LAT:
            raise TubeError(f"Latitude {lat} is out of bounds.")
        self.lat = lat
        if lon < MIN_LON or lon > MAX_LON:
            raise TubeError(f"Longitude {lon} is out of bounds.")
        self.lon = lon

        # For later use in __repr__
        self.repr_zones = zones
        self.repr_interchange_lines = interchange_lines

    def is_interchange(self) -> bool:
        """Returns True if the station is an interchange station with tube lines not accounting for bus routes, False otherwise."""
        return any(line in TUBE_LINES for line in self.interchange_lines_ids)  # If any tube line passes in station it is an interchange

    def distance_to(self, other: "Station") -> float:
        """Returns distance between current station and 'other' using haversine distance and r = 6371.0"""
        # Notice doc https://docs.python.org/3/library/math.html#math.cos
        # math.cos/sin expect radians as input, therefore we will convert the lat/lon values.
        rad_lat, rad_lon = math.radians(self.lat), math.radians(self.lon)
        delta_phi = math.radians(other.lat) - rad_lat
        delta_lambda = math.radians(other.lon) - rad_lon
        # Using equations in link for question 1(b).
        hav_theta = (1 - math.cos(delta_phi))/2 + math.cos(rad_lat) * \
            math.cos(math.radians(other.lat))*((1-math.cos(delta_lambda))/2)
        # Calculate theta using hav_theta.
        theta = 2*math.asin(math.sqrt(hav_theta))
        return theta*R

    def __str__(self):
        return f"This is {self.station_name} station."

    def __repr__(self):
        return (f"Station('{self.station_id}', '{self.station_name}', "
                f"'{self.repr_interchange_lines}', '{self.repr_zones}', '{self.lat}', '{self.lon}')")

    def __eq__(self, other: "Station"):
        """Checks equality using id."""
        return self.station_id == other.station_id

    def __hash__(self):
        """Hash on tuples of (id,name)"""
        return hash((self.station_id, self.station_name))
