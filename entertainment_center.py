# ---------------------------------------------------------------------#
#  Udacity Course: Full Stack Web Developer
#  Proj #1: Movie Website
#  Purpose: write server-side code to store a list of favorite movies,
#            including box art imagery and a movie trailer URL. Code
#            is used to generate a static web page allowing visitors to
#            browse a set of movies and watch the trailers.
#  File:    entertainment_center
# 
# ---------------------------------------------------------------------
#  DISCLAIMER: Most of fresh_tomatoes and media file is borrowed from 
#              code provided in "Programming Foundations with Python". 
#
#              Even though I didn't pay for a private GitHub
#              repository, please do not alter this code unless
#              you are an Udacity instructor. Initially at least
#              I would like to make my own homework mistakes.  ;-)
#
#              Many thanks. -- Paul
# ---------------------------------------------------------------------
#  PPC | 01/04/2018 | Original code.
#  PPC | 01/05/2018 | Move to GitHub and add header. 
# ---------------------------------------------------------------------
import os

# Std lib code for handling CSV files. See https://docs.python.org/2/library/csv.html 
import csv

# CSF File handling code to get raw movie data
import ec_create_csv
import ec_read_csv

# Import fresh_tomatoes file which creates HTML elements 
import fresh_tomatoes

# Import media file which defines Movie class. 
import media

ec_movie_list = []

def find_movies():
    # Load Movies into array from file if exists / otherwise create if not exist
    if not os.path.isfile('./ec_movie_list.csv'):
        ec_create_csv.create_movie_csv()    
    ec_movie_list = ec_read_csv.read_movie_csv()
    
    # Locate all movies in the array db (simulates user searching on web page)
    #  index = 99 id not found in CSV file.
    m1_idx = find_one_movie("Toy Story", ec_movie_list)
    m2_idx = find_one_movie("Avatar", ec_movie_list)
    m3_idx = find_one_movie("Ender's Game", ec_movie_list)
    m4_idx = find_one_movie("School of Rock", ec_movie_list)
    m5_idx = find_one_movie("Avengers", ec_movie_list)
    m6_idx = find_one_movie("Jesus of Nazareth", ec_movie_list)

  
    # If movie found in array, make class movie instance from each array row
    nbrmov = 0
    
    if (m1_idx != 99):
        toy_story = media.Movie(ec_movie_list[m1_idx][0],
                                ec_movie_list[m1_idx][1],
                                ec_movie_list[m1_idx][2],
                                ec_movie_list[m1_idx][3])
        nbrmov += 1
    if (m2_idx != 99):
        avatar = media.Movie(ec_movie_list[m2_idx][0],
                                ec_movie_list[m2_idx][1],
                                ec_movie_list[m2_idx][2],
                                ec_movie_list[m2_idx][3])
        nbrmov += 1
    if (m3_idx != 99):
        endersgame = media.Movie(ec_movie_list[m3_idx][0],
                                ec_movie_list[m3_idx][1],
                                ec_movie_list[m3_idx][2],
                                ec_movie_list[m3_idx][3])
        nbrmov += 1
    if (m4_idx != 99):
        school_of_rock = media.Movie(ec_movie_list[m4_idx][0],
                                ec_movie_list[m4_idx][1],
                                ec_movie_list[m4_idx][2],
                                ec_movie_list[m4_idx][3])
        nbrmov += 1
    if (m5_idx != 99):
        avengers = media.Movie(ec_movie_list[m5_idx][0],
                                ec_movie_list[m5_idx][1],
                                ec_movie_list[m5_idx][2],
                                ec_movie_list[m5_idx][3])
        nbrmov += 1
    if (m6_idx != 99):
        jesus = media.Movie(ec_movie_list[m6_idx][0],
                                ec_movie_list[m6_idx][1],
                                ec_movie_list[m6_idx][2],
                                ec_movie_list[m6_idx][3])
        nbrmov += 1

    # If everything found, then build website
    if (nbrmov == 6):
        # Create Python array with all movie Class instances!
        #   Why can't Class instant names be generic or created by code
        movies = [jesus, toy_story, avatar, endersgame, school_of_rock, avengers]
        fresh_tomatoes.open_movies_page(movies)    # Create page and display in browser
    else:
        print(m1_idx, m2_idx, m3_idx, m4_idx, m5_idx, m6_idx)
        print("One or more required movies not found in ec_movie_list.csv")
        print("Total movies = "+str(total_movies))
        print("Fresh Tomatoes website cannot be created.")             
    return 

def find_one_movie(searchMovie, myList):
    movie_found = 99
    
    for movie_nbr in range(0, 6):
        # print(movie_nbr, myList[movie_nbr][0], searchMovie)  
        if (myList[movie_nbr][0] == searchMovie):
            movie_found = movie_nbr

    return movie_found


# Main Path Code Here
find_movies()                   # In this file
