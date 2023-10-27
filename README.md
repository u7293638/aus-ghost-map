# Australian Ghost Map
Map of Ghost Stories in Tasmania and Australia, extracted from Trove data

## Pipeline
To put Trove data through the pipeline to result in a csv file with placenames and coordinates:
1. Download data using Trove in-built bulk download or Trove Web Harvester 
2. Run extract_ghost_titled on the csv file of trove data
3. Change column name at the end of the "extract_placenames.py" file to whichever column you wish to extract placenames from
4. Run extract_placenames on the output csv file from Step 2
5. If you get a lot of placenames you don't want, you can try and filter some of these out by running the file through remove_foreign_places.py (add in any places you want to remove in the "keywords" list)
6. Run get_coordinates on the output csv file from Step 4
7. Your final csv file should have the title [original file name]_w_coords