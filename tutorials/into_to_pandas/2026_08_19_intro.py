import sys

print("exe", sys.executable)
print("prefix", sys.prefix)


import numpy as np
import pandas as pd

from pprint import pprint


def create_series():
    s = pd.Series([1, 3, 5, np.nan, 6, 8])
    print(s)


def create_dataframe():
    dates = pd.date_range("20130101", periods=6)
    pprint(dates)

    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
    pprint(df)
    print(df.describe())
    # transposing data
    print(df.T)
    print(df.sort_index(axis=1, ascending=False))
    print(df.sort_values(by="B"))


def create_df_from_dict():
    df = pd.DataFrame(
        {
            "A": 1.0,
            "B": pd.Timestamp("20130102"),
            "C": pd.Series(1, index=list(range(4)), dtype="float32"),
            "D": np.array([3] * 4, dtype="int32"),
            "E": pd.Categorical(["test", "train", "test", "train"]),
            "F": "foo",
        }
    )
    pprint(df)
    print(df.dtypes)
    print(df.A)
    print(df.head(2))
    print(df.tail(3))
    print(df.index)
    print(df.columns)
    pprint(df.to_numpy())
    # print(df.describe())


def play_with_selection():
    dates = pd.date_range("20130101", periods=6)
    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
    print(df["A"])
    for i in df["A"]:
        print(type(i), i)
    pprint(df.A)

    pprint(df[["A", "B"]])

    pprint(df[0:3])
    print(df["20130102":"20130104"])


def selection_by_label():
    dates = pd.date_range("20130101", periods=6)
    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
    print(df.loc[dates[0]])

    print(df.loc[:, ["A", "B"]])

    print(df.loc["20130102":"20130104", ["A", "B"]])

    print(df.loc[dates[0], "A"])
    print(df.at[dates[0], "A"])


def selection_by_position():
    dates = pd.date_range("20130101", periods=6)
    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
    print(df.iloc[3])
    print(df.iloc[3:5, 0:2])
    print(df.iloc[[1, 2, 4], [0, 2]])
    print(df.iloc[1:3, :])
    print(df[:])
    print(df.iloc[:, 1:3])
    print(df.iloc[1, 1])
    print(df.iat[1, 1])


def boolean_indexing():
    dates = pd.date_range("20130101", periods=6)
    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
    # Select rows where df.A is greater than 0.
    print(df[df["A"] > 0])
    # Selecting values from a DataFrame where a boolean condition is met:
    print(df[df > 0])

    df2 = df.copy()
    df2["E"] = ["one", "one", "two", "three", "four", "three"]
    pprint(df2)
    # filtering with range
    pprint(df2[df2["E"].isin(["two", "four"])])


def setting_column_values():
    dates = pd.date_range("20130101", periods=6)
    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
    s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range("20130102", periods=6))
    pprint(s1)
    df["F"] = s1
    pprint(df)
    df.at[dates[0], "A"] = 0
    df.iat[0, 1] = 0
    df.loc[:, "D"] = np.array([5] * len(df))
    pprint(df)
    df2 = df.copy()
    df2[df2 > 0] = -df2
    pprint(df2)


def missing_data(): ...


def main() -> None:
    print(f"Hello main from : {__file__} executed by {sys.executable}")
    # create_series()
    # create_dataframe()
    # create_df_from_dict()
    # play_with_selection()
    # selection_by_label()
    # selection_by_position()
    # boolean_indexing()
    # setting_column_values()
    missing_data()

if __name__ == "__main__":
    main()
