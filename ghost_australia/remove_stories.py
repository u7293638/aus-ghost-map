"""
This program extracts all the rows which contain the word 'Ghost' in the
title of the article.
"""
import pandas as pd
import re

# Keywords to search for in title
keywords = ["CHAPTER"]
titles_to_drop = []

filename = input("Name of file: ")

def remove_stories(filename):
    column_to_search = input("Which column do you want to search for your keywords? ")
    df = pd.read_csv(filename + "_w_ghost_title.csv")
    # Import the csv file
    df.fillna('None', inplace=True)

    # Remove articles that don't contain any keyword in their title
    for index, row in df.iterrows():
        if pd.isnull(df.iloc[index][column_to_search]):
            continue
        title = row[column_to_search].upper()
        for word in keywords:
            if word in title:
                print("FATALITY " + str(index) + ": " + title)
                titles_to_drop.append(index)
                
                break
            elif word == "CHAPTER":
                # puts title in caps so duplicates can be removed later
                df.replace(row[column_to_search],title,inplace=True)
                print(str(index) + ": " + title)
                

    # remove titles without keywords and with duplicates
    df.drop(titles_to_drop,inplace=True)
    df.drop_duplicates(subset=[column_to_search],inplace=True)

    # write to CSV file and save
    df.to_csv(filename + "_w_ghost_title.csv", index=True)
    print("--Program complete--")

remove_stories(filename)