import time
import pandas as pd
import numpy as np
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ['chicago', 'new york city', 'washington']
    city = input("Enter city name ").lower()
    while city not in cities:
        city = input('while nearly right,Please try again').lower()
        if city in cities:
            print("Great!,{}".format(city))
            break
        else:
             print("Ops!, nearly right, try again")
    # TO DO: get user input for month (all, january, february, ... , june)
    months=['all','january','june','july','august','september','may','april','october','november','december','february','march']
    month=input('Enter the month name ').lower()
    while month not in  months:
        month=input('while:try again ').lower()
        if month in months:
            print("well done,{}".format(month))
            break
        else:
            print ('Ops!, something went worng')
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days=['all','monday','sunday','tuesday','wednesday','thursday','friday','saturday']
    day=input('Enter the day ').lower()
    while day not in days:
        day=input('Ops! try please ').lower()
        if day in days:
            print('well done , the day is  {}'.format(day))
            break
        else:
                print('Ops, try again ')
    print('-'*40)
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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df




def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    MCM=df['month'].mode()[0]
    
    
    


    # TO DO: display the most common day of week
    MCD=df['day_of_week'].mode()[0]
        
    
    


    # TO DO: display the most common start hour
    
    mch=df['Start Time'].dt.hour.mode()[0]
    
    


    print("\nThis took %s seconds.\n" % (time.time() - start_time),'the most common month {}\n'.format(MCM),
          'the most common day of week {}\n'.format(MCD),
          'the most common start hour {}\n'.format(mch)
         )
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    MCS=df['Start Station'].mode()[0]


    # TO DO: display most commonly used end station
    MCE=df['End Station'].mode()[0]


    # TO DO: display most frequent combination of start station and end station trip
    df['Start StationEnd Station']=df['Start Station'] + df['End Station']
    MCSE=df['Start StationEnd Station'].mode()[0]


    print("\nThis took %s seconds.\n" % (time.time() - start_time),
          "The most commonly used start station IS {}\n".format(MCS),
         "The most commonly used end station IS {}\n".format(MCE),
          "The most frequent combination of start station and end station trip IS {} ".format(MCSE)
         )
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    ttt=df['Trip Duration'].sum()


    # TO DO: display mean travel time
    MTT=df['Trip Duration'].mean()


    print("\nThis took %s seconds.\n" % (time.time() - start_time),
          "The total travel time {}\n".format(ttt),
         "The mean travel time {} ".format(MTT))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('counts of user types :\n {}'.format(df['User Type'].value_counts().to_frame()))
    
    
    try:
        print('counts of gender :\n {}'.format(df['Gender'].value_counts().to_frame()))
    except:
        print('error in gender data ')
        
   

    
    
   
    


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        print("The earliest year of birth is {} \n".format(df['year of birth'].min()))
        print(" the latest year of birth is {} \n".format(df['year of birth'].max()))
        print("the most common years is {}\n".format(df['year of birth'].mode()[0]))
    except:
        print ("error in data")

        
   
        



    print("\nThis took %s seconds.\n" % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
def display_raw_data(df):
    """Displays raw data in batches of 5 rows to the user for their filtered dataframe"""
    display_data_input = input("Would you like to see raw data for your chosen dataset? Type 'yes': ").lower()
    index = 0
    while True:
        if display_data_input == "yes":
            print(df.iloc[0:5,:])
        display_data_input = input("Would you like to see 5 more rows of this data? Type 'yes' or 'no': ").lower()
        if display_data_input == "yes":
            index += 5 # Increment the index by some value
        elif display_data_input == "no":
            break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break



if __name__ == "__main__":
	main()
