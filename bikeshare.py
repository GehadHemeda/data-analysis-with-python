import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
list_of_months = ["january", "february", "march", "april", "may", "june"]
dict_of_days_of_week={1:"sunday",
                      2:"monday",
                      3:"tuesday",
                      4:"wednesday",
                      5:"thursday",
                      6:"friday",
                      7:"saturday"}
list_of_filter_types=["month","day","both","none"]
def get_filters():
    global month
    global day
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city = str(input("would you like to see data for Chicago,New York City,or washington?\n ")).lower()
    while city not in CITY_DATA.keys():
            print("Please enter one of the names of the cities in front of you")
            city =str(input("would you like to see data for Chicago,New York City,or washington?\n ")).lower()

    filter_type=str(input("would you like to filter the data by month, day, both, or none\n")).lower()
    while filter_type not in list_of_filter_types:
        print("Please enter one of the choices in front of you")
        filter_type = str(input("would you like to filter the data by month, day, both, or none\n")).lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    if filter_type =="month":
        day=None
        month=str(input("which month?January,February,March,April,May,or June\n")).lower()
        while month not in list_of_months:
            print("Please enter one of the choices in front of you")
            month = str(input("which month?January,February,March,April,May,or June\n")).lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    if filter_type =="day":
        month=None
        day=int(input("which day?please type ur response as an integer...eg:1=sunday\n"))
        while day not in dict_of_days_of_week.keys():
            print("Please enter one of the choices in front of you")
            day = int(input("which day?please type ur response as an integer...eg:1=sunday\n"))
    if filter_type=="both":
        month = str(input("which month?January,February,March,April,May,or June\n")).lower()
        while month not in list_of_months:
            print("Please enter one of the choices in front of you")
            month = str(input("which month?January,February,March,April,May,or June\n")).lower()
        day = int(input("which day?please type ur response as an integer...eg:1=sunday\n"))
        while day not in dict_of_days_of_week.keys():
            print("Please enter one of the choices in front of you")
            day = int(input("which day?please type ur response as an integer...eg:1=sunday\n"))
    if filter_type=="none":
        month=None
        day=None
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
    df = pd.read_csv(CITY_DATA[city]) #load data

    df['Start Time'] = pd.to_datetime(df['Start Time']) #convert the Start Time column to datetime
    # extract month and day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['days_of_week'] = df['Start Time'].dt.day_name() #but weekday_name not working in this version
    df['hour'] = df['Start Time'].dt.hour
    # filter by month if applicable
    if month != None:
        month = list_of_months.index(month) + 1
        df = df[df['month'] == month]
    #filter by day of week if applicable
    if day != None:
        df = df[df['days_of_week'] == dict_of_days_of_week[day].title()]
    #print(df.head())
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    popular_month= df['month'].mode()[0]
    popular_day = df['days_of_week'].mode()[0]
    popular_hour = df['hour'].mode()[0]
    count_months=0
    count_hours=0
    count_days=0
    for x in df['hour']:
        if x==popular_hour:
            count_hours+=1
    for x in df['days_of_week']:
        if x == popular_day:
            count_days += 1
    for x in df['month']:
        if x == popular_month:
            count_months += 1
    # TO DO: display the most common month
    # TO DO: display the most common day of week
    # TO DO: display the most common start hour

    if month !=None and day !=None:
        print("Most popular hour is:"+ " "+str(popular_hour)+"   "+"count of most pop hour is:"+str(count_hours))

    elif month !=None and day ==None:
        print("Most popular day is:"+" "+str(popular_day)+"   "+"count of most pop day is:"+str(count_days)+"\n")
        print("Most popular hour is:" + " " + str(popular_hour)+"   "+"count of most pop hour is:"+str(count_hours))
    elif month ==None and day ==None:
        print("Most popular month is:" + " " + str(popular_month) +"   "+"count of most pop month is:"+str(count_months)+"\n")
        print("Most popular day is:" + " " + str(popular_day)+"   "+"count of most pop day is:"+str(count_days)+"\n")
        print("Most popular hour is:" + " " + str(popular_hour)+"   "+"count of most pop hour is:"+str(count_hours))
    elif month ==None and day !=None:
        print("Most popular month is:" + " " + str(popular_month)+"   "+"count of most pop month is:"+str(count_months)+"\n")
        print("Most popular hour is:" + " " + str(popular_hour)+"   "+"count of most pop hour is:"+str(count_hours))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    # TO DO: display most commonly used end station
    # TO DO: display most frequent combination of start station and end station trip
    most_start_used=df['Start Station'].mode()[0]
    count_Most_start_used=0
    most_end_used=df['End Station'].mode()[0]
    count_Most_end_used=0

    df['combined col']=df['Start Station']+df['End Station']
    trip_combination = df['combined col'].mode()[0]
    count_combination=0
    for x in df['Start Station']:
        if x==most_start_used:
            count_Most_start_used+=1
    print("most commonly used start station:"+str(most_start_used)+" ,"+"count"+str(count_Most_start_used)+"\n")
    #---------------------------------------------------------------------------------------
    for x in df['End Station']:
        if x==most_end_used:
            count_Most_end_used+=1
    print("most commonly used End station:"+str(most_end_used)+" ,"+"count"+str(count_Most_end_used))
    #------------------------------------------------------------------------------
    for x in df['combined col']:
        if x==trip_combination:
            count_combination+=1
    print("most commonly used start&end station:"+str(trip_combination)+" ,"+"count"+str(count_combination)+"\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_trip_duration = df['Trip Duration'].sum()
    print("Total trip duration :", total_trip_duration)

    # TO DO: display mean travel time
    avg_trip_duration = df['Trip Duration'].mean()
    print("average trip duration :", avg_trip_duration)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    # TO DO: Display counts of gender
    # TO DO: Display earliest, most recent, and most common year of birth

    user_counts = df['User Type'].value_counts()
    print(user_counts)
    counts_of_gender=0
    if 'Gender' in df.columns:
        counts_of_gender=df['Gender'].value_counts()
        print("count of Gender is:"+str(counts_of_gender)+"\n")

    if 'Birth Year' in df.columns:
        print("earliest year of birth"+" "+str(round(df['Birth Year'].min())))
        print("most recent year of birth"+" "+str(round(df['Birth Year'].max())))
        print("most common year of birth"+" "+str(round(df['Birth Year'].mode()[0])))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_the_data(df):

        i=0
        data_disp = str(input("would you like to see some of data?Please type Yes or No.")).lower()
        while True or i <df.shape[0]:

            if data_disp not in ['yes', 'no']:
                data_disp = input("wrong entry. Please type Yes or No.").lower()
            elif data_disp == 'yes':
                i+=5
                print(df.iloc[i: i+5])
                another_entry = input("Do you want to see more? Yes or No").lower()
                if another_entry not in ['yes', 'no']:
                    break
                elif  another_entry=='no':
                    break
            elif data_disp == 'no':
                return

#------------------------------------------------------------------------------------------

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        display_the_data(df)



        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            continue


if __name__ == "__main__":
	main()
