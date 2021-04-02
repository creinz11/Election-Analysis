#Data we need to retrieve
# 1. The total number of votes cast
# 2. Complete list of candidates who receive votes
# 3. The percentage of votes each candidate received
# 4. Total number of votes each candidate received
# 5. The winner of the election based on the popular vote

# Import the date time class form datetime moduel
#import datetime
#now = datetime.datetime.now()
#print("The time right now is ", now)

# can abbreviate date time as dt
#import datetime as dt
#now = dt.datetime.now()
#print("The current time is ", now)

#load in CSV
file_to_load = 'iCloud Drive/Desktop/Election_Analysis/Resources/election_results.csv'

#Open the election results 
election_data = open(file_to_load, 'r')