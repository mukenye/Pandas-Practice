import pandas as pd

# loaded the data
data = pd.read_csv('courses.csv')

# created a dictionary to store the flexibility measure for each area
flexibility = {}

# looped through each area
for area in data['area'].unique():
    
	# selected the courses in the current area
	area_courses = data[data['area']==area]
    
	# calculated the total credits for the current area
	total_credits = area_courses['credits'].sum()
    
	# calculated the total credits of courses that have prerequisites
	prereq_credits = area_courses[area_courses['prereq_type']!='None']['credits'].sum()
    
	# calculated the flexibility measure for the current area
	if total_credits > 0:
    	flexibility[area] = 1 - (prereq_credits/total_credits)
	else:
    	flexibility[area] = 0
   	 
# created a pandas dataframe to display the flexibility measure for each area
flexibility_df = pd.DataFrame({'area': list(flexibility.keys()), 'flexibility': list(flexibility.values())})

# sorted the dataframe by flexibility in descending order
flexibility_df = flexibility_df.sort_values(by=['flexibility'], ascending=False)

# displayed the dataframe
print(flexibility_df.head(10))


