# Election_Analysis
## Overview
This analysis uses Python & Visual Studio code to perform an election audit of the tabulated results for a US congressional precinct in Colorado. The output should analyze the election results, votes, county turnout & determine the winner.
### Background
The data used to perform this analysis is pulled from a csv file showing the Ballot ID of each voter, which county they are in, and the name of the candidate they cast their vote for. The following link shows the used data:
https://github.com/Lamismn/Election_Analysis/blob/main/Resources/election_results.csv
### Purpose
The purpose of this analysis is to use Python coding to audit the election results in the file identifying the following:
1. The total number of votes cast in the elections, as well as the number & percentage of votes of each county
2. The total number of votes cast for each candidate & the percentage they got of the total votes
3. The winning candidate based on the popular vote

The analysis shoud also provide an output text file with this summary
## Results
After using Python to analyze the data provided, the following screenshot shows the output concluded:

<img width="296" alt="Capture" src="https://user-images.githubusercontent.com/79733383/111920472-91f4c680-8a65-11eb-82a6-e844b9dc2f72.PNG">

Based on the shown image, the results are as follows:
1. The total number of votes cast was 369,711 votes
2. There are three counties in this precinct; Jefferson, Denver & Arapahoe. Their respective number of votes & percentage of turnout are as follows:
   - Jefferson: 38,855 votes, percentage of 10.5% of the total vote count
   - Denver: 306,055 votes, percentage of 82.8% of the total vote count
   - Arapahoe: 24,801 votes, percentage of 6.7% of the total vote count
3. The County with the highest turnout is Denver, with a total number of votes of 306,055 votes and a percentage of 82.8% of the total votes cast in the precinct
4. There are thre candidates in this election; Charles Casper Stockham, Diana DeGette, and Raymon Anthony Doane. Their respective number of votes won and percentages are as follows:
   - Charles Casper Stockham: Won 85,213 votes, with a percentage of 23.0%  of the total vote count
   - Diana DeGette: Won 272,892 votes, with a percentage of 73.8% of the total vote count
   - Raymon Anthony Doane: Won 11,606 votes, with a percentage of 3.1% of thetotal vote count
6. Based on these results, the winner of this election with a big gap is Diana DeGette, with a total number of votes won of 272,892 & a percentage of 73.8% of the total votes.
## Summary
This analysis used Python coding to calculate & document the results of a Colorado congressional precinc with three counties and three candidates. Python made it really easy to go through more than 350,000 votes and classify them to show the winner, the county with the highest turnout as well as produce an output text file summarizing the results, which is not possible using Excel & VBA.

The script written for this analysis can be used on any other election, verses doing the analysis on Excel, this saves a lot of time & help standardize the expected output of any analysis. For any election data saved in the same csv format, we could use it without modification, and minor modifications could be made to allow for using it on more diverse results, for example, we could use more lines instead of line 7, to reference more files and allow for using it on multiple data files.

Another modification to allow for using it on a higher scale, is writing a script to analyze the votes each candidate got from each county, this would allow for using the script on regional as well as central election, if a voter gives votes to candidates on each level at the same time. This could be achieved by adding a dictionary for each county at the begining and where the candidate name is the key and the votes they got in this county is the value.

<img width="691" alt="Capture 4" src="https://user-images.githubusercontent.com/79733383/111925254-70ec9f80-8a7e-11eb-9a05-1a3281c19f18.PNG">
