# 1.) Gib nacheinander alle Kontinente aus der Liste continents aus.
print("1.) Gib nacheinander alle Kontinente aus der Liste continents aus.")
continents = ["Afrika", "Antarktis", "Asien", "Australien und Ozeanien", "Europa", "Nordamerika", "Südamerika"]

for i in continents:
    print(i)

# 2.) Gib aus der Liste continents nur die bewohnten Kontinente aus.
print("2.) Gib aus der Liste continents nur die bewohnten Kontinente aus.")
continents = ["Afrika", "Antarktis", "Asien", "Australien und Ozeanien", "Europa", "Nordamerika", "Südamerika"]

for continent in continents:
	if continent == "Antarktis":
		continue
	print(continent)

# 3.) Gib aus der Liste stuff nur die Kontinente aus.
print("3.) Gib aus der Liste stuff nur die Kontinente aus")
stuff = ["Asien", "Max", 101, "Monika", "China", "Simbabwe", "Antarktis"]

for i in stuff:
	if i in continents:
		print(i)

# 4.) Wie viele Kontinente sind in der Liste stuff enthalten?
print("4.) Wie viele Kontinente sind in der Liste stuff enthalten?")
count = 0 

for i in stuff:
	if i in continents:
		count = count + 1
print(count)

# oder
count = 0 

for i in stuff:
	if i in continents:
		count += 1
print(count)

# oder
contis = []

for i in stuff:
	if i in continents:
		contis.append(i)

print(len(contis))

# 5.)Gib für die Variable price den neuen, rabattierten Preis aus.
print("5.) Gib für die Variable price den neuen, rabattierten Preis aus.")
price = 50
# 0,<=20, >20,<=50, >50

new_price = 50

if price > 0 and price <= 20:
    new_price = price * 0.8
elif price > 20 and price <= 50:
    new_price = price * 0.6
elif price > 50:
    new_price = price * 0.4
else:
    print("Du hast eine negative Zahl eingegeben")

print(new_price)

# 6.)Berechne nun für jeden der alten Preise aus der Liste *prices* die passenden reduzierten Preise und speichere sie in der neuen Liste new_prices. 
print("6.) Berechne nun für jeden der alten Preise aus der Liste prices die passenden reduzierten Preise und speichere sie in der neuen Liste new_prices.")
# Gib diese Liste schließlich aus.
prices = [2, 50, 70, 30]
new_prices =[]

new_price = 50

for price in prices:
    if price > 0 and price <= 20:
        new_price = price * 0.8
        #new_prices.append(new_price) entweder in jedem case oder danach einmal
    elif price > 20 and price <= 50:
        new_price = price * 0.6
        #new_prices.append(new_price)
    elif price > 50:
        new_price = price * 0.4
        #new_prices.append(new_price)
    else:
        print("Du hast eine negative Zahl eingegeben")
    new_prices.append(new_price)      
    
print(new_prices)

# 7.)Gehe die Elemente in der Liste *chaos* durch. Bei einem neuen Preis 
# ziehst du bloß den neuen Wert aus dem String und hängst ihn der Liste *order* an. 
# Bei einem alten Preis hingegen holst du dir den alten Wert, berechnest 
# den neuen Preis und hängst diesen Wert an die Liste *order*.
# Schließlich gibst du die vollständige Liste *order* aus, in der nur noch neue Preise
# drinstehen (und nur noch Zahlen!).
# Tipp: Mit Hilfe des `in` - Operators kannst du prüfen, ob `old` oder `new` in einem
# Listenelement vorkommt (`"old" in "old price: 123"`), und entsprechend entscheiden,
# ob du die Rabatierung durchführen möchtest oder nicht.

print("7.) Schließlich gibst du die vollständige Liste *order* aus, in der nur noch neue Preise drinstehen (und nur noch Zahlen!).")
chaos =["old price: 40", "new price: 21", "old price: 29", "old price: 50", "new price: 101"]
order = []

for price_string in chaos:
    if "new" in price_string:
        new_price = int(price_string.split(":")[1])
        order.append(new_price)
    elif "old" in price_string:
        old_price = int(price_string.split(":")[1]) 
        if old_price > 0 and old_price <= 20:
            new_price = old_price * 0.8
            #new_prices.append(new_price) entweder in jedem case oder danach einmal
        elif old_price > 20 and price <= 50:
            new_price = old_price * 0.6
            #new_prices.append(new_price)
        elif old_price > 50:
            new_price = old_price * 0.4
            #new_prices.append(new_price)
        order.append(new_price)      

print(order)