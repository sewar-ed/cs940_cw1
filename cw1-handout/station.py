"""This module defines a Station class."""

import json
import math
import re
from typing import List

from exceptions import TubeError
# The 11 Tube lines are the Bakerloo, Central, Circle, District, Hammersmith & City, Jubilee,
# Metropolitan, Northern, Piccadilly, Victoria, and Waterloo & City
# TO-DO: ask if this can be done (???)
TUBE_LINES = ["bakerloo", "central", "circle", "district", "hammersmith",
              "jubilee", "metropolitan", "northern", "piccadilly", "victoria", "waterloo"]


class Station:

    def __init__(self, station_id: str, station_name: str, interchange_lines: List, zones: str, lat: float, lon: float):
        """Init station object."""
        self.station_id, self.station_name = station_id, station_name
        # Split zones either by + or / and keep order.
        self.zones = re.split(r'\+ | /', zones)
        # Get id per line if it exists
        self.interchange_lines_ids = [line['id']
                                      for line in interchange_lines if 'id' in line]
        # Check if lat in [-90, 90] and lon in [-180, 180]
        if lat < -90 or lat > 90:
            raise TubeError(f"Latitude {lat} is out of bounds.")
        self.lat = lat
        if lon < -180 or lon > 180:
            raise TubeError(f"Longitude {lon} is out of bounds.")
        self.lon = lon

        # For use in __repr__
        self.repr_zones = zones
        self.repr_interchange_lines = interchange_lines

    def is_interchange(self) -> bool:
        """Returns True if the station is an interchange station with tube lines not accounting for bus routes, False otherwise."""
        return any(line in TUBE_LINES for line in self.interchange_lines_ids)  # If any tube line passes in station it is an interchange

    def distance_to(self, other: "Station") -> float:
        """Returns distance between current station and 'other' using haversine distance and r = 6371.0"""
        rad_lat, rad_lon = math.radians(self.lat), math.radians(
            self.lon)  # math.cos/sin expect radians.
        delta_phi = math.radians(other.lat) - rad_lat
        delta_lambda = math.radians(other.lon) - rad_lon
        # Using equations in link for question 1(b).
        hav_theta = (1 - math.cos(delta_phi))/2 + math.cos(rad_lat) * \
            math.cos(math.radians(other.lat))*((1-math.cos(delta_lambda))/2)
        # Calculate theta using hav_theta.
        theta = 2*math.asin(math.sqrt(hav_theta))
        return theta*6371.0

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
        return hash(self.station_id, self.station_name)
    # def find_station_modes(self) -> List[str]:
    #     """Opens lines file of a station and returns a list of modes for the station."""
    #     # modes = []
    #     # # Each station has a corresponding lines file.
    #     # with open(f"/modules/cs940/cw1/lines/*.json", "r") as f:
    #     #     lines = json.load(f)
    #     #     # Each lines file has a stations object containing stations information (including modes).
    #     #     if "modes" in lines:
    #     #         modes.extend(lines["modes"])
    #     # return modes
    #     # this is wrong because lines have multiple stations.. we need to look for all lines in folder that include station name..
    #     pass
