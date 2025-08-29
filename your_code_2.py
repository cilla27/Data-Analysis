import pandas as pd
df = pd.read_csv('GoogleApps.csv')

# What is the price of the cheapest paid app (type == 'Paid')?
print(df[df['Type'] == 'Paid']['Price'].min())
#0.99

# What is the median number of installs
# for the applications from the "ART_AND_DESIGN" category?
print(df[df['Category'] == 'ART_AND_DESIGN']['Installs'].median())
#100000.0

# How much more is the maximum number of Reviews for free apps (type == 'Free')
# than the maximum number of Reviews for paid apps (Type == 'Paid')?
free = df[df['Type'] == 'Free']['Reviews'].max()
paid = df[df['Type'] == 'Paid']['Reviews'].max()
print(free - paid)
#44703802

# What is the minimum size of an application for teenagers (Content Rating == 'Teen')?
print(df[df['Content Rating'] == 'Teen']['Size'].min())
# 0.3154296875 

# *What is the category of an app having the most number of reviews?
print(df[df['Reviews'] == df['Reviews'].max()]['Category'])
#GAME

# *What is the mean rating of applications which price exceeds $20 and 
# the number of installs is over 10,000?
print(df[(df['Price']>20) & (df['Installs']>10000)]['Rating'].mean())
#4.25