import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime


# Get the current year
today_year = datetime.date.today().year

print(f'Scraping Box Office Mojo. Data is available from 1977 to {today_year}.')
year = int(input("Enter the year you want to scrape: "))

if year < 1977 or year > today_year:
    print(f"Year should be between 1977 and {today_year}")
    exit()

# Lists to hold the scraped data
Worldwide = []
Domestic = []
Foreign = []
per_Domestic = []
per_Foreign = []
Movie_name = []
Rank = []

# URL for the given year
URL = f"https://www.boxofficemojo.com/year/world/{year}/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")


# Find the results table
results = soup.find(id="table")
if not results:
    print("No table found on the page.")
    exit()

world = results.find_all("td", class_="a-text-right mojo-field-type-money")
per = results.find_all("td", class_="a-text-right mojo-field-type-percent")
name = results.find_all("a", class_="a-link-normal")

i=0
j=0
k=0
r = 1


for movie in name:
    if k > 5:
        Movie_name.append(movie.text)
        Rank.append(r)
        r+=1
    k+=1
for movie in per:
    if j==0:
        per_Domestic.append(movie.text)
        j+=1
    elif j == 1:
        per_Foreign.append(movie.text)
        j = 0

for movie in world:
    if i==0:
        Worldwide.append(movie.text)
        i+=1
    elif i == 1:
        Domestic.append(movie.text)
        i+=1
    elif i==2:
        Foreign.append(movie.text)
        i = 0

    
# Creating a DataFrame
data = {
    "Rank": Rank,
    "Movie Name": Movie_name,
    "Worldwide": Worldwide,
    "Domestic": Domestic,
    "Domestic %": per_Domestic,
    "Foreign": Foreign,
    "Foreign %": per_Foreign
}

# Saving the data to a CSV file
df = pd.DataFrame(data)
df.to_csv(f'Movies_Box_Office_{year}.csv',index=False)
print(f"Data for {year} saved to Movies_Box_Office_{year}.csv")