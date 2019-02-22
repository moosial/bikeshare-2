import time
import pandas as pd
import numpy as np
from get_filter import get_filters
from load_data import load_data
from stats import *



# imported from load_data.py
# ---> def get_filters():
# imported from get_filter.py


 # imported from load_data.py
# ---> def load_data(month, day, file2load, month_data):
# imported from load_data.py


# imported from stats.py
# ---> def  time_stats(df)
# ---> def  station_stats(df)
# ---> def  trip_duration_stats(df)
# ---> def  user_stats(df)
# imported from stats.py

def main():
    while True:
        city, month, day, file2load, month_data = get_filters()
        df = load_data(month, day, file2load, month_data)
        if len(df) > 0:
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)
        else:
            print('The filters applied to the data returned no results!')
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
