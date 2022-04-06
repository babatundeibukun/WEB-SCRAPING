from bs4 import BeautifulSoup
# import lxml
# with open("website.html", encoding="utf-8") as file:
#     contents = file.read()
# soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)

import requests

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "html.parser")

text = []
link = []

article_tag = soup.find_all(name="a", class_="titlelink")
for article in article_tag:
    article_text = article.get_text()
    article_link = article.get("href")
    text.append(article_text)
    link.append(article_link)

article_score = [int(score.get_text().split()[0]) for score in soup.find_all(name="span", class_="score")]

# print(text)
# print(link)
# print(article_score)

largest_number = max(article_score)
largest_index = article_score.index(largest_number)
print(text[largest_index])
print(link[largest_index])