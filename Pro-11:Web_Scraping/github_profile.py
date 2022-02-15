import requests
from bs4 import BeautifulSoup as bs

user = input("\nEnter GitHub Username: ")
url = 'https://github.com/' + user
r = requests.get(url)
soup = bs(r.content, 'html.parser')
profile_image = soup.find('img',{'alt' : 'Avatar'})['src']
print(profile_image)
