"""This module creates a station class"""

import json
import re
from typing import List

from exceptions import TubeError


class Station:

    def __init__(self, station_id: str, station_name: str, interchange_lines: List, zones: str, lat: float, lon: float):
        self.station_id, self.station_name = station_id, station_name
        # Split zones either by + or / and keep order.
        self.zones = re.split(r'\+ | /', zones)
        # Get id per line if it exists
        self.interchange_lines = [line['id']
                                  for line in interchange_lines if 'id' in line]
        # Check if lat in [-90, 90] and lon in [-180, 180]
        if lat < -90 or lat > 90:
            raise TubeError(f"Latitude {lat} is out of bounds.")
        self.lat = lat
        if lon < -180 or lon > 180:
            raise TubeError(f"Longitude {lon} is out of bounds.")
        self.lon = lon

    def is_interchange(self) -> bool:
        """Returns True if the station is an interchange station with tube lines not accounting for bus routes, False otherwise."""
        modes = self.find_station_modes()
        return True if "tube" in modes and len(self.interchange_lines) > 1 else False

    def find_station_modes(self) -> List[str]:
        """Opens lines file of a station and returns a list of modes for the station."""
        modes = []
        # Each station has a corresponding lines file.
        with open(f"/modules/cs940/cw1/lines/*.json", "r") as f:
            lines = json.load(f)
            # Each lines file has a stations object containing stations information (including modes).
            if "modes" in lines:
                modes.extend(lines["modes"])
        return modes
        # this is wrong because lines have multiple stations.. we need to look for all lines in folder that include station name..
        pass
