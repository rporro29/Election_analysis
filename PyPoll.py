# The data we need to retrieve.
# 1. The total numbers of votes cast
# 2. A complete list of candidas who received votes 
# 4. The total number of votes each candidate won
# 5. The winner of the election based popular vote
import os
import csv
#file_to_load = 'Resources/election_results.csv'
#election_data = open(file_to_load, 'r')
#election_data.close()
#file_to_load = os.path.join("Resources", "election_result.csv")

#file_to_save = os.path.join("analysis", "election_analysis.txt")


#with open("election_results.csv", 'r') as election_data:
#    file_to_load = csv.reader(election_data, delimiter="," )
 #   for county in file_to_load:
  #      if county :="denver":
   #         print('we won')


#with open(file_to_load) as election_data:
 #   print(election_data)
    
#file_to_load = os.path.join("Election_analysis", "election_results.csv")


#with open(file_to_load) as election_data:
   # print(election_data)

#with open(file_to_load) as election_data:
       # print(election_data)

# Assign a variable for the file to load and the path.
###file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
###with open(file_to_load) as election_data:

    # Print the file object.
     ###print(election_data)

# Create a filename variable to a direct or indirect path to the file.
#file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
#open(file_to_save, "w")

# Create a filename variable to a direct or indirect path to the file.
#file_to_save = os.path.join("analysis", "election_analysis.txt")

#Use the open statement to open the file as a text file.
#outfile = open(file_to_save, "w")
 #Write some data to the file.
#outfile.write("Hello World")

# Close the file
#outfile.close()

# Create a filename variable to a direct or indirect path to the file.
#file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
#with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
     # txt_file.write("Counties in the Election\n")
      #txt_file.write("---------------------------\n")
      #txt_file.write("Arapahoe\nDenver\nJefferson")

      # Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
 # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    #for row in file_reader:
     #   print(row[0])
    headers = next(file_reader)
    print(headers)