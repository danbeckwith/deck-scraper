from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import json as json

url = "http://www.hearthstonetopdecks.com/hearthstones-best-standard-ladder-decks/"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, 'html.parser')


def getTierList():
    deckTiers = {}
    tierLevel = 0
    for h2 in soup.findAll('h2'):
        recording = False if tierLevel < 1 else True
        
        if "Tier" in h2.get_text() and "Season" not in h2.get_text():
            tierLevel += 1
            recording = False

        if recording and "Comments" not in h2.get_text():
            deckTiers[h2.get_text()] = {"tierLevel": tierLevel, "cardList": []}
    
    return deckTiers


def getDeckLists():
    deckTiers = getTierList()

    allTestList = soup.findAll('div', attrs={'class': 'card-list'})
    blockList = soup.findAll('div', attrs={'class': 'td-box-wrap'})

    for testList,block in zip(allTestList,blockList):
        deckName = block.h2.get_text()

        for item in testList.ul:
            name,count = textStripper(item)
            deckTiers[deckName]["cardList"].append([name, count])

    return deckTiers


def textStripper(item):
    cardName = item.find('span', attrs={'class': 'card-name'}).get_text()
    cardCount = int(item.find('span', attrs={'class': 'card-count'}).get_text())
    return cardName,cardCount


decks = getDeckLists()


print(json.dumps(decks, ensure_ascii=False))



