import requests
from bs4 import BeautifulSoup

url = "https://www.fifa.com/worldcup/archive/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find match information (this will depend on the website structure)
# For demonstration, this is a pseudo example
matches = soup.find_all('div', class_='match-info')

for match in matches:
    date = match.find('span', class_='date').text
    teams = match.find('span', class_='teams').text
    print(f"Date: {date}, Teams: {teams}")