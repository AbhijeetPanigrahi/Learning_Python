# TASK:-    Print the lasrgest upvoted article in the ycombinator page
#######################################################################
from bs4 import BeautifulSoup

import requests # to access any url

response = requests.get("https://news.ycombinator.com/news")
yc_webpage = response.text
# print(yc_webpage)

soup = BeautifulSoup(yc_webpage, "html.parser")

# Find all span elements with class 'titleline'
all_spans = soup.find_all(name="span", class_="titleline")

articles_text = []
articles_links = []

for span in all_spans:
    # Find the a tag within the span tag
    a_tag = span.find('a')
    if a_tag:
        text = a_tag.getText()
        link = a_tag.get("href")
        articles_text.append(text)  # Append the a tag's text
        articles_links.append(link) # Append the a tag's link

upvotes =  soup.select(selector = ".score")
article_upvotes = []
for votes in upvotes:
    # print(votes.getText())
    # article_upvotes.append(votes.getText())
    article_upvotes.append(int(votes.getText().split()[0])) # as we need only the number 

largest_upvote = max(article_upvotes)
largest_index = article_upvotes.index(largest_upvote)
print("\nHighst Upvoted article:-")
print(articles_text[largest_index])
print(f"Link:- {articles_links[largest_index]}")
print(f"Upvote:- {article_upvotes[largest_index]}")

# print(articles_text)
# print(articles_links)
# print(article_upvotes)



