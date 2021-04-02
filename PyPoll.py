# The data we need to retrive
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate received
# 4. The total numbner of votes each candidate received
# 5. The winner of the election based on popular vote

#Import the datetime clss from the datetime module
#import datetime
#now = datetime.datetime.now()
#print(now)

#Alternative date time
#import datetime as dt
#now = dt.datetime.now()
#print("it is currently", now)

#Import CSV
#import csv
#dir(csv)

#Assign variable to file path
#file_to_load = '/Users/cjreinhardt/Election-Analysis/Election-Analysis/Resources/election_results (1).csv'

#Open the election results and read the file
#election_data = open(file_to_load,'r')

#To do: perform analysis.

#Close the file
#election_data.close()

#open the election results and read the file
#with open(file_to_load) as election_data:
    #print(election_data)


#open the election results and read the file.
#election_data = open(file_to_load, 'r')
#with open(file_to_load) as election_data:
    #print the file object
    #print(election_data)

#create a filename variable to a direct or indirect path to the file
#file_to_save = os.path.join("analysis", "election_analysis.txt")
#using the open() function with w mode will write the data to the file
#outfile = open(file_to_save, 'w')
#write some data to the file.
#outfile.write("Hello World")
#close the file
#outfile.close

#using the with statement open the file as a text file
#with open(file_to_save, 'w') as txt_file:
    #txt_file.write('Arapahoe\nDenver\nJefferson')

#Add our dependencies
import csv
import os
#Assign a variable to load a file from path.
file_to_load = os.path.join("Resources", "election_results (1).csv")
#Assign a variable to save the file to a path
file_to_save = os.path.join('analysis', 'election_analysis.txt')

#open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    #read and print the header row
    headers = next(file_reader)
    print(headers)

