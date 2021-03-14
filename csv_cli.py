import sys
from csv_reader import read_csv
import pandas as pd

if __name__ == "__main__":
    """ Invokes CSV reader with target CSV file as the first argument
    
    Usage: python csv_cli.py [path_to_csv_file]
    """

    # Select CSV document to read:
    if len(sys.argv) > 1:

        # User chosen CSV document:
        csv_file = sys.argv[1]

        # Read CSV document:
        print("\nAttempting to read {}:".format(csv_file))
        csv = read_csv(csv_file, header=True)

        # Convert CSV document to Pandas dataframe:
        print("\nAttempting to convert to Pandas dataframe {}:".format(csv_file))
        df_indoor = pd.DataFrame(csv)
        print(df_indoor.head())

    else:
        # Default example CSV document:
        print("Usage: csv_cli.py [path_to_csv_file]")

