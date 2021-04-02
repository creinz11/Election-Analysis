# The data we need to retrive
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate received
# 4. The total numbner of votes each candidate received
# 5. The winner of the election based on popular vote

#Add our dependencies
import csv
import os
#Assign a variable to load a file from path.
file_to_load = os.path.join("Resources", "election_results (1).csv")
#Assign a variable to save the file to a path
file_to_save = os.path.join('analysis', 'election_analysis.txt')

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes
candidate_options = []
#Declare empty dictionary
candidate_votes ={}

#Winning Candidate and Winning Count Tracker
winning_candidate = ''
winning_count = 0
winning_percentage = 0

#open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    #read and print the header row
    headers = next(file_reader)

    #print each row in the CSV File
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes +=1

        # Print the candidate name for each row.
        candidate_name = row[2]

        #If the candidate does not match any existing candidate..
        if  candidate_name not in candidate_options:
            #Add candidate name to the list of candidates.
            candidate_options.append(candidate_name)

            #begin tracking that candidates votes
            candidate_votes[candidate_name] = 0

            #Add a vote to the referenced candidate's count
        candidate_votes[candidate_name] += 1


#Determine the percentages of votes for each candidate by looping counts
# 1. Iterate thru candidate list
for candidate_name in candidate_votes:
    #2.Retrive vote of a candidate
    votes = candidate_votes[candidate_name]
    #3. calc the percent of votes
    vote_percentage = float(votes) / float(total_votes) * 100
    # to do: print out each candidate's name, vote count and percent to the terminal
    #Determin the winning vote count and candidate
    # votes to terminal
    print(f'{candidate_name}: {vote_percentage:.1f}% ({votes: ,})\n')
    #Determine if votes are greater than winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        #if true then set winning_count = votes and winning_percent =
        #vote_percentage
        winning_count = votes
        winning_percentage = vote_percentage
        #and set the winning_candidate = candidate_name
        winning_candidate = candidate_name

winning_candidate_summary = (
    f"------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count: ,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"------------------------\n")

print(winning_candidate_summary)

# to do: print out the winning candidate, vote count, and percent to term

    #4. print the candidate name and percent of votes & Total Votes
    #print(f'{candidate_name}: received {vote_percentage}% of the vote.')
    #print(candidate_votes)
