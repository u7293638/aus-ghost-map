import pandas as pd

df = pd.read_csv('records_w_placenames.csv')

for index, row in df.iterrows():
    if placename != "":
        url = "http://tlcmap.org/ghap/search?fuzzyname=" + placename + "&state=TAS"
        sitetext = urllib.request.urlopen(url).read()
        html = HTMLParser(sitetext)

