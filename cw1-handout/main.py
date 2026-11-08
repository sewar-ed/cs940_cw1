"""
Author: Siddharth Srivastava
"""
import json
from station import Station
from line import Line
from branch import Branch
from prediction import Prediction
from network import Network

from pprint import pprint

path_to_jsons = '/modules/cs940/cw1/'


def main():
    tube = Network()

    # Populate all the stations and lines to our network
    lines = ['bakerloo', 'central', 'circle', 'district', 'hammersmith-city',
             'jubilee', 'metropolitan', 'northern', 'piccadilly', 'victoria', 'waterloo-city']

    for line in lines:
        file = f'{path_to_jsons}lines/{line}.json'

        with open(file, 'r') as f:
            obj = json.load(f)

        line_obj = Line(obj['lineId'], obj['lineName'])

        for stop_point_sequence in obj['stopPointSequences']:
            branch = Branch(
                branch_id=stop_point_sequence['branchId'], next_branch_ids=stop_point_sequence['nextBranchIds'])

            for stop_point in stop_point_sequence['stopPoint']:
                station = Station(stop_point['id'], stop_point['name'], stop_point['lines'],
                                  stop_point['zone'], stop_point['lat'], stop_point['lon'])
                branch.add_station(station.station_id)

                tube.add_station(station)

            line_obj.add_branch(branch)

        tube.add_line(line_obj)

    # Populate our predictions to our network
    with open(f'{path_to_jsons}arrivals/arrivals-5844355.json', 'r') as f:
        obj = json.load(f)

    for arrival in obj:
        pred = Prediction(
            arrival['vehicleId'],
            arrival['naptanId'],
            arrival['lineId'],
            arrival['platformName'],
            arrival.get('destinationNaptanId', ''),
            arrival['timeToStation'],
            arrival['currentLocation']
        )

        tube.add_prediction(pred)

    # # Prelimiary tests (should run successfully after implementing everything in the cw)
    print('----- Next 6 trains arriving at TCR overall ----')
    pprint(tube.next_arrivals_by_station('940GZZLUTCR', k=6))

    print('---- Next 12 trains on the Victoria line ---- ')
    pprint(tube.next_arrivals_by_line('victoria', k=12))

    print('---- Next 8 trains at Green park on piccadilly line ---- ')
    pprint(tube.next_arrivals_by_station_and_line(
        station_id='940GZZLUGPK', line_id='piccadilly', k=8))

    print('---- Where is train 012 on the District line going next? (in order) ---- ')
    # note that you might not have a train 012 in the district line in your arrivals.json - change this accordingly.
    pprint(tube.next_stations_by_train(
        vehicle_id='204', line_id='waterloo-city', k=10))
    # ==========================================
    # 1. Edge Case Tests for 'k' Parameters
    # ==========================================
    print('----- Testing k = 0 (should return empty list) ----')
    pprint(tube.next_arrivals_by_station('940GZZLUTCR', k=0))

    print('----- Testing k = -1 (should return all arrivals) ----')
    pprint(tube.next_arrivals_by_station('940GZZLUTCR', k=-1))

    print('----- Testing k larger than total available arrivals ----')
    pprint(tube.next_arrivals_by_line('waterloo-city', k=500))

    # # ==========================================
    # # 2. Trie / Prefix Search Tests
    # # ==========================================
    # print('----- Searching stations with empty prefix (should return all) ----')
    # all_stations = tube.search_by_prefix('')
    # print(f'Total stations returned: {len(all_stations)}')

    # print('----- Searching stations matching prefix "park" (Hint: expect 24) ----')
    # park_stations = tube.search_by_prefix('park')
    # pprint(park_stations)
    # assert len(park_stations) == 24, f"Expected 24, got {len(park_stations)}"

    # print('----- Searching stations matching prefix "road" (Hint: expect 12) ----')
    # road_stations = tube.search_by_prefix('road')
    # pprint(road_stations)
    # assert len(road_stations) == 12, f"Expected 12, got {len(road_stations)}"

    # print('----- Searching stations matching prefix "south" (Hint: expect 11) ----')
    # south_stations = tube.search_by_prefix('south')
    # pprint(south_stations)
    # assert len(south_stations) == 11, f"Expected 11, got {len(south_stations)}"

    # # ==========================================
    # # 3. Alternative Station & Line Combinations
    # # ==========================================
    # print('----- Next 5 trains at King\'s Cross St. Pancras (Central/Northern/Piccadilly/Victoria) ----')
    # # King's Cross St. Pancras NaPTAN ID
    # pprint(tube.next_arrivals_by_station('940GZZLUKSX', k=5))

    # print('----- Next 10 trains on the Central line ----')
    # pprint(tube.next_arrivals_by_line('central', k=10))

    # print('----- Next 3 trains at Oxford Circus on the Bakerloo line ----')
    # pprint(tube.next_arrivals_by_station_and_line(
    #     station_id='940GZZLUOXC', line_id='bakerloo', k=3))


if __name__ == '__main__':
    main()
