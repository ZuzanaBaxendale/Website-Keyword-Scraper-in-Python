import requests
import string


print('PLEASE ENTER HTML OF WEBPAGE TO CRAWL FOR KEYWORDS:')


url = input()
res = requests.get(url)
html_page = res.content
from bs4 import BeautifulSoup

soup = BeautifulSoup(html_page, 'html.parser')

text = soup.find_all(text=True)

set([t.parent.name for t in text])

# {'label', 'h4', 'ol', '[document]', 'a', 'h1', 'noscript','span', 'header', 'ul', 'html', 'section', 'article', 'em', 'meta', 'title', 'body', 'aside', 'footer', 'div', 'form', 'nav', 'p', 'head', 'link', 'strong', 'h6', 'br', 'li', 'h3', 'h5', 'input', 'blockquote', 'main', 'script', 'figure'}

output = ''
blacklist = [
    '[document]',
    'noscript',
    'header',
    'html',
    'meta',
    'head', 
    'input',
    'script',
    ]

for t in text:
    if t.parent.name not in blacklist:
        output += '{} '.format(t)


output1 = output.replace(',', '')
output = output1.replace('.', '')
output1 = output.replace("!", '')
output = output1.replace(';', '')
output1 = output.replace(':', '')
output = output1.replace('?', '')

words = output.split()

stopwords = ['is', 'but', 'and', 'so', 'because', 'if']

resultWords = [word for word in words if word.lower() not in stopwords]

keywords = [' '.join(resultWords[i: i + 3]) for i in range(0, len(resultWords), 3)]

keywordsSorted = sorted(keywords)

for n in range(len(keywordsSorted)):
    print(keywordsSorted[n])
    print("\n")

