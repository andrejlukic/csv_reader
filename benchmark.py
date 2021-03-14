from csv_reader import read_csv
import pandas as pd
import time

if __name__ == "__main__":

    csvfilepath = 'weather-data/indoor-temperature-1617.csv'

    t1 = time.time()
    csv = read_csv(csvfilepath)
    t2 = time.time()

    assert len(csv) == 354

    df = pd.DataFrame(csv)
    print(df.head())
    df["Humidity"] = pd.to_numeric(df["Humidity"], errors='coerce')
    df["Temperature"] = pd.to_numeric(df["Temperature"], errors='coerce')
    df["Temperature_range (low)"] = pd.to_numeric(df["Temperature_range (low)"], errors='coerce')
    df["Temperature_range (high)"] = pd.to_numeric(df["Temperature_range (high)"], errors='coerce')

    # Compare with Pandas CSV reader:
    t3 = time.time()
    df2 = pd.read_csv(csvfilepath)
    t4 = time.time()

    print("Reading {} lines in {} compared to Pandas reader in {}".format(df2.shape[0], t2-t1, t4-t3))