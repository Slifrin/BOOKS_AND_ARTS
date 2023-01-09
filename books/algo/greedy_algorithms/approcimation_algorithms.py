"""
    chapter 8
"""


def aproximation():
    states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])
    stations = {}
    stations["kone"] = set(["id", "nv", "ut"])
    stations["ktwo"] = set(["wa", "id", "mt"])
    stations["kthree"] = set(["or", "nv", "ca"])
    stations["kfour"] = set(["nv", "ut"])
    stations["kfive"] = set(["ca", "az"])

    final_stations = set()

    while states_needed:
        best_station = None
        states_covered = set()
        for station, states_for_station in stations.items():
            coverd = states_needed & states_for_station
            if len(coverd) > len(states_covered):
                best_station = station
                states_covered = coverd
        states_needed -= states_covered
        final_stations.add(best_station)
    print(f"{final_stations=}")
    
def main() -> None:
    print(f'Hello main from : {__file__}')
    aproximation()


if __name__ == '__main__':
    main()