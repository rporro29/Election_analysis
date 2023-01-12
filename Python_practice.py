#print("Hello World")
#counties = ["Arapahoe", "Denver", "Jefferson"]
#if counties[1] == "Denver":
    #print(counties[1])

#temperature = int(input("What is the temperature outside? "))

#if temperature > 80:
   # print("Turn on the AC.")
#else:
    #print("Open the windows.")

# What is the score?
#score = int(input("What is your test score? "))

# Determine the grade.
#if score >= 90:
 #   print('Your grade is an A.')
#elif score >= 80:
#    print('Your grade is a B.')
#elif score >= 70:
#    print('Your grade is a C.')
#elif score >= 60:
 #   print('Your grade is a D.')
#else:
 #   print('Your grade is an F.')
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
counties =["Arapahoe", "Denver", "Jefferson"]
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

#if "El Paso" in Counties:
 #   print("El Paso is in the list of counties.")
#else:
 #       print("El Paso is not in the list of counties.")

#x = 0
#while x <= 5:
    ### x = x + 1
#counties = ["Arapahoe","Denver","Jefferson"]

#for county in counties:
    #print(county)

#numbers = [0, 1, 2, 3, 4]
#for num in numbers:
    #print(num)


#for num in range(5):
    #print(num)

#for i in range(len(counties)):
    #print(counties[i])


#for county in counties_dict.keys():
    #print(counties_dict.keys())

#for voters in counties_dict.values():
    #print(voters)
#for county in counties_dict:
    #print(counties_dict[county])

#for county in counties_dict:
    #print(counties_dict.get(county))

#for county, voters in counties_dict.items():
   ##for county_dict in voting_data:
    #print(county_dict)

#for i in range(len(voting_data)):

     #print(voting_data[i]['county'])

#for county, voters in counties_dict.items():
    #print(f"{county} county has {voters} registered voters.")

#for county_dict in voting_data:
   # for value in county_dict.values():
        #print(value)

#for county_dict in voting_data:
    #print(county_dict['county'])

#candidate_votes = int(input("How many votes did you get in the election? "))
#total_votes = int(input("What is the total votes in the election? "))
#message_to_candidate = (
    
    #f"You received {candidate_votes:,} number of votes. "

    
   # f"The total number of votes in the election was {total_votes:,}. "
    
   # f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

#print(message_to_candidate)


for votes in voting_data:
    print(f'{votes["county"]} has {votes["registered_voters"]:,} registered voters')