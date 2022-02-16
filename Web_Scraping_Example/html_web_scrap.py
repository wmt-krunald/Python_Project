from bs4 import BeautifulSoup as bs

with open('/home/webmob/Krunal_Work_space/Python/Python_Project/Web_Scraping_Example/test.html', 'r') as html_file:

    content = html_file.read()
    
    soup = bs(content, 'lxml')
    tags = soup.find_all('div', class_='card')

    for course in tags:
        # print(course.h4)
        course_name = course.h4.text
        course_price = course.a.text

        print(f"\n{course_name} is only start from {course_price} .")        
        # print(course_name)
        # print(course_price)