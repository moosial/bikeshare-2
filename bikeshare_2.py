import time
import datetime
import pandas as pd
import numpy as np

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyse
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter """
    """ load the help xls for city, day and month descriptions """
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
       

    
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True :
        print('-'*40)
        print('\n......Which city you like to analyze (enter Numbers or Cities)?')
        print('\n[1] - Chicago\n[2] - New York City\n[3] - Washington \n')
        city = input('......Your input:___ ').lower()
        
        try:   

            if city in city_data.city_lower.values:
                # now get the city name 
                city_data = city_data.set_index(['city_lower'],drop=False)
                city = city_data['city'].loc[city]
                print('-'*40)
                break
           
            elif city in city_data.city_key.values:
                # now get the city name 
                city_data = city_data.set_index(['city_key'],drop=False)
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
            month_short = month_data['month_short'].iloc[(i)] 
            month_long = month_data['month_long'].iloc[(i)]    
            print('[{}]- {} -- {}'.format(i,month_short, month_long))
        
        month = input('......Your input:___ ').capitalize()
         
        try:
            if  month in month_data.month_key.values:
                # now get the month name J
                month_data = month_data.set_index(['month_key'],drop=False)
                month = month_data['month_long'].loc[month]
                print('-'*40)
                break

            
            elif month in month_data.month_short.values:
                # now get the month name 
                month_data = month_data.set_index(['month_short'],drop=False)
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
                day_data = day_data.set_index(['day_key'],drop=False)
                day = day_data['day_long'].loc[day]
                print('-'*40)
                break
            
            elif day in day_data.day_short.values: 
                # now get the month name 
                day_data = day_data.set_index(['day_short'],drop=False)
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
    
    
    return city, month, day, file2load, month_data
  

def load_data(month, day, file2load, month_data):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
        (str) file2load - name of the city data file in teh same folder
        (df)  month definitions to get the index for access
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
    if month != 'All':
        # extract month and day of week from Start Time to create new columns
        df['month'] = df['Start Time'].dt.month
        
        month_data = month_data.set_index(['month_long'],drop=False)
        month_idx = int(month_data['month_key'].loc[month])
        
        # filter by month to create the new dataframe
        df = df.loc[df['month'] == month_idx]

    # filter by day of week if applicable
    if day != 'All':
        df['day_of_week'] = df['Start Time'].dt.weekday_name

        # filter by day of week to create the new dataframe
        df = df.loc[df['day_of_week'] == day]

    print('......Filtered Records  ' + str(len(df.index)) + '...Original File Length: ' + original_file_ln)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    return df


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
    # so to avoid errors check for th epresence of the 2 columns
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

def display_raw(df):
   #Simply keep displaying five lines of the filtzered data if the user wnat to. """"
    
    count=0;
    while True:
        display = input('\n......Would you like to view individual trip data belonging to your filter?\n'
                        '......Pls. type yes (y) or no (n). Your choice: ')
        if display.lower() in ('yes', 'no','y','n'):
            if display.lower() == 'yes' or display.lower() == 'y':
                """ simply acces by a range which increases by 5 """                
                print(df[count:count+5].to_string())
                count +=5
            else:
                print('......Display of the data ends!')
                break
        else:    
            print('.....Enter a valid input provided in the options')





def main():
    while True:
        city, month, day, file2load, month_data = get_filters()
        df = load_data(month, day, file2load, month_data)
        if len(df) > 0:
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)
            display_raw(df)
        else:
            print('......The filters applied to the data returned no results!')
            
        restart = input('\n......Would you like to restart?\n......Pls. type yes (y) or no (n). Your choice: ')
        
        if restart.lower() in ('yes', 'no','y','n'):
            if restart.lower() in ('yes', 'y'):
                print('......Let\'s continue.')
            else:
                print('......bye bye...')
                break
        else:
            print('.....Enter a valid input provided in the options')


if __name__ == "__main__":
	main()
