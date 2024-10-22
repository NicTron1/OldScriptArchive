def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

from requests_html import HTML, HTMLSession
import requests
from dhooks import Webhook, Embed, File

session = HTMLSession()
r = session.get('https://old.reddit.com/r/wallstreetbets/top/')

titles = ''

ticker = '[data-subreddit="wallstreetbets"]'
tickers = r.html.find(ticker)
linkList = []
idList = []

for ticker in tickers:
    linkList.append('https://old.reddit.com/' + ticker.attrs['data-permalink'])
    idList.append(ticker.attrs['id'])
   
#id > div.entry.unvoted > div.expando > form
item = 0
while item < len(linkList):
    nsession = HTMLSession()
    n = session.get(linkList[item])
    titleSel = '[data-event-action="title"]'
    titleEl = n.html.find(titleSel)
    title = titleEl[0].text
    titles = titles + title + ' '
    formSel = str('#' + idList[item] + ' > div.entry.unvoted > div.expando > form')
    form = n.html.find(formSel)
    try:
        el = form[0].find('div')
        el2 = el[0].find('div')
        bodys = el2[0].find('p')
        for text in bodys:
            titles = titles + text.text + ' '
    except:
        test = []
    item += 1

sortedItems = sorted(word_count(titles), key=word_count(titles).get, reverse=True)

desc = ''

for i in sortedItems:
    if (i.isupper()):
        desc = desc + '`' + i + '`' + '\n'

#print(desc)

hook = Webhook('https://discord.com/api/webhooks/803488491820417044/X-utQMtp-uSJxK0LRljgIQ2y4kfFcWr93QQz14KzsocguwSfiprU2jgvBnR7WIgY8tHF',username="WSB Tracker",avatar_url="https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/160/softbank/145/chart-with-upwards-trend_1f4c8.png")

embed = Embed(
    description=desc,
    color=4062976,
    url="https://reddit.com/r/wallstreetbets/",
    title="WSB Hype"
    )


hook.send(embed=embed)

