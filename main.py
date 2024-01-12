import requests
import math
import os


if os.path.exists('./data.txt'):
    os.remove('./data.txt')

number_of_ads = int(input('Please enter the number of advertisements: '))
number_of_pages = math.ceil(number_of_ads / 24)

counter = 0
for page_number in range (number_of_pages):
    URL = "https://api.divar.ir/v8/web-search/bojnurd/real-estate"
    paginated_URL = URL + "?page=" + str(page_number)
    response = requests.get(paginated_URL)
    response = response.json()
    posts = response["web_widgets"]["post_list"]
    with open('./data.txt', 'a', encoding='utf-8') as file:
        for post in posts:
            if counter < number_of_ads:
                file.write(post["data"]["title"])
                file.write("\n")
                counter += 1
