from csv_reader import read_csv
import pandas as pd                 # For converting to Pandas dataframe

def read_csv_calculate_stats(csv_file):
    # Read CSV document:
    print("\nAttempting to read {}:".format(csv_file))
    csv = read_csv(csv_file, header=True)

    # Convert CSV document to Pandas dataframe:
    df_indoor = pd.DataFrame(csv)

    # Calculate basic statistics on Humidity:
    print("\nCalculate basic statistics for Humidity:".format(csv_file))
    df_indoor["Humidity"] = pd.to_numeric(df_indoor["Humidity"], errors='coerce')
    humidity_stats = df_indoor["Humidity"].describe()
    return humidity_stats

if __name__ == "__main__":
    """ Reads an example CSV file and calculates basic statistics on column Humidity

    Usage: python csv_example.py
    Example file: weather-data/indoor-temperature-1617.csv
    """

    # Default example CSV document containing indoor temperatures:
    csv_file = 'weather-data/indoor-temperature-1617.csv'
    stats1 = read_csv_calculate_stats(csv_file)

    # Default example CSV document containing indoor temperatures with outliers:
    csv_fileMod = 'weather-data/indoor-temperature-1617 modified.csv'
    stats2 = read_csv_calculate_stats(csv_fileMod)

    print(stats1)
    print(stats2)
