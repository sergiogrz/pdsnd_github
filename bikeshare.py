import time
import calendar
from datetime import timedelta
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\nHello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city_names = ['chicago', 'new york', 'washington']
    city_abbreviations = ['chi', 'ny', 'wa']
    city = input('\nWould you like to see data for Chicago (CHI), New York (NY), or Washington (WA)?\n').lower()

    # while loop to handle invalid inputs for the city
    while city not in city_names and city not in city_abbreviations:
        print('\nYou have typed an invalid name. Please enter one of the cities name or abbreviation.')
        city = input('Would you like to see data for Chicago (CHI), New York (NY), or Washington (WA)?\n').lower()

    # if the user types an abbreviation, convert it to its corresponding city name
    if city in city_abbreviations:
        city = city_names[city_abbreviations.index(city)]

    # get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    months_numbers = ['1', '2', '3', '4', '5', '6']
    month = input('\nWhich month (from January [1] to June [6]) would you like to see the data for?\n'
    'Please type \'all\' if you don\'t want to filter by month.\n').lower()

    # while loop to handle invalid inputs for the month
    while month not in months and month not in months_numbers:
        print('\nYou have typed an invalid name. Please enter a month name, a month number, or \'all\'.')
        month = input('Which month (from January [1] to June [6]) would you like to see the data for?\n'
        'Please type \'all\' if you don\'t want to filter by month.\n').lower()

    # if the user types a number, convert it to its corresponding month
    if month in months_numbers:
        month = months[months_numbers.index(month)]

    # get user input for day of week (all, monday, tuesday, ... sunday)
    dow = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    dow_numbers = ['1', '2', '3', '4', '5', '6', '7']
    day = input('\nWhich day of the week (from Monday [1] to Sunday [7]) are you interested in?\n'
    'Please type \'all\' if you don\'t want to filter by any day of the week.\n').lower()

    # while loop to handle invalid inputs for the day of the week
    while day not in dow and day not in dow_numbers:
        print('\nYou have typed an invalid name. Please enter a day name, a day number, or \'all\'.')
        day = input('Which day of the week (from Monday [1] to Sunday [7]) are you interested in?\n'
        'Please type \'all\' if you don\'t want to filter by any day of the week.\n').lower()

    # if the user types a number, convert to its corresponding day of the week
    if day in dow_numbers:
        day = dow[dow_numbers.index(day)]

    print('\n' + '-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month, day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[(df['month'] == month)]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[(df['day_of_week'] == day.title())]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    print('Notice that the results for month and day of the week are only useful if you \n'
    'have selected \'all\' when you were asked about these filters\n')
    start_time = time.time()

    # display the most common month
    popular_month = calendar.month_name[df['month'].mode()[0]]
    print('Most common month: {}'.format(popular_month))

    # display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most common day of the week: {}'.format(popular_day))

    # display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('Most common start hour (0-23): {}'.format(popular_hour))

    print('\nThis took {}s seconds.'.format(time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_st = df['Start Station'].mode()[0]
    print('Most commonly used start station: {}'.format(popular_start_st))

    # display most commonly used end station
    popular_end_st = df['End Station'].mode()[0]
    print('Most commonly used end station: {}'.format(popular_end_st))

    # display most frequent combination of start station and end station trip
    # to do that, I create a new column for the combination Start - End stations
    df['Start - End combination'] = 'From ' + df['Start Station'] + ' to ' + df['End Station']
    popular_comb_st = df['Start - End combination'].mode()[0]
    print('Most frequent combination of start station and end station trip:\n'
    '{}'.format(popular_comb_st))

    print('\nThis took {}s seconds.'.format(time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time = str(timedelta(seconds = int(df['Trip Duration'].sum())))
    print('Total travel time: {}'.format(total_time))

    # display mean travel time
    mean_time = str(timedelta(seconds = int(df['Trip Duration'].mean())))
    print('Average travel time: {}'.format(mean_time))

    print('\nThis took {}s seconds.'.format(time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # display counts of user types
    user_types_count = df['User Type'].value_counts().to_string()
    print('Number of each user type:')
    print(user_types_count)

    # for Washington, no data available regarding gender and birth date
    if city == 'washington':
        print('\nFor Washington there is no data available regarding gender and birth date')

    # display counts of gender and earliest, most recent and most common year of birth
    # for New York and Chicago
    else:
        # eliminate NaN values
        df['Gender'].dropna(axis = 0, inplace = True)
        df['Birth Year'].dropna(axis = 0, inplace = True)

        # display counts of gender
        gender_counts = df['Gender'].value_counts().to_string()
        print('\nCounts of each gender:')
        print(gender_counts)

        # display earliest, most recent, and most common year of birth
        early_birth = int(df['Birth Year'].min())
        recent_birth = int(df['Birth Year'].max())
        common_birth = int(df['Birth Year'].mode()[0])
        print('\nInformation regarding users year of birth:')
        print('Oldest user year of birth: {}'.format(early_birth))
        print('Youngest user year of birth: {}'.format(recent_birth))
        print('Most common year of birth: {}'.format(common_birth))

    print('\nThis took {}s seconds.'.format(time.time() - start_time))
    print('-'*40)

def get_table(city, month, day):
    """Displays each time 5 rows of the dataset until the user decides to stop"""

    print('\nGetting individual trip data...\n')

    # call load_data function to get the original inforamtion (not modified)
    df = load_data(city, month, day)

    # set options to display the table with all its columns instead of a truncated one
    pd.set_option('display.max_columns', None)

    # show each time 5 rows of the get_table
    # until the user decides to stop or there are no more rows to show
    answer = 'yes'
    i = 0
    while answer in ('yes', 'y') and i < len(df.index):
        if i + 5 < len(df.index):
            print(df.iloc[i:i+5])
            i += 5

        else:
            print(df.iloc[i:])
            break

        # ask the user if he wants to see other 5 rows of data
        answer = input('\nWould you like to see some more individual trip data? Please type yes (y) or no (n).\n')
        answer = answer.lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        get_table(city, month, day)

        restart = input('\nWould you like to restart? Enter yes(y) or no(n).\n')
        if restart.lower() not in ('yes', 'y'):
            break


if __name__ == "__main__":
	main()
