from bs4 import BeautifulSoup

starter_cards = []
starter_summoners = []
with open("cards.html", "r", encoding='utf-8') as html:
    soup = BeautifulSoup(html, 'html.parser')
    cards = soup.select('div.card.beta.starter')

    for card in cards:
        # Get Card Name
        name = card.find('div', {'class': "card-name-name"}).getText()

        # Get Card ID
        card_id = card.find('img').get("card_detail_id")

        # Get Card Element
        element = card.find('div', {'class': "card-name"}).get("class")[1]
        # Get Card Mana
        mana = card.find('div', {'class': "stat-text-mana"}).getText()

        starter_cards.append({
            'name': name,
            'card_id': card_id,
            'element': element,
            'mana': mana
        })

with open("summoners.html", "r", encoding='utf-8') as html:
    soup = BeautifulSoup(html, 'html.parser')
    cards = soup.select('div.card.beta')

    for card in cards:
        # Get Card Name
        name = card.find('div', {'class': "card-name-name"}).getText()
        starter_summoners.append(name)

print(starter_cards)
print(starter_summoners)



#
# Summoner: 3 - 259
# Tank : 8 - 184
# Creeping Ooze : 1 - 91
#
# 12
# ==========================================
# Summoner: 3 - 259
# Tank : 8 - 184
# Faild Summoner  : 2 - 180
#
# 13
# ==========================================
# 99
