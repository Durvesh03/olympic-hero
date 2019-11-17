# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path

#Code starts here
data = pd.read_csv(path)
data.rename(columns={'Total' : 'Total_Medals'}, inplace = True)
data.head()


# --------------
#Code starts here




data['Better_Event'] = np.where(data['Total_Summer'] > data['Total_Winter'],'Summer','Winter')
data['Better_Event'] = np.where(data['Total_Summer'] == data['Total_Winter'], 'Both', data['Better_Event'])
better_event_Summer = data[data['Better_Event'] == 'Summer']['Better_Event'].value_counts()
better_event_Winter = data[data['Better_Event'] == 'Winter']['Better_Event'].value_counts()
if int(better_event_Summer) > int(better_event_Winter) :
    better_event = 'Summer'
else:
    better_event = 'Winter'

    
print(better_event)



# --------------
#Code starts here







#top_countries = data[data['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]
top_countries = data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]
#top_countries = top_countries.drop(top_countries.tail(1).index, inplace = True)
top_countries = top_countries[:-1]
#print(top_countries.tail(2))
def top_ten(df,colname):
    country_list = []
    topTen = df.nlargest(10,colname)
    country_list = list(topTen['Country_Name'])
    return country_list

top_10_summer = top_ten(top_countries,'Total_Summer')
top_10_winter = top_ten(top_countries,'Total_Winter')
top_10 = top_ten(top_countries,'Total_Medals')
common = list(set(top_10_summer) & set(top_10_winter) & set(top_10))
print(common)








# --------------
#Code starts here
summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]

summer_df[['Country_Name','Total_Summer']].plot(kind = 'bar')
winter_df[['Country_Name','Total_Winter']].plot(kind = 'bar')
top_df[['Country_Name','Total_Medals']].plot(kind = 'bar')





# --------------
#Code starts here
summer_df['Golden_Ratio'] = summer_df['Gold_Summer'] / summer_df['Total_Summer']
summer_max_ratio = summer_df['Golden_Ratio'].max()
summer_country_gold = summer_df['Country_Name'][summer_df['Golden_Ratio']==summer_max_ratio].iloc[0]
winter_df['Golden_Ratio'] = winter_df['Gold_Winter'] / winter_df['Total_Winter']
winter_max_ratio = winter_df['Golden_Ratio'].max()
winter_country_gold = winter_df['Country_Name'][winter_df['Golden_Ratio']==winter_max_ratio].iloc[0]
top_df['Golden_Ratio'] = top_df['Gold_Total'] / top_df['Total_Medals']
top_max_ratio = top_df['Golden_Ratio'].max()
top_country_gold = top_df['Country_Name'][top_df['Golden_Ratio']==top_max_ratio].iloc[0]



# --------------
#Code starts here
data_1 = data[:-1]
#data_1 = data.iloc[:1]
data_1['Total_Points'] = (data_1['Gold_Total']*3) + (data_1['Silver_Total']*2) + data_1['Bronze_Total']
most_points = data_1['Total_Points'].max()
best_country = data_1['Country_Name'][data_1['Total_Points']==most_points].iloc[0]








# --------------
#Code starts here
best = data[data['Country_Name']==best_country]
best = best[['Gold_Total','Silver_Total','Bronze_Total']]
best.plot.bar()
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation = 45)





