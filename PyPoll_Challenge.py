# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Declare a county names empty list to add to later & a county votes dictionary
county_names = []
county_votes = {}
# Initialize a total vote counter.
total_votes = 0
# Candidate Options as a list and candidate votes as a dictionary.
candidate_options = []
candidate_votes = {}
# Inittaite the winning parameters name, count & percentage & the county with the largest turnover
Winning_candidate = ""
Winning_count = 0
Winning_pecentage = 0
highest_county = ""
highest_turnout = 0
# Read the data file with csv reader function
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Identify the header row & test it
    headers = next(file_reader)
    print(headers)
# Initialize a county list to hold the county names & start the total votes counter
    for row in file_reader:
        total_votes +=1
        county_name = row[1]
        # add to the county name to the list if it's not there & initialize the county vote counter
        if county_name not in county_names:
            county_names.append(county_name)
            county_votes[county_name] = 0
        county_votes[county_name] += 1
        # Initialize the list of candidate names, add the names to the list & initialize the candidate vote counter
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1
    # Print the output
    print(county_names)
    print(county_votes)
    print(candidate_options)
    print(candidate_votes)
# Open the output text file as a write file
with open(file_to_save, "w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    txt_file.write(election_results)
    print(election_results, end="")
    txt_file.write("County Votes:\n")
    # Calculate countys' turnout percentage & print it in a statement    
    for county_name in county_names:
        county_total_votes = county_votes[county_name]
        county_percentage = float(county_total_votes)/float(total_votes)*100
        print(f"{county_name}: {county_percentage:.1f}% ({county_total_votes:,})\n")
        txt_file.write(f"{county_name}: {county_percentage:.1f}% ({county_total_votes:,})\n")
        # Identify the county with the highest turnout
        if (county_total_votes>highest_turnout):
            highest_turnout = county_total_votes
            highest_county = county_name
    highest_county_summary = (
            f"-------------------------\n"
            f"Largest County Turnout:{highest_county}\n"
            f"-------------------------\n")
    
    txt_file.write(highest_county_summary)
    # Calculate candidates' percentages & print them in a statement
    for candidate_name in candidate_options:
        candidate_total_votes = candidate_votes[candidate_name]
        candidate_percentage = float(candidate_total_votes)/float(total_votes)*100
        print(f"{candidate_name}: {candidate_percentage:.1f}% ({candidate_total_votes:,})\n")
        txt_file.write(f"{candidate_name}: {candidate_percentage:.1f}% ({candidate_total_votes:,})\n")
        # Determine the winning count, percentage & candidate
        if (candidate_total_votes>Winning_count) and (candidate_percentage>Winning_pecentage):
            Winning_count = candidate_total_votes
            Winning_candidate = candidate_name
            Winning_pecentage = candidate_percentage
    Winning_Candidate_Summary = (
            f"--------------------------\n"
            f"Winner:{Winning_candidate}\n"
            f"Winning Vote Count: {Winning_count:,}\n"
            f"Winning Percentage: {Winning_pecentage:.1f}%\n"
            f"---------------------------\n")
    txt_file.write(Winning_Candidate_Summary)
    print(Winning_Candidate_Summary)
    print(highest_county_summary)