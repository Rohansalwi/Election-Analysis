import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("/Users/rohansalwi/Desktop/Assignment Projects/Python/Election-Analysis/Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("/Users/rohansalwi/Desktop/Assignment Projects/Python/Election-Analysis/Resources", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
# To do: read and analyze the data here.
   file_reader = csv.reader(election_data)
   headers = next(file_reader)
   print(headers)
   for row in file_reader:
    print(row)