#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 08:18:33 2019

@author: moosial
"""


import time
import pandas as pd
import numpy as np
import sys


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    
    
    """ load the help cvs for city, day and month descriptions ("""
    print('......Loading paramters.xlsx (Sheets: cities, months and days).')
    print('......Pls. make sure to have the xls in the same folder as the ')
    print('......python script bikeshare_2.py! ')
    try:
        city_data   = pd.read_excel(io='parameters.xlsx', sheet_name='cities', converters={'city_key':str})
        month_data = pd.read_excel(io='parameters.xlsx', sheet_name='months', converters={'month_key':str})
        day_data = pd.read_excel(io='parameters.xlsx', sheet_name='days' , converters={'day_key':str})
        
    except Exception as er:
        print(str(er)) 
        sys.exit()
       
    export_month = month_data
    
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True :
        print('-'*40)
        print('\n......Which city you like to analyze (enter Numbers or Cities)?')
        print('\n[1] - Chicago\n[2] - New York City\n[3] - Washington \n')
        city = input('......Your input:___ ').lower()
        
        try:

            if city in city_data.city_lower.values:
                # now get the city name 
                city_data = city_data.set_index(['city_lower'])
                city = city_data['city'].loc[city]
                print('-'*40)
                break
           
            elif city in city_data.city_key.values:
                # now get the city name 
                city_data = city_data.set_index(['city_key'])
                city = city_data['city'].loc[city]
                print('-'*40)
                break 
                
            else: 
                print('......Wrong Input! Enter Numbers (1-3) or Cities!')
            
        except Exception as er:
            print(str(er)) 
            sys.exit()
            
    print('Your choice for city: {}. Thank you.'.format(city))
    city_data = city_data.set_index(['city'])
    file2load = city_data.file.loc[city]

    # get user input for month (all, january, february, ... , june)
    while True:
        print('-'*40)
        print('\n......Which month you like to analyze (enter Numbers or Month)?')
        length = len(month_data)
        
               
        for i in range(0, length, 1):
            month_short = month_data['month_short'].loc[i] 
            month_long = month_data['month_long'].loc[i]    
            print('[{}]- {} -- {}'.format(i,month_short, month_long))
        
        month = input('......Your input:___ ').capitalize()
           
         
        try:
            if  month in month_data.month_key.values:
                # now get the month name 
                month_data = month_data.set_index(['month_key'])
                month = month_data['month_long'].loc[month]
                print('-'*40)
                break
            
            elif month in month_data.month_short.values:
                # now get the month name 
                month_data = month_data.set_index(['month_short'])
                month = month_data['month_long'].loc[month]
                print('-'*40)
                break
             
            elif month in month_data.month_long.values:
                # now get the month name (actually to set teh index and slect teh value throes an error)
                month = month
                print('-'*40)
                break
                
            else: 
                print('......Wrong Input! Enter Numbers (1-12) or Month short or long like Jan or January!')
            
              
        except Exception as er:
            print(str(er)) 
            sys.exit()  
            
            
    print('Your choice for month: {}. Thank you.'.format(month))
    

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        print('-'*40)
        print('\n......Which day you like to analyze (enter Number or Day)?')
        length = len(day_data)
       
                       
        for i in range(0, length, 1):
            day_key   = day_data['day_key'].loc[i]
            day_short = day_data['day_short'].loc[i] 
            day_long  = day_data['day_long'].loc[i]    
            print('[{}]- {} -- {}'.format(day_key, day_short,day_long))
        
        day = input('......Your input:___ ').capitalize()
           
         
        try:
            if  day in day_data.day_key.values:
                # now get the month name 
                day_data = day_data.set_index(['day_key'])
                day = day_data['day_long'].loc[day]
                print('-'*40)
                break
            
            elif day in day_data.day_short.values: 
                # now get the month name 
                day_data = day_data.set_index(['day_short'])
                day = day_data['day_long'].loc[day]
                print('-'*40)
                break
             
            elif day in day_data.day_long.values:
                # now get the month name (actually to set teh index and slect teh value throes an error)
                day = day
                print('-'*40)
                break
                
            else: 
                print('......Wrong Input! Enter Numbers (1-12) or Month short or long like Jan or January!')
            
 
             
        except Exception as er:
            print(str(er)) 
            sys.exit()     

    print('Your choice for day: {}. Thank you.'.format(day))
    
    print('-'*40)
    
    return city, month, day, file2load, export_month


def main():
      print('.Test routine of of user input.....')
      city, month, day, file, month_data = get_filters()
      print('.......these are your inputs:')
      print('.city: {}'.format(city))
      print('.month: {}'.format(month))
      print('.day: {}'.format(day))
      print('.file: {}'.format(file))
      print('.month: {}'.format(month_data))
    
      
if __name__ == "__main__":
	main()
