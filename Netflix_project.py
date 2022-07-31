#This project requires 'netflix_data.csv' file
#The main objetive of this project are importing/manipulate the datas and plotting.

import pandas as pd
import matplotlib.pyplot as plt


#Creating years and durations lists and converting them to DF
years = [2011,2012,2013,2014,2015,2016,2017,2018,2019,2020]
durations = [103,101,99,100,100,95,95,96,93,90]
movie_dict = {"years": years,"durations":durations}
durations_df = pd.DataFrame(movie_dict)

#Asking if the user wants to plot the Year vs Durations
print('Would like to see the Year.vs.Durations plot? Type yes or no')
answer = input()
if answer == 'yes':
   fig = plt.figure()
   plt.plot(years, durations)
   plt.title("Netflix Movie Durations 2011-2020")
   plt.show()

#Reading the CSV files
netflix_df = pd.read_csv('netflix_data.csv')

#Subsetting the column 'Type' only for 'Movies' and selecting
netflix_df_movies_only = netflix_df[netflix_df["type"] == "Movie"]
netflix_movies_col_subset = netflix_df_movies_only[["title","country","genre","release_year","duration"]]

print('Would like to see the Movie filtered frame? Type yes or no')
answer = input()
if answer == 'yes':
   print(netflix_movies_col_subset[:5])

#Creating a scatter plot: Realese year vs duration
print('Would Like to plot the Realease Year vs Duration? Type yes or no')
answer = input()
if answer == 'yes':
   fig = plt.figure(figsize=(12, 8)) #Creating the figure and fitting to 12,8 size
   plt.scatter(netflix_movies_col_subset['release_year'], netflix_movies_col_subset['duration']) #Scatting the axis
   plt.title("Movie Duration by Year of Release")
   plt.show()

#Filtering Durations shorter than 60
short_movies = netflix_movies_col_subset[netflix_movies_col_subset['duration'] < 60]

#Creating a empty list for colors
colors = []

#Defining colors for genres
for lab, row in netflix_movies_col_subset.iterrows():
    if row['genre'] == "Children":
        colors.append("red")
    elif row['genre'] == "Documentaries":
        colors.append("blue")
    elif row['genre'] == "Stand-Up":
        colors.append("green")
    else:
        colors.append("black")

#Creating a Colorful scatter plot
print('Would like to create a colorful scatter plot which each color is a genre? Type yes or no')
answer = input()
if answer == 'yes':
    plt.style.use('fivethirtyeight')
    fig = plt.figure(figsize=(12, 8))
    plt.scatter(netflix_movies_col_subset["release_year"], netflix_movies_col_subset["duration"], c=colors)
    plt.title("Movie duration by year of release")
    plt.xlabel("Release year")
    plt.ylabel("Duration (min)")
    plt.show()




