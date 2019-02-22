#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 14:07:13 2019

@author: moosial
"""

import time
import pandas as pd
import numpy as np


def load_data(month, day, file2load, month_data):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
        (str) file2load - name of the city data file in teh same folder
        (df)  month definitions to get teh index for access
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    
    
    print('\n......Loading the requested data\n')
    start_time = time.time()


    print ("......Accessing data from: " + file2load)
    df = pd.read_csv(file2load)
    original_file_ln = str(len(df.index))

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(arg = df['Start Time'], format = '%Y-%m-%d %H:%M:%S')

    # filter by month if applicable
    if month != 'all':
        # extract month and day of week from Start Time to create new columns
        df['month'] = df['Start Time'].dt.month


        month_data = month_data.set_index(['month_long'])
        month_idx = int(month_data['month_key'].loc[month])
        
        
        # filter by month to create the new dataframe
        df = df.loc[df['month'] == month_idx]

    # filter by day of week if applicable
    if day != 'all':
        df['day_of_week'] = df['Start Time'].dt.weekday_name

        # filter by day of week to create the new dataframe
        df = df.loc[df['day_of_week'] == day]

    print('......Filtered Records  ' + str(len(df.index)) + '...Original File Length: ' + original_file_ln)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    return df


def main():
    
    print('.Test routine of for data load .....')
    month = 'January'
    day = 'Sunday'
    file2load = 'chicago.csv'
    
    try:
        month_data = pd.read_excel(io='parameters.xlsx', sheet_name='months', converters={'month_key':str})
    
    except Exception as er:
        print(str(er)) 
        sys.exit()
    
    df = load_data(month, day, file2load, month_data)
   
if __name__ == "__main__":
    main()