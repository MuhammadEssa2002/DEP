# Description: This file is used to analyze the data of the series and display the results in the form of graphs.
import pandas as pd #importing pandas library
import matplotlib.pyplot as plt #importing matplotlib library
import warnings #importing warnings library


warnings.filterwarnings(
    action='ignore', category=UserWarning, message=r"Boolean Series.*"
)

#####################################################################
# Reading the csv files
serise_name = pd.read_csv('title.basics.csv')
epi = pd.read_csv('title.episode.csv')
rating = pd.read_csv('title.ratings.csv')

#####################################################################
# Function to get the number of episodes in a season
def epi_number(se, serise_code):
    i = 0 
    for _ in epi[(epi.seasonNumber == se)&(epi.parentTconst==serise_code)].episodeNumber:
        i += 1
    return i

# Function to get the average rating of a season
def ratings(se, serise_code):
    l=0
    for i in epi[(epi.seasonNumber == se)&(epi.parentTconst==serise_code)].tconst:
        l = rating[rating.tconst == i].iloc[0].averageRating + l  
    return l/epi_number(se,serise_code) 



#####################################################################
# Displaying the top 10 series based on average rating
serise_name = serise_name.sort_values(by=['averageRating'], ascending=False)
top_serise = serise_name.iloc[0:10]
print('\n')
print('Top 10 Series Based on Average Rating')
print(top_serise[['primaryTitle','averageRating']].to_string(index=False))
ax = top_serise.plot(x='primaryTitle', y='averageRating', kind='bar',color='#53a8b6')
ax.set_facecolor('#bbe4e9')
plt.ylabel('Average Rating')
ax.figure.set_facecolor('#79c2d0')
plt.tight_layout()
plt.show()



#####################################################################
# Displaying the number of episodes in each season of the Game of Thrones series
plt.figure(figsize=(7, 5),facecolor = '#dbd8e3')
got = top_serise.tconst[top_serise.primaryTitle == 'Game of Thrones'].iloc[0]
number_of_episodes = []
number_of_seasons = []
for i in range(1, 9):
    number_of_episodes.append(epi_number(i, got))
    number_of_seasons.append(i)
data = {'Seasons': number_of_seasons, 'Number of Episodes': number_of_episodes}
df = pd.DataFrame(data)
print('\n')
print('Number of Episodes in each season of Game of Thrones')
print(df.to_string(index=False))
ax = plt.axes()
plt.bar(number_of_seasons, number_of_episodes,color='#2a2438')
plt.xlabel('Seasons')
plt.ylabel('Number of Episodes')
plt.title('Game of Thrones')
ax.set_facecolor('#5c5470')
plt.show()




#####################################################################
# Displaying the average rating of each season of the Game of Thrones series
plt.figure(figsize=(7, 5),facecolor='#93e4c1')
ratting_of_season = []
number_of_seasons = []
for i in range(1,9):
    number_of_seasons.append(i)
    ratting_of_season.append(ratings(i,got))
data = {'Seasons': number_of_seasons, 'Average Rating': ratting_of_season}
df = pd.DataFrame(data)
print('\n')
print('Average Rating of each season of Game of Thrones')
print(df.to_string(index=False))
ax = plt.axes()
ax.set_facecolor('#3baea0')
plt.bar(number_of_seasons,ratting_of_season,color='#118a7e',width=0.5)
plt.plot(number_of_seasons,ratting_of_season,marker='o',color='#1f6f78')
plt.xlabel('Seasons')
plt.ylabel('Average Rating')
plt.title('Game of Thrones')
plt.show()