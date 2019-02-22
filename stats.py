#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 16:20:27 2019

@author: moosial
"""

import time
import pandas as pd
import numpy as np
import datetime


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\n......Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(arg = df['Start Time'], format = '%Y-%m-%d %H:%M:%S')

   
    #display the most common month
    most_common_month = df['Start Time'].dt.month.mode()[0]
    print('......Most common month:        ', most_common_month)

    #display the most common day of week
    most_common_day_of_week = df['Start Time'].dt.weekday_name.mode()[0]
    print('......Most common day of week: ', most_common_day_of_week)

    #display the most common start hour
    common_start_hour = df['Start Time'].dt.hour.mode()[0]
    print('......Most frequent start hour:  ', common_start_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    
    """Displays statistics on the most popular stations and trip."""
    print('\n......Calculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # I searched help here:
    #https://stackoverflow.com/questions/48590268/pandas-get-the-most-frequent-values-of-a-column
    
    start_time = time.time()

    #display most commonly used start station
    print('......Most commonly used start station:     ', df['Start Station'].value_counts().idxmax())

    #display most commonly used end station
    print('......Most commonly used end station:       ', df['End Station'].value_counts().idxmax())

    #display most frequent combination of start station and end station trip
    #do a string concat
    concat_stations = df['Start Station'] + " to " + df['End Station']
    concat_stations = str(concat_stations.value_counts().idxmax())
    print('......Most frequent used combinations are:   {}'.format(concat_stations))

    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    # looked here for help: https://stackoverflow.com/questions/775049/how-do-i-convert-seconds-to-hours-minutes-and-seconds
    print('\n......Calculating Trip Duration...\n')
    start_time = time.time()
    # display total travel time
    total_travel_time = int(df['Trip Duration'].sum())
    total_travel_time  = datetime.timedelta(seconds=total_travel_time)
    print('......Total travel time: ' + str(total_travel_time))
  

    #display mean travel time
    mean_travel_time = int(df['Trip Duration'].mean())
    mean_travel_time = datetime.timedelta(seconds=mean_travel_time)
    print('......Mean travel time: {} '.format(mean_travel_time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\n......Calculating User Stats...\n')
    start_time = time.time()

    #Display counts of user types
    user_types = df['User Type'].value_counts()
    print('......Counts of user types: \n' +  user_types.to_string())
    
    # washington doesn't has gnder and birthyear

    # Display counts of gender
    if 'Gender' in df.columns:
        gender_count = df['Gender'].value_counts()
        print('......Counts of gender:  \n' +  gender_count.to_string())

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_birth_year = df['Birth Year'].min()
        most_recent_birth_year = df['Birth Year'].max()
        common_birth_year = df['Birth Year'].mode()[0]
        print("......Earliest year of birth:    " + str(earliest_birth_year))
        print("......Most recent year of birth: " + str(most_recent_birth_year))
        print("......Most common year of birth: " + str(common_birth_year))
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    print('.Test routine of for statistics .....')
    file2load = 'chicago.csv'
    df = pd.read_csv(file2load)
    df['Start Time'] = pd.to_datetime(arg = df['Start Time'], format = '%Y-%m-%d %H:%M:%S')
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    time_stats(df)
    station_stats(df)
    trip_duration_stats(df)
    user_stats(df)


if __name__ == "__main__":
	main()