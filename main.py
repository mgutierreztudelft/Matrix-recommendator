# Code by Miguel Gutiérrez Fernández - Delft University of Technology 
                            # Started Dec 2024

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import csv

movies_data = pd.read_csv("movies.csv")
ratings_data = pd.read_csv("ratings.csv")
links_data = pd.read_csv("links.csv")
tags_data = pd.read_csv("tags.csv")

def view_head_and_tail(data): # input is a DataFrame, output is the head and tail of said dataframe

    head = data.head() # views the top rows of the DataFrame "data"
    print(head)
    tail = movies_data.tail() # views the last rows of the DataFrame "data"
    print(tail)

    return head, tail

def get_avg_per_user(ratings_data): # input is the ratings data, output is the avg of rating given per person

    mov_id = ratings_data.loc[:,"movieId"]
    user_id = ratings_data.loc[:,"userId"]
    rating = ratings_data.loc[:,"rating"]


    user_size = user_id.size
    last_user = user_id[user_size-1]
    totalpoints = np.zeros(last_user)
    totalpoints[0] = rating[0] # initialize the starting count
    films_rated = np.zeros(last_user)

    for user in range(user_size):
        if user != 0:
            if user_id[user] == user_id[user-1]:
                films_rated[user_id[user]-1] = films_rated[user_id[user]-1] + 1
                totalpoints[user_id[user]-1] = rating[user] + totalpoints[user_id[user]-1]
            else:
                totalpoints[user_id[user]-1] = rating[user]
                films_rated[user_id[user]-1] = 1

        else:
            totalpoints[0] = rating[0] # initialize the starting count
            films_rated[0] = 1


    average_rating_user = np.zeros(last_user)
    for user in range(last_user):
        average_rating_user[user] = totalpoints[user]/films_rated[user]
    # print(totalpoints)
    # print(films_rated)

    return average_rating_user, films_rated

[avg_rg_per_user, films_rated] = get_avg_per_user(ratings_data)

plt.scatter(films_rated[:], avg_rg_per_user[:], s = 3)
plt.xlabel("Number of rated films")
plt.ylabel("Rating")

plt.show()