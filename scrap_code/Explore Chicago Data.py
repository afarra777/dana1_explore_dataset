# -*- coding: utf-8 -*-
"""
Exploring Chicago Bike Share Dataset

"""
import pandas as pd
import datetime

df = pd.read_csv("chicago.csv")
print(df.columns)
print('\n ************************************************* \n')

# start by viewing the first few rows of the dataset!
print(df.info())  
print('\n ************************************************* \n')


# convert the Start Time column to datetime
df['Start Time'] = pd.to_datetime(df['Start Time'])


# extract hour from the Start Time column to create an hour column
df['hour'] = df['Start Time'].apply(lambda n: n.hour)

print(df.info()) 
print('\n ************************************************* \n')

print(df['Start Station'].mode()[0]) 
print(df['End Station'].mode()[0])
print('\n ************************************************* \n')


print(df['User Type'].value_counts())
print('\n ************************************************* \n')


now = datetime.datetime.now()
df['User Age'] = now.year - df['Birth Year']
print(df['User Age'].min())
print(df['User Age'].max())
print(df['User Age'].mean())
print(df['User Age'].mode()[0])

print('\n ************************************************* \n')

df['Age Range'] = pd.cut(df['User Age'], [0, 10, 14, 18, 29, 39, 49, 59, 120])
print(df['Age Range'].mode()[0])
print('\n ************************************************* \n')


print(df['Birth Year'].min())
print(df['Birth Year'].max())
print(df['Birth Year'].mean())
print(df['Birth Year'].mode()[0])
print(df['Birth Year'].median())

print('\n ************************************************* \n')

# Counting Values
print( df.loc[df['User Type'] == 'Customer', 'User Type'].count() )

print((df['User Type'] == 'Customer').sum())

print(df[df['User Type'] == "Customer"]['User Type'].count())


print(type(df[df['User Type'] == "Customer"]))

print(df['Gender'].value_counts())
print('\n ************************************************* \n')

