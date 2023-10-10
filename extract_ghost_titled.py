"""
This program extracts all the rows which contain the word 'Ghost' in the
title of the article.
"""
import pandas as pd
import re

# Keywords to search for in title
keywords = ["GHOST", "GHOST'S", "GHOSTS", "SPIRIT", "SPIRITS", "APPARITION", "PHANTOM"]
titles_to_drop = []

filename = input("Filename: ")
# Import the csv file
df = pd.read_csv(filename + ".csv")
df.fillna('None', inplace=True)

# Remove articles that don't contain any keyword in their title
for index, row in df.iterrows():
    if pd.isnull(df.iloc[index]['heading']):
        continue
    title = row["heading"].upper()
    for word in keywords:
        if word in title:
            # puts title in caps so duplicates can be removed later
            df.replace(row["heading"],title,inplace=True)
            print(str(index) + ": " + title)
            break
        elif word == "PHANTOM":
            print("FATALITY " + str(index) + ": " + title)
            titles_to_drop.append(index)

# remove titles without keywords and with duplicates
df.drop(titles_to_drop,inplace=True)
df.drop_duplicates(subset=["heading"],inplace=True)

# write to CSV file and save
df.to_csv(filename + "_w_ghost_title.csv", index=True)
print("--Program complete--")


        





