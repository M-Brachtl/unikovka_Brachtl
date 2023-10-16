from random import randint
# startovní nastavení
possibilities = ("Pohyb","Zvedni","Útoč","Uteč")
rooms_doors = ((1,2,3,4),(0,2,4,5),(0,1,3),(0,2,4,6),(0,1,3,5,6),(1,4,6),(3,4,5)) # možnosti přesunu v místnostech
rooms_visit = ["Nic","","","","","",""]
things = ("Red key","Blue key","Pistole","Obvaz","Gumová kačenka")
enemy = {
    "lives": 3,
    "position": 6
}
inventory = ["Obvaz","Gumová kačenka"] # inventář hráče
invent_state = [2,2] # zbylý počet použití odpovídajícího předmětu v inventáři
player = {
    "lives": 5,
    "position": 0
}
fight = 0
fight2 = 1
noise = 0
trefa = ("Vedle!","Trefa!")
while True:
    decision = ""
    print(inventory)
    print(player)
    
    decision = input(("Zadej svoji akci (kontrola inventáře se nepočítá jako akce): ","Jsi v boji, útoč nebo uteč. Pro detailní kontrolu inventáře napiš 'Inventory'")[fight])
    if decision.lower() == "inventory": # kontrola inventáře
        ref_thing = input("Zadejte věc z inventáře, které počet chcete znát: ")
        if ref_thing in inventory:
            print(f"{ref_thing} lze použít ještě {invent_state[inventory.index(ref_thing)]}x")
        else: print("Tato věc se nenachází ve vašem inventáři.")
        ref_thing = "Nichts"
        decision = input(("Zadej svoji akci: ","Jsi v boji. Útoč, nebo uteč.")[fight])
    if fight:
        if player["lives"] == 0:
            print("Jsi mrtvý.")
            break
        else:
            if decision.lower() == "útoč":
                if input("Čím zaútočíš?").lower() == "pistole" and "Pistole" in inventory:
                    live_change = randint(0,1)
                    enemy["lives"] += live_change
                    print("Bang!",trefa[live_change])
                    # stav pistole
                    ref_index = inventory.index("Pistole")
                    invent_state[ref_index] += -1
                    if invent_state[ref_index] == 0:
                        invent_state.remove(invent_state[ref_index])
                        inventory.remove("Pistole")
                    ref_index = 0
                else:
                    print("Zaútočil jsi pěstmi, protože nemáš pistoli nebo jsi nezadal 'pistole'! Ne zrovna efektivní zbraň...")
                    print("Oba přijdete o život.")
                    player["lives"] += -1
                    enemy["lives"] += -1
                if enemy["lives"] == 0 and player["position"] == 6:
                    print("Nepřítel je mrtev! Zabil jsi jej v jeho domovině, takže teď už žádného dalšího nepotkáš!")
                    fight = 0
                elif enemy["lives"] == 0:
                    print("Nepřítel je mrtev!")
                    enemy["position"] = 6
                    enemy["lives"] = randint(1,3)
                    fight = 0
            elif decision.lower() == "uteč":
                player["lives"] += -1
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
    elif decision == "Pohyb": # přesun mezi místnostmi
        print("\nNacházíš se v místnosti č.",player["position"])
        doors = ""
        for r in rooms_doors[player["position"]]:
            doors = doors + str(r) + ", "
        print("Odtud se lze dostat do místnotí:",doors)
        next_room = int(input("Zadej místnost, do které se chceš přesunout: "))
        if next_room in rooms_doors[player["position"]]:
            player["position"] = next_room
            if not rooms_visit[next_room]:
                rooms_visit[next_room] = things[randint(2,4)]
                # inventory.append(things[randint(2,4)])
                print("V místnosti jsi našel:",rooms_visit[next_room])
        else: print(f"Z místnosti {player['position']} se nelze dostat do místnosti {next_room}")
    # inventář a sbírání předmětů
    elif decision == "Konec": # ukončení hry
        break
    elif decision == "Zvedni": # zvednutí předmětu
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
    
    elif decision == "Use":# používání předmětů
        ref_thing = input("Kterou věc z inventáře chcete použít? ")
        if ref_thing in inventory:
            ref_index = inventory.index(ref_thing)
            if ref_thing == "Obvaz": # Obvaz
                player["lives"] += 1
                invent_state[ref_index] += -1
                print("Obvázal ses. +1 život")
            elif ref_thing == "Pistole":
                if input("Pistolí lze střílet pouze na živé objekty. Momentálně nikoho živého nevidíš. Opravdu chceš pistoli použít?") == "Ano":
                    player["lives"] += -2
                    invent_state[ref_index] += -1
                    print("Střelil ses do ruky. Deset z deseti doktorů nedoporučuje. A teď ani ty. -2 životy")
            elif ref_thing == "Gumová kačenka": # Aktivity s gumovou kačenkou
                action = ""
                while not (action in {"Zmáčknout","Hodit"}):
                    action = input("Vyberte akci: Zmáčknout, Hodit ")
                if action == "Zmáčknout":
                    if enemy["position"] in rooms_doors[player["position"]]:
                        print("Mimo kačenky uslyšels nějaký zvuk.")
                        noise = 1 # pro enemyho
                    else: print("Písk!")
                elif action == "Hodit":
                    action = input("Kam chceš kačenku hodit? (o zeď, do vzduchu, do vedlejší místnosti) ")
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
                            invent_state[ref_index] += -1
                            print("Nic se nestalo.")
            if invent_state[ref_index] == 0:
                invent_state.remove(invent_state[ref_index])
                inventory.remove(ref_thing)
            ref_index = 0
        ref_thing = "Nichts"
    print("--------------------------------------------------------",print(fight,fight2,noise,enemy["position"],enemy["lives"]))
    # enemyho akce
    # pravidla pohybu: 1) enemy se pohne o jedno pole v oblasti 3-6; 2) v boji se nehne; 3) při zapískání GK se 1. kolo nehne, 2. jde na místo pískání; 4) pokud enemy vleze sám do boje mimo účinky GK, randint rozhoduje, kdo útočí první
    if noise == 1: # GK píská a player je v sousední roomce
        # do nothing
        noise = 2
        direction = player["position"]
    elif noise == 2:
        enemy["position"] = direction
        noise = 0
    else:
        if not fight:
            posi = list(rooms_doors[enemy["position"]])
            for block in range(5):
                if block in posi:
                    posi.remove(block)
            enemy["position"] = posi[randint(0,len(posi)-1)]
            fight = int(not enemy["position"]-player["position"])
        if fight: fight2 = randint(0,1)
        if fight and fight2:
            if enemy["lives"] > 1 and randint(0,1):
                player["lives"] += -1
            elif enemy["lives"] == 1 and not randint(0,2):
                player["lives"] += -1 # bezpečnější, ale méně efektivní útok
            elif enemy["lives"] == 1 and not live_change: # když enemy životy = 1 a útok pistolí byl nepovedený, enemy uteče
                enemy["position"] = randint(0,len(rooms_doors[player["position"]])-1)
                print("Nepřítel utekl do místnosti",enemy["position"])
                fight = 0
            enemy["lives"] += -randint(0,1+(int((enemy["lives"]-1)/enemy["lives"] + 0.9))) # pro životy = 1 -> randint(0,1); pro živ. = 2+ -> randint(0,2)
    fight2 = 1
    print(fight,fight2,noise,enemy["position"],enemy["lives"])
    print("--------------------------------------------------------")
var_end = ""
input("Enter pro ukončení hry")
