#! /usr/bin/env python

stations = {
    'kone': set(['id', 'nv', 'ut']),
    'ktwo': set(['wa', 'id', 'mt']),
    'kthree': set(['or', 'nv', 'ca']),
    'kfour': set(['nv', 'ut']),
    'kfive': set(['ca', 'az'])
} 

def greedy(states_needed):
    final_stations = set()
    while states_needed:
        best_station = None
        states_covered = set()
        for station, states_for_station in stations.items():
            covered = states_for_station & states_needed
            if len(covered) > len(states_covered):
                best_station = station
                states_covered = covered

        final_stations.add(best_station)
        states_needed -= states_covered
    return final_stations

def main():
    states_needed = set(['mt', 'wa', 'or', 'id', 'nv', 'ut'])
    print greedy(states_needed)


if __name__ == '__main__':
    main()
