# Code by Miguel Gutiérrez Fernández - Delft University of Technology 
                            # Started Dec 2024

import pandas as pd
import numpy as np
import matplotlib 
import csv

movies_data = pd.read_csv("movies.csv")
ratings_data = pd.read_csv("ratings.csv")
links_data = pd.read_csv("links.csv")
tags_data = pd.read_csv("tags.csv")

print("movies data")
print(movies_data)
print("ratings data")
print(ratings_data)
print("links data")
print(links_data)
print("tags data")
print(tags_data)