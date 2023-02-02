import numpy as np
import pandas as pd


def create_data(m: int = 10, n: int = 20) -> pd.DataFrame:
    np.random.seed(42)
    data = np.random.uniform(low=0, high=100, size=(m, n)).astype(int)
    return pd.DataFrame(data)


def set_zeros(df: pd.DataFrame) -> pd.DataFrame:
    rows, cols = np.where(df == 0)

    df.iloc[rows, :] = 0
    df.iloc[:, cols] = 0

    return df


if __name__ == "__main__":
    df = create_data()
    df = set_zeros(df)
    print(df)
