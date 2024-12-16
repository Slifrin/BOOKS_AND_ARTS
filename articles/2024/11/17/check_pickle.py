import pickle
from pprint import pprint


def main() -> None:
    print(f"Hello main from : {__file__}")
    my_data = {"name": "Tom", "Age": 31}
    with open("tmp_data.pkl", "wb") as wf:
        pickle.dump(my_data, wf)
        print(pickle.dumps(my_data))

    with open("tmp_data.pkl", "rb") as rf:
        loaded_data = pickle.load(rf)

    pprint(loaded_data)


if __name__ == "__main__":
    main()
