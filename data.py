import requests
import json

battles_win_history = []

# Request Player History from splinterland API
resp = requests.get('https://api.splinterlands.io/battle/history?player=kingsgambit0615').json()
battles = resp['battles']

temp = []
for battle in battles:
    temp.append(battle['mana_cap'])

output = []
for x in temp:
    if x not in output:
        output.append(x)

output.sort()
print(output)



    # print('Loop:' + str(temp))
    # temp = temp + 1
    # # Loads Battle Details
    # fight_details = json.loads(battle['details'])

    # # Get player winning deck summoners and monsters
    # if fight_details['winner'] == "kingsgambit0615":

    #     # Get Mana Cap Of the Match
    #     mana_cap = battle['mana_cap']
    #     print("mana: " + str(mana_cap))
    #     # Get Ruleset Of the Match
    #     ruleset = battle['ruleset']
    #     print("ruleset: " + ruleset)

    #     # team_one = (fight_details['team1'])
    #     # print(team_one['player'])

    #     try:
    #         if fight_details['team1']['player'] == "kingsgambit0615":
    #             summoner = fight_details['team1']['summoner']['card_detail_id']
    #             print("Summoner: " + str(summoner))

    #             monsters = fight_details['team1']['monsters']
    #             for monster in monsters:
    #                 print("monster:" + str(monster['card_detail_id']))
    #         else:
    #             summoner = fight_details['team2']['summoner']['card_detail_id']
    #             print("Summoner: " + str(summoner))

    #             monsters = fight_details['team2']['monsters']
    #             for monster in monsters:
    #                 print("monster:" + str(monster['card_detail_id']))
    #     except:
    #         pass



