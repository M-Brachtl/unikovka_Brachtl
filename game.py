from random import choice, randint
# příběh
print("\nSešel jsem žebříkem dolů, do ředitelské místnosti. Tady by měly být ty dokumenty. Vynález zkázy, ano, už jej vynalezli. Zase. Musím zjistit, jak je sestrojen, abychom jej mohli deaktivovat.")
print("Ou. Moje prohledávání té opuštěné základny je u konce. Ne že by zrovna začalo. Šel jsem do centrální místnosti, abych našel ty dokumenty, ale oni už na mě přišli.")
print("Jak se ale dívám, ty dokumenty tu stejně nejsou. Ne, že by na tom teď zrovna záleželo.")
print("A právě vypnuli elektřinu. Pochopitelně někdo nechce, abych mu utekl. Naštěstí mám baterku. Žebřík nahoru už koukám taky vede jen do stropu... budu muset jít východem. A tam jsou vojáci, co mě chtějí dostat.")
print("\n----------------------------------------------------------------------------------------------\n")
print("Všude je tma, musíš si svítit baterkou. Momentálně je nabitá na 100 %, ale po každém kole se o pětinu vybije. Nabít ji lze jen tam, kde je elektřina a nabíječka, tedy pouze v místnosti 4.")
print("Pozor! V místnostech 3-6 chodí voják. Sice jen jeden, ale pokaždé, když zemře, přijde další.")
print("Energie klesá vždy na konci kola, tedy bezprostředně po nepřítelově akci. Pokud na konci kola jsi stále v boji, neubívá ti energie v baterce.")
print("Nenech svoji baterku vybít, protože pak nic neuvidíš a budeš do všeho narážet. Tak strážcům umožníš tě zajmout nebo zabít.")
print("\nV jedné z mísností 3, 5 nebo 6 je výstup z komplexu, tedy záchrana (místnost č. 7). Abys zjistil v které, musíš najít mapu.\n")
print("------------------------------------------------------------------------------------------------")
# startovní nastavení
# possibilities = ("Pohyb","Zvedni","Útoč","Uteč")
safe_position = randint(1,5)
exit_position = 4
while exit_position == 4:
    exit_position = randint(3,6)
rooms_doors = ((1,2,3,4),(0,2,4,5),(0,1,3),(0,2,4,6),(0,1,3,5,6),(1,4,6),(3,4,5)) # možnosti přesunu v místnostech
rooms_visit = ["Nic","","","","","",""]
things = ("Klíč","Mapa","Pistole","Obvaz","Gumová kačenka")
enemy = {
    "lives": randint(3,4),
    "position": 6,
    "key_holder": randint(1,3)
}
inventory = ["Obvaz"] # inventář hráče
invent_state = [3] # zbylý počet použití odpovídajícího předmětu v inventáři
player = {
    "lives": 5,
    "position": 0,
    "energy" : 5,
    "unlocked_safe" : 0
}
fight = 0
fight2 = 1
noise = 0
trefa = ("Vedle!","Trefa!")
while True:
    decision = ""
    live_change = 1
    if player["lives"] <= 0:
        print("Jsi mrtvý. Nebo možná jen zajatý. Jak kdyby na tom záleželo...\n")
        endgame_text_index = 2
        break
    print("\nTvůj inventář:",inventory)
    print("Nacházíš se v místnosti:",player["position"],"\nŽivoty:",player["lives"],"\nZbylá energie v baterce:",player["energy"]*20,"%\n")
    if player["energy"] == 2:
        print("Baterku máš na 40 %. Musíš ji do příštího kola nabít, jinak se ti vybije úplně.\n".upper())
    while not decision.lower() in {"inventory","použít","zvedni","pohyb","útoč","uteč","konec","odemkni","dobít"}:
        decision = input(("Zadej svoji akci (kontrola inventáře se nepočítá jako akce): ","Jsi v boji, útoč nebo uteč. Pro detailní kontrolu inventáře napiš 'Inventory' ")[fight])
    if decision.lower() == "inventory": # kontrola inventáře
        ref_thing = input("Zadejte věc z inventáře, které počet chcete znát: ")
        copy_inv = []
        for item in inventory:
            copy_inv.append(item.lower())
        if ref_thing.lower() in copy_inv:
            print(f"{ref_thing} lze použít ještě {invent_state[copy_inv.index(ref_thing.lower())]}x")
        else: print("Tato věc se nenachází ve vašem inventáři.")
        ref_thing = "Nichts"
        decision = ""
        while not decision.lower() in {"inventory","použít","zvedni","pohyb","útoč","uteč","konec","odemkni","dobít"}:
            decision = input(("\nZadej svoji akci: ","\nJsi v boji. Útoč, nebo uteč. ")[fight])
    elif decision.lower() == "konec":
        print("-----------------")
        endgame_text_index = 0
        break
    if fight:
        done = 0
        if decision.lower() == "útoč":
            if input("Čím zaútočíš? ").lower() == "pistole" and "Pistole" in inventory:
                print("-----------------")
                live_change = randint(0,1)
                enemy["lives"] += -live_change
                print("Bang!",trefa[live_change])
                # stav pistole
                ref_index = inventory.index("Pistole")
                invent_state[ref_index] += -1
                if invent_state[ref_index] == 0:
                    invent_state.remove(invent_state[ref_index])
                    inventory.remove("Pistole")
                ref_index = 0
            else:
                print("-----------------")
                print("Zaútočil jsi pěstmi, protože nemáš pistoli nebo jsi nezadal 'pistole'! Ne zrovna efektivní zbraň...")
                print("Oba se navzáje poraníte.")
                player["lives"] += -randint(1,2)
                enemy["lives"] += -1
                live_change = 1
            # if enemy["lives"] == 0 and player["position"] == 6:
            #     print("Nepřítel je mrtev! Zabil jsi jej v jeho domovině, takže teď už žádného dalšího nepotkáš!")
            #     fight = 0
            if enemy["lives"] == 0:
                fight = 0
        elif decision.lower() == "uteč":
            player["lives"] += -randint(0,1)
            while True:
                doors = ""
                for r in rooms_doors[player["position"]]:
                    doors = doors + str(r) + ", "
                print("\nOdtud se lze dostat do místnotí:",doors)
                next_room = int(input("Zadej místnost, do které se chceš přesunout: "))
                if next_room in rooms_doors[player["position"]]:
                    player["position"] = next_room
                    break
                else: print(f"Z místnosti {player['position']} se nelze dostat do místnosti {next_room}")
            fight = 0
            print("-----------------\nUtekl jsi do místnosti ",player["position"])
    elif decision.lower() == "pohyb": # přesun mezi místnostmi
        print("\nNacházíš se v místnosti č.",player["position"])
        doors = ""
        for r in rooms_doors[player["position"]]:
            doors = doors + str(r) + ", "
        if exit_position == player["position"] and player["unlocked_safe"]:
            doors = doors + "7"
        print("Odtud se lze dostat do místnotí:",doors)
        next_room = 20
        while not (next_room in rooms_doors[player["position"]] or (exit_position == player["position"] and player["unlocked_safe"] and next_room == 7)):
            next_room = int(input("Zadej místnost, do které se chceš přesunout: "))
        if next_room == 7:
            print("-----------------")
            player["position"] = 7
        else:
            print("-----------------")
            print("Přesunul ses do místnosti",next_room)
            player["position"] = next_room
            if not rooms_visit[next_room]:
                rooms_visit[next_room] = things[randint(2,4)]
                # inventory.append(things[randint(2,4)])
                print("V místnosti jsi našel:",rooms_visit[next_room])
            if player["position"] == enemy["position"]:
                fight = 1
                print("Á. Natrefil jsi na vojáka. To znamená BOJ.")
                fight2 = randint(0,1)
            if player["position"] == safe_position:
                print("V této místnosti jsi našel těžkou ocelovou krabičku s dvířki a otvorem pro klíč, jinak známou jako safe. Tam musí být ta mapa!")
    # inventář a sbírání předmětů
    elif decision.lower() == "konec": # ukončení hry
        print("-----------------")
        endgame_text_index = 0
        break
    elif decision.lower() == "zvedni": # zvednutí předmětu
        print("-----------------")
        if rooms_visit[player["position"]] in things:
            if rooms_visit[player["position"]] in inventory:
                invent_state[inventory.index(rooms_visit[player["position"]])] += randint(2,4)
            else:
                inventory.append(rooms_visit[player["position"]])
                invent_state.append(randint(2,4))
            print("Zvedl jsi",rooms_visit[player["position"]].lower())
            rooms_visit[player["position"]] = "Nic"
        else:
            print("Nic zde není k sebrání.")
    elif player["position"] == safe_position and decision.lower() == "odemkni" and not player["unlocked_safe"]:
        print("-----------------")
        print("Odemknul jsi safe. Našel jsi v něm mapu základny.")
        print("Východ se nachází v mísnosti č.",exit_position)
        player["unlocked_safe"] = 1
    elif decision.lower() == "dobít" and player["position"] == 4:
        player["energy"] = 6
        print("-----------------\nDobil sis baterku na 100 %")
    #
    # elif decision.lower() == "testing": #testing#
    #     test_id = input("Hey, a tester! I am the happiest code ever!")
    #     if test_id == "get_key":
    #         print("Tento voják u sebe měl klíč")
    #         if rooms_visit[safe_position]:
    #             print("To musí být ten klíč od safu!")
    #         inventory.append("Klíč")
    #         invent_state.append(1)
    #     else:
    #         player["energy"] += 3 #testing#
    #
    elif decision.lower() == "použít":# používání předmětů
        ref_thing = "Nichts"
        while not ref_thing in inventory:
            ref_thing = input("Kterou věc z inventáře chcete použít? ").capitalize()
        ref_index = inventory.index(ref_thing)
        if ref_thing.lower() == "obvaz": # Obvaz
            print("-----------------")
            player["lives"] += 1
            invent_state[ref_index] += -1
            print("Obvázal ses. +1 život")
        elif ref_thing.lower() == "pistole":
            if input("Pistolí lze střílet pouze na živé objekty. Momentálně nikoho živého nevidíš. Opravdu chceš pistoli použít? ") == "Ano":
                print("-----------------")
                player["lives"] += -2
                invent_state[ref_index] += -1
                print("Střelil ses do ruky. Deset z deseti doktorů nedoporučuje. A teď ani ty. -2 životy")
        elif ref_thing.lower() == "gumová kačenka": # Aktivity s gumovou kačenkou
            action = ""
            while not action in {"zmáčknout","hodit"}:
                action = input("Vyberte akci Zmáčknout nebo hodit: ")
            if action.lower() == "zmáčknout":
                print("-----------------")
                if enemy["position"] in rooms_doors[player["position"]]:
                    print("Mimo kačenky uslyšels nějaký zvuk.")
                    noise = 1 # pro enemyho
                else: print("Písk!")
            elif action.lower() == "hodit":
                action = input("Kam chceš kačenku hodit? (o zeď, do vzduchu, do vedlejší místnosti) ")
                print("-----------------")
                if action.lower() in {"o zeď","do vzduchu","do vedlejší místnosti"}:
                    if not (action.lower() == "do vedlejší místnosti"):
                        if not (randint(0,100) == 50):
                            print("Kačenku jsi hodil a zase chytil! Dobrá práce!")
                        else:
                            print("Kačenku jsi nechytil a spadla ti na hlavu. -1 život")
                            player["lives"] += -1
                    else:
                        if int(input(f"Do které místnosti chceš kačenku hodit? Možnosti: {rooms_doors[player['position']]}")) == enemy["position"]:
                            print("Ve vedlejší mísnosti byl nepřítel, kterého jsi přilákal sem. Dobrá práce! Teď víš, kde je! Tady...")
                            enemy["position"] = player["position"]
                            fight = 1
                        else:
                            print("Nic se nestalo.")
                        invent_state[ref_index] += -1
            if invent_state[ref_index] == 0:
                invent_state.remove(invent_state[ref_index])
                inventory.remove(ref_thing)
            ref_index = 0
        elif ref_thing.lower() == "klíč" and player["position"] == safe_position and not player["unlocked_safe"]:
            print("-----------------")
            print("Odemknul jsi safe. Našel jsi v něm mapu základny.")
            print("Východ se nachází v mísnosti č.",exit_position)
            player["unlocked_safe"] = 1
        ref_thing = "Nichts"
    print("\n--------------------------------------------------------")
    # print(fight,fight2,noise,enemy["position"],enemy["lives"],safe_position) # testing
    # enemyho akce
    # pravidla pohybu: 1) enemy se pohne o jedno pole v oblasti 3-6; 2) v boji se nehne; 3) při zapískání GK se 1. kolo nehne, 2. jde na místo pískání; 4) pokud enemy vleze sám do boje mimo účinky GK, randint rozhoduje, kdo útočí první
    if not player["position"] == 7 or enemy["lives"] > 0:
        print("Známé informace o akcích nepřítele:\n")
        if noise == 1: # GK píská a player je v sopoužítdní roomce
            # do nothing
            noise = 2
            direction = player["position"]
        elif noise == 2:
            enemy["position"] = direction
            noise = 0
            fight = not player["position"] - enemy["position"]
        else:
            if not fight:
                posi = list(rooms_doors[enemy["position"]])
                for block in range(3):
                    if block in posi:
                        posi.remove(block)
                enemy["position"] = choice(posi) #posi[randint(0,len(posi)-1)]
                fight = int(not enemy["position"]-player["position"])
                if fight:
                    fight2 = randint(0,1)
                    print("Nepřátelský voják tě našel! To vypadá na boj.")
            if fight and fight2:
                if enemy["lives"] > 1 and randint(0,1):
                    player["lives"] += -1
                    print("Nepřítel na tebe zaútočil a poranil tě.")
                elif enemy["lives"] == 1 and not randint(0,2):
                    player["lives"] += -1 # bezpečnější, ale méně efektivní útok
                    print("Nepřítel na tebe zaútočil a poranil tě.")
                elif enemy["lives"] == 1 and not live_change: # když enemy životy = 1 a útok pistolí byl nepovedený, enemy uteče
                    enemy["position"] = randint(0,len(rooms_doors[player["position"]])-1)
                    print("Nepřítel utekl do místnosti",enemy["position"])
                    fight = 0
                enemy["lives"] += -randint(0,1+(int((enemy["lives"]-1)/enemy["lives"] + 0.9))) # pro životy = 1 -> randint(0,1); pro živ. = 2+ -> randint(0,2)
                enemy["lives"] += -(fight - 1)
                if enemy["lives"] == 1:
                    print("Nepříteli zbývá pouze 1 život!")
        if not fight2:
            print("Nepřítel ještě nezaútočil. Máš výhodu první rány!")
        fight2 = 1
        # print(fight,fight2,noise,enemy["position"],enemy["lives"],enemy["key_holder"]) #testing#
    if enemy["lives"] == 0:
        fight = 0
        print("\nNepřítel zemřel.")
        enemy["key_holder"] -= 1
        if enemy["key_holder"] == 0:
            print("Tento voják u sebe měl klíč")
            if rooms_visit[safe_position]:
                print("To musí být ten klíč od safu!")
            else:
                print("K čemu by mi mohl být? Teď hlavně potřebuju najít to místo, kde je mapa k východu.")
            inventory.append("Klíč")
            invent_state.append(1)
        while enemy["position"] == player["position"]:
            enemy["position"] = randint(3,6)
        enemy["lives"] = randint(2,4)
        player["energy"] += 1 # rozvaž přítomnost tohoto - uprav lore
    print("--------------------------------------------------------")
    if player["position"] == 7: ################################################################# Endgame
        endgame_text_index = 1
        break
    player["energy"] += -(1 - fight)
    if player["energy"] == 6:
        player["energy"] = 5
    elif player["energy"] == 0:
        print("Ouuu. Baterka došla. Kam teď? Třebaaaa tudy? ... Au! Moje noha! Aaaaaa! Počkat... Nejsou to kroky?")
        player["lives"] = 0
endgame_text = ("Zmizet beze stopy v uzavřeném prostoru je vskutku výhoda. Ale to neznamná, že jsi vyhrál.","Světlo! Tady už mě nedostanou. Sice jsem nesplinil cíl mise, ale aspoň jsem naživu.","Co taková reinkarnace, hm?")
print(endgame_text[endgame_text_index])

input("\nEnter pro ukončení hry")
