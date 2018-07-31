# define the CityInfo class
# CityInfo class encapsulates the bikeshare statistics of a city

import pandas as pd
import datetime

class BSCityStats:
    # error messages list
    errors = []
    # Display dropdown selection
    city_options = ['Chicago', 'New York', 'Washington']
    month_options = ['All', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    day_options = ['All', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    
    bs_data = pd.DataFrame({'A' : []}) # initially empty dataframe
    
    # Filter Information with default values
    selected_city = 'Chicago'
    selected_month = 'All'
    selected_day= 'All'
    
    # Travel Time Information
    popular_month = ''
    popular_day = ''
    popular_hour = ''
    
    # Travel Station
    pop_start_station = ''
    pop_end_station = ''
    pop_start_end = ''
    
    # Trip Duration
    total_trip_duration = ''
    average_trip_duration = ''
    total_trip_duration = ''
    total_trip_duration = ''
    
    # Users
    customer_count = ''
    subscriber_count = ''
    dependent_count = ''
    male_count = ''
    female_count = ''
    youngest = ''
    oldest = ''
    pop_age = ''
    pop_age_range = ''
    

    def load_data(self):
        """
        Loads data for the specified city and filters by month and day if applicable.
    
        Returns:
            df - Pandas DataFrame containing city data filtered by month and day
        """
    
        CITY_DATA = { 'Chicago': 'data_files/chicago.csv',
                  'New York': 'data_files/new_york_city.csv',
                  'Washington': 'data_files/washington.csv' }
    
        # load data file into a dataframe
        df = pd.read_csv(CITY_DATA[self.selected_city])
    
        # convert the Start Time column to datetime
        df['Start Time'] = pd.to_datetime(df['Start Time'])
    
        # extract month and day of week from Start Time to create new columns
        df['month'] = df['Start Time'].dt.month
        df['day_of_week'] = df['Start Time'].dt.weekday_name
    
        # filter by month if applicable
        if self.selected_month != 'All':
            # use the index of the months list to get the corresponding int
            month = self.month_options.index(self.selected_month)
    
            # filter by month to create the new dataframe
            df = df[df['month'] == month]
    
        # filter by day of week if applicable
        if self.selected_day != 'All':
            # filter by day of week to create the new dataframe
            df = df[df['day_of_week'] == self.selected_day.title()]
    
        self.bs_data =  df

    
    def time_stats(self):
         df = self.bs_data
         # Find moust popular month and day from their added columns
         month = df['month'].mode()[0]
         self.popular_month = self.month_options[month]
         self.popular_day = df['day_of_week'].mode()[0]         
         # Create an hour column and find the most popular hour
         df['hour'] = df['Start Time'].dt.hour
         self.popular_hour = str(df['hour'].mode()[0])
         
    def station_stats(self):
        df = self.bs_data
        self.pop_start_station = df['Start Station'].mode()[0] 
        self.pop_end_station = df['End Station'].mode()[0] 
        df['Start End Stations'] = df['Start Station'] + " >> "+ df['End Station']
        self.pop_start_end = df['Start End Stations'].mode()[0] 

    def duration_stats(self):
        df = self.bs_data
        self.average_trip_duration = str(round(df["Trip Duration"].mean()/60, 2))
        self.total_trip_duration = str(round(df["Trip Duration"].sum()/60, 2))
        self.min_trip_duration = str(round(df["Trip Duration"].min()/60, 2))
        self.max_trip_duration = str(round(df["Trip Duration"].max()/60, 2))
        
    def user_stats(self):
        df = self.bs_data
        self.customer_count = (df['User Type'] == 'Customer').sum()
        self.subscriber_count = (df['User Type'] == 'Subscriber').sum()
        self.dependent_count = (df['User Type'] == 'Dependent').sum()
        # Gender and age infromation is not available in all cities
        try:
            self.male_count = (df['Gender'] == 'Male').sum()
            self.female_count = (df['Gender'] == 'Female').sum()
            now = datetime.datetime.now()
            df['User Age'] = now.year - df['Birth Year']
            self.youngest = str(df['User Age'].min())
            self.oldest = str(df['User Age'].max()) 
            self.pop_age = str(df['User Age'].mode()[0])
            df['Age Range'] = pd.cut(df['User Age'], [0, 10, 14, 18, 29, 39, 49, 65, 140], labels=['0-10', '10-14', '14-18', '18-29', '29-39', '39-49', '49-65', '65-140'])
            self.pop_age_range = str(df['Age Range'].mode()[0])    
        except:
            # nothing to be done for this one
            pass
        
    def analyse_data(self):
        try:
            self.errors.clear()
            self.time_stats()
            self.station_stats()
            self.duration_stats()
            self.user_stats()   
        except IndexError as e:
            self.errors.append("No Data Available for the selected parameters... Please try again")     
            
        except Exception as e:
            self.errors.append("Error Occured: " + str(e))     
       
       
       
     

        
        
        
          
                       