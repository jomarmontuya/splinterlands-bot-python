import splinterlands as sp

for i in range(100):
    try:
        play = sp.splinterlands_login('env.username', 'env.password')
        play.battle()
        play.search_match()
        play.create_team()
        play.battle_start()
    except:
        pass

    try:
        play_1 = sp.splinterlands_login('env.username', 'env.password')
        play_1.battle()
        play_1.search_match()
        play_1.create_team()
        play_1.battle_start()
    except:
        pass