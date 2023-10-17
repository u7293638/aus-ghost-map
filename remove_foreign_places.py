"""
This program extracts all the rows which contain the word 'Ghost' in the
title of the article.
"""
import pandas as pd
import re

# Keywords to search for in title
keywords = ["NEW YORK", "NEW ZEALAND", " NEW ", "SOUTHERN", "FRANCE", "LONDON", "YORK", "JAPANESE", 
    "SCOTLAND", "FRENCH", "ENGLAND", "ITALIAN", "BRITISH", "PARIS", "IRISH", "VESUVIUS", 
    "BRIGHTON", "AMERICAN", "SPANISH", "ENGLISH", "CALIFORNIA"]


filename = input("Name of file: ")

def remove_stories(filename):
    column_to_search = input("Which column do you want to search for your keywords? ")
    df = pd.read_csv(filename + "_w_placenames.csv")
    # Import the csv file
    df.fillna('None', inplace=True)

    # Remove articles that don't contain any keyword in their title
    for index, row in df.iterrows():
        if pd.isnull(df.iloc[index][column_to_search]):
            continue
        places = row[column_to_search].upper()
        for word in keywords:
            if word in places:
                altered_places = places.replace(word,'')
                df.replace(row[column_to_search],altered_places,inplace=True)
                print(str(index) + ': ' + word + " REMOVED")
            else:
                continue
                

    # remove titles without keywords and with duplicates

    # write to CSV file and save
    df.to_csv(filename + "_w_foreign_removed.csv", index=True)
    print("--Program complete--")

remove_stories(filename)