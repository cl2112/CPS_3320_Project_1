#===============================================================================
# Name: Christian Liguori
# Project 1
# Date: 03/03/21
#===============================================================================

###---------------###
###--- Imports ---###
###---------------###
import pandas # Data Library that is used for parsing and querying data.
import matplotlib.pyplot as plt # Plotting Library used to display graphs.


###--------------------------------------------###
###--- Importing and Formatting the Data Set ---###
###--------------------------------------------###
# Importing and parsing the data using the pandas library. The file is in
#   .CSV format. The 'Date Made Public' field is explicitly converted to a 
#   datetime.
breachDataSet = pandas.read_csv(
    './PRC Data Breach Chronology - 1.13.20.csv',
    parse_dates=['Date Made Public']
)

###------------------------------------------------------------###
###--- Parsing and Extracting Information from the Data Set ---###
###------------------------------------------------------------###
# The total number of breaches. Count of each row in the data set.
numberOfBreaches = len(breachDataSet)

# Creating a subset of data that only contains breaches of type 'HACK' and
#   storing it in a variable.
hacksDataSet = breachDataSet[breachDataSet["Type of breach"] == 'HACK']
# The total number of breaches by hacks. Count of each row in the data subset.
numberOfHacks = len(hacksDataSet)

# Creating a subset of data that only contains breaches of type 'HACK' and 
#   organization of type 'MED' and storing it in a variable.
medDataSet = hacksDataSet[hacksDataSet['Type of organization'] == "MED"]
# The total number of breaches by hacks of MED organizations. Count of 
#   each row in the data subset.
numberOfMedHacked = len(medDataSet)

# Creating a subset of data that only contains breaches of type 'HACK' and 
#   organization of type 'BSF' and storing it in a variable.
bsfDataSet = hacksDataSet[hacksDataSet['Type of organization'] == "BSF"]
# The total number of breaches by hacks of BSF organizations. Count of 
#   each row in the data subset.
numberOfBsfHacked = len(bsfDataSet)


###------------------------------------------------###
###--- Calculations and Analysis of Information ---###
###------------------------------------------------###
# Calculating what percentage of breaches are hacks.
percentageOfBreachesByHacks = numberOfHacks/numberOfBreaches * 100

# Calculating what percentage of hacks affect MED organizations.
percentageOfMedHacked = numberOfMedHacked/numberOfHacks * 100

# Calculating what percentage of hacks affect BSF organizations.
percentageOfBsfHacked = numberOfBsfHacked/numberOfHacks * 100

# Determining the type of organization most affected by breaches by hacks.
mostAffectedByHacks = 'medical' if percentageOfMedHacked > \
    percentageOfBsfHacked else 'financial'


###-------------------------------------------###
###--- Presenting Findings and Conclusions ---###
###-------------------------------------------###
# (Code was split to avoid long lines and improve readability)
print('\n###--- REPORT ---###')

# Display total number of breaches in the data set.
print('There were ' + str(numberOfBreaches) + ' breaches reported.')

# Display total number of hacks.
print('Of those breaches, there were ' + str(numberOfHacks) + ' breaches ' + \
    'due to hacks. (Defined as "Hacked by an Outside Party or ' + \
    'Infected by Malware")')

# Display percentage of hack breaches.
print('That is {:.2f}% of all breaches were due to \
hacks.'.format(percentageOfBreachesByHacks))

# Display the count and percentage of hacks affecting MED organizations.
print('\nThe number of hacks that affected medical organizations (Healthcare, \
Medical Providers and Medical Insurance Services) is ' + \
str(numberOfMedHacked) + '.')
print('The percentage of hacks affecting medical organizations is \
{:.2f}%.'.format(percentageOfMedHacked))

# Display the count and percentage of hacks affecting MED organizations.
print('\nThe number of hacks that affected financial organizations (Financial \
and Insurance Services) is ' + str(numberOfBsfHacked) + '.')
print('The percentage of hacks affecting financial organizations is \
{:.2f}%.'.format(percentageOfBsfHacked))

# Display which service is successfully attacked more by hackers.
print('\nComparing the count and percentages of hacks on medical ' + \
'organizations and on financial organizations ' + \
'it is clear that ' + mostAffectedByHacks + \
' organizations have been affected by hacks the most out of the two.')

###--- Bar Graphs ---###
# Ask user if they would like to see the data presented in bar graph form.
if input('\nWould you like to see the information displayed in ' + \
'bar graphs? (Y/N): ').lower() == 'y':
    # Present Information as Bar Graphs.
    # Create subset of hacks of both MED and BSF and count occurrences.
    medAndBsfHacks = hacksDataSet[(hacksDataSet['Type of organization'] == \
    'MED') | (hacksDataSet['Type of organization'] == 'BSF')]
    
    # Create bar graph of count of hacks of affecting MED and BSF organizations.
    medAndBsfHacks['Type of organization'].value_counts().plot.bar(title=\
    'Number of Hacks of Type MED and BSF')
    plt.show() # Display bar graph.

    # Create bar graph of count of breaches of all types affecting 
    #   MED organizations.
    breachDataSet[breachDataSet['Type of organization'] == 'MED']\
    ['Type of breach'].value_counts().plot.bar(title=\
    'Count of Breaches of All Types Affecting Med Organizations')
    plt.show() # Display bar graph.

    # Create bar graph of the count of each type of breach.
    breachDataSet["Type of breach"].value_counts().plot.bar(title=\
    'Count of Breaches by Type of Breach')
    plt.show() # Display bar graph.
    
    # Create bar graph of the count of breaches by hacks by type of organization.
    hacksDataSet['Type of organization'].value_counts().plot.bar(title=\
    'Count of Breaches by Hacks by Type of Organization')
    plt.show() # Display bar graph.
