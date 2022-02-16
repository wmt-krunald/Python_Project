from urllib import request
import requests
from bs4 import BeautifulSoup as bs

page = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=").text
soup = bs(page, 'lxml')
jobs = soup.find('li', class_="clearfix job-bx wht-shd-bx")
#print(jobs)

company_name = soup.find('h3', class_="joblist-comp-name").text.replace(' ','')
# print("Company Name : ", company_name.text.replace(' ', ''))

skills = soup.find('span', class_="srp-skills").text
# print("Skills Required : ", skills.text.replace(' ', ''))

posted_date = soup.find('span', class_="sim-posted").text
# print("Posted Date : ", posted_date.text.replace(' ', ''))

print(f'''
Company Name: {company_name}
Required Skills : {skills}
Posted Date : {posted_date}
''')