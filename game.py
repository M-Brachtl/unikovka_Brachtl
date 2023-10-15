from random import randint
# startovní nastavení
possibilities = ("Move","Pick up","Attack","Run away")
rooms_doors = ((1,2,3,4),(0,2,4,5),(0,1,3),(0,2,4,6),(0,1,3,5,6),(1,4,6),(3,4,5)) # možnosti přesunu v místnostech
rooms_visit = ["Nic","","","","",""]
things = ("Red key","Blue key","Axe","Obvaz","Gumová kačenka")
inventory = ["Obvaz"] # inventář hráče
invent_state = [1] # zbylý počet použití odpovídajícího předmětu v inventáři
player = {
    "lives": 5,
    "position": 0
}
while True:
    print("Možné akce:",possibilities)
    decision = input("Zadej svoji akci: ")
    if decision == "Move": # přesun mezi místnostmi
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
    elif decision == "Pick up":
        if rooms_visit[player["position"]] in things:
            if rooms_visit[player["position"]] in inventory:
                invent_state[inventory.index(rooms_visit[player["position"]])] += randint(2,4)
            else:
                inventory.append(rooms_visit[player["position"]])
                invent_state.append(randint(2,4))
            rooms_visit[player["position"]] = "Nic"
        else:
            print("Nic zde není k sebrání.")
    elif decision == "Inventory":
        print(inventory)
        ref_thing = input("Zadejte věc z inventáře, které počet chcete znát: ")
        if ref_thing in inventory:
            print(f"{ref_thing} lze použít ještě {invent_state[inventory.index(ref_thing)]}x")
        else: print("Tato věc se nenachází ve vašem inventáři.")
        ref_thing = "Nichts"
    elif decision == "Use":
        ref_thing = input("Kterou věc z inventáře chcete použít? ")
        if ref_thing in inventory:
            ref_index = inventory.index(ref_thing)
            if ref_thing == "Obvaz":
                player["lives"] += 1
                invent_state[ref_index] += -1
            if invent_state[ref_index] == 0:
                invent_state.remove(invent_state[ref_index])
                inventory.remove(ref_thing)
            ref_index = 0
        ref_thing = "Nichts"
    elif decision == "Player":
        print(player)

