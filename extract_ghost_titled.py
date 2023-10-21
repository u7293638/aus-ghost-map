"""
This program extracts all the rows which contain the word 'Ghost' in the
title of the article.
"""
df
import re

# Keywords to search for in title
keywords = ["GHOST", "SPIRIT", "APPARITION", "PHANTOM"]
titles_to_drop = []

def extract_ghost_titles(filename):
    column_to_search = input("Which column do you want to search for your keywords? ")
    df = pd.read_csv(filename + ".csv")
    # Import the csv file
    df.fillna('None', inplace=True)

    # Remove articles that don't contain any keyword in their title
    for index, row in df.iterrows():
        if pd.isnull(df.iloc[index][column_to_search]):
            continue
        title = row[column_to_search].upper()
        for word in keywords:
            if word in title:
                # puts title in caps so duplicates can be removed later
                df.replace(row[column_to_search],title,inplace=True)
                print(str(index) + ": " + title)
                break
            elif word == "PHANTOM":
                print("FATALITY " + str(index) + ": " + title)
                titles_to_drop.append(index)

    # remove titles without keywords and with duplicates
    df.drop(titles_to_drop,inplace=True)
    df.drop_duplicates(subset=[column_to_search],inplace=True)

    # write to CSV file and save
    df.to_csv(filename + "_w_ghost_title.csv", index=True)
    print("--Program complete--")


        





