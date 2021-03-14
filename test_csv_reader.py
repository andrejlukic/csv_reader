from csv_reader import read_csv
import pandas as pd                 # For converting to Pandas dataframe

def test_000():
    csvfilepath = 'weather-data/testcsverror001_indoor-temperature-1617.csv'
    csv = read_csv(csvfilepath)

    print(csv)

    assert len(csv) == 6

    csvfilepath = 'weather-data/testnoheader002_indoor-temperature-1617.csv'
    csv = read_csv(csvfilepath, header=True)

    assert len(csv) == 1

    # Compare with Pandas CSV reader:
    df = pd.DataFrame(csv)
    df2 = pd.read_csv(csvfilepath, error_bad_lines=False)
    df[df.columns[1]] = pd.to_numeric(df[df.columns[1]], errors='coerce')
    df2[df2.columns[1]] = pd.to_numeric(df2[df2.columns[1]], errors='coerce')
    print(df2)
    print(df)
    assert all(df[df.columns[1]] == df2[df2.columns[1]])

    csv = read_csv('weather-data/testnoheader002_indoor-temperature-1617.csv', header=False)

    assert len(csv) == 2

    csv = read_csv('weather-data/testemptyspaces003_indoor-temperature-1617.csv', header=True)

    assert len(csv) == 1

    csv = read_csv('weather-data/testemptyspaces003_indoor-temperature-1617.csv', header=False)

    assert len(csv) == 2

    csv = read_csv('weather-data/testbadheader004_indoor-temperature-161.csv', header=True)

    assert len(csv) == 2

    csv = read_csv('weather-data/testbadheader004_indoor-temperature-161.csv', header=False)

    assert len(csv) == 2




def test_001():
    csvfilepath = 'weather-data/barometer-1617.csv'
    csv = read_csv(csvfilepath)

    assert len(csv) == 355

    # Compare with Pandas CSV reader:
    df = pd.DataFrame(csv)
    df["Baro"] = pd.to_numeric(df["Baro"], errors='coerce')
    df2 = pd.read_csv(csvfilepath)
    df2["Baro"] = pd.to_numeric(df2["Baro"], errors='coerce')
    assert all(df["Baro"] == df2["Baro"])
    assert all(df["Baro"].describe() == df2["Baro"].describe())

def test_002a():
    csvfilepath = 'weather-data/indoor-temperature-1617.csv'

    csv = read_csv(csvfilepath)

    assert len(csv) == 354

    df = pd.DataFrame(csv)
    print(df.head())
    df["Humidity"] = pd.to_numeric(df["Humidity"], errors='coerce')
    df["Temperature"] = pd.to_numeric(df["Temperature"], errors='coerce')
    df["Temperature_range (low)"] = pd.to_numeric(df["Temperature_range (low)"], errors='coerce')
    df["Temperature_range (high)"] = pd.to_numeric(df["Temperature_range (high)"], errors='coerce')

    # Compare with Pandas CSV reader:
    df2 = pd.read_csv(csvfilepath)
    df2["Humidity"] = pd.to_numeric(df2["Humidity"], errors='coerce')
    df2["Temperature"] = pd.to_numeric(df2["Temperature"], errors='coerce')
    df2["Temperature_range (low)"] = pd.to_numeric(df2["Temperature_range (low)"], errors='coerce')
    df2["Temperature_range (high)"] = pd.to_numeric(df2["Temperature_range (high)"], errors='coerce')
    assert all(df["Humidity"] == df2["Humidity"])
    assert all(df["Humidity"].describe() == df2["Humidity"].describe())
    assert all(df["Temperature"] == df2["Temperature"])
    assert all(df["Temperature"].describe() == df2["Temperature"].describe())
    assert all(df["Temperature_range (low)"] == df2["Temperature_range (low)"])
    assert all(df["Temperature_range (low)"].describe() == df2["Temperature_range (low)"].describe())

def test_002b():
    csvfilepath = 'weather-data/indoor-temperature-1617 modified.csv'
    csv = read_csv(csvfilepath)

    assert len(csv) == 354

    df = pd.DataFrame(csv)
    print(df.head())
    df["Humidity"] = pd.to_numeric(df["Humidity"], errors='coerce')
    df["Temperature"] = pd.to_numeric(df["Temperature"], errors='coerce')
    df["Temperature_range (low)"] = pd.to_numeric(df["Temperature_range (low)"], errors='coerce')
    df["Temperature_range (high)"] = pd.to_numeric(df["Temperature_range (high)"], errors='coerce')

    # Compare with Pandas CSV reader:
    df2 = pd.read_csv(csvfilepath)
    df2["Humidity"] = pd.to_numeric(df2["Humidity"], errors='coerce')
    df2["Temperature"] = pd.to_numeric(df2["Temperature"], errors='coerce')
    df2["Temperature_range (low)"] = pd.to_numeric(df2["Temperature_range (low)"], errors='coerce')
    df2["Temperature_range (high)"] = pd.to_numeric(df2["Temperature_range (high)"], errors='coerce')
    assert all(df["Humidity"] == df2["Humidity"])
    assert all(df["Humidity"].describe() == df2["Humidity"].describe())
    assert all(df["Temperature"] == df2["Temperature"])
    assert all(df["Temperature"].describe() == df2["Temperature"].describe())
    assert all(df["Temperature_range (low)"] == df2["Temperature_range (low)"])
    assert all(df["Temperature_range (low)"].describe() == df2["Temperature_range (low)"].describe())

def test_003():
    csv = read_csv('weather-data/outside-temperature-1617.csv')

    assert len(csv) == 355

    df = pd.DataFrame(csv)
    print(df.head())
    df["Temperature"] = pd.to_numeric(df["Temperature"], errors='coerce')
    df["Temperature_range (low)"] = pd.to_numeric(df["Temperature_range (low)"], errors='coerce')
    df["Temperature_range (high)"] = pd.to_numeric(df["Temperature_range (high)"], errors='coerce')
    print(df["Temperature"].describe())
    print(df["Temperature_range (low)"].describe())
    print(df["Temperature_range (high)"].describe())

def test_004():
    csv = read_csv('weather-data/rainfall-1617.csv')

    assert len(csv) == 353

    df = pd.DataFrame(csv)
    print(df.head())
    df["mm"] = pd.to_numeric(df["mm"], errors='coerce')
    print(df["mm"].describe())
