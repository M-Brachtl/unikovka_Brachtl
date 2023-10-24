# Cíl hry:
Cílem hry je dostat se z komplexu 7 místností, označených 0-6, ven. Venek je znázorněn jako místnost č. 7, která je pro začátek hráči skryta.
Plánek uspořádání místností a jejich propojení je v souboru [a relative link](plan.png)
Východ ven se nachází v jedné z místností 3,5 nebo 6. Hráč se tuto informaci doví po otevření sejfu. K otevření sejfu je potřeba klíč, který má u sebe nepřítel.
# Nepřátelé
Nepřátelský voják se pohybuje v místnostech 3-6, ve speciálních situacích může z trasy vyjít (např. při útěku nebo při jiné hráčově akci).
V jednu chvíli je přítomen jen 1 nepřátelský voják. V případě jeho smrti se objeví nový, v jedné z místností 3-6, ve které se nenachází hráč.
Klíč má jeden z prvních třech vojáků. V nejhorším případě je tedy potřeba zabít 3x nepřátelského vojáka, abys dostal klíč.
# Boj
Pokud jsi v boji, máš na výběr ze dvou možností (viz # Akce). V případě útoku, pokud chceš použít pistoli, kterou máš v inventáři, pokusíš se nepřítele trefit, ale nikdy sám o život nepřijdeš. Útok pěstmi (tedy při zadání čehokoli vyjma "Pistole") má za následek zaručené poranění nepřítele -1 život a stejně tak poranění hráčovo - 1-2 životy.
Také se můžeš pokusit utéct, je tu ovšem šance, že se při útěku poraníš a přijdeš o 1 život.
Během boje se ti nevybíjí baterka (viz # Baterka)
# Baterka
Všude je tma, proto si musíš svítit. Na začátku ji máš nabitou na 100 %, ale každý tah se vybije o 20 %. Při 40 % dostaneš upozornění.
Při vybití na 0 % jsi prohrál.
Dobít ji lze v místnosti 4 samostatnou akcí.
# Akce
Mimo boj:
    Pohyb - Přesun hráče mezi místnostmi, po příchodu do nové místnosti zde najdeš předmět
    Zvedni - Předmět v místnosti, který jsi nesebral můžeš takto přidat do svého inventáře. Nebývá vždy jen jeden
    Použít - Věci ze svého inventáře můžeš použít. Obvaz ti přidá jeden život, gumová kačenka může mít... zajímavé účinky a klíčem lze odemknout sejf.
    Odemkni - Stejný účinek jako akce Použít a zvolení Klíče
    Inventory - Prohledání počtu zvolené věci z inventáře. Na rozdíl od ostatních příkazů se tento nepočítá jako plnohodnotná akce, a proto lze po tomto provést další akci. Inventory lze použít i v boji.
    Dobít - V místnosti 4 si lze dobít baterku na 100 %.
V boji:
    
