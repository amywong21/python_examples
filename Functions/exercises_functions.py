# 1.) Schreibe eine Funktion, die den Gesamtpreis der Produkte im Warenkorb berechnet!
# Vervollständige die Funktion list_sum(), der als Parameter eine Liste mit den Preisen 
# übergeben wird. Die Funktion soll dann die Summe der Zahlen aus der Liste ausgeben.
cart_prices = [20, 3.5, 6.49, 8.99, 9.99, 14.98]
foodprices = [3.5, 6.49, 8.99, 9.99, 14.98]
generaltaxfactor = 1
foodtaxfactor = 1

def list_sum(price_list, factor):
	sum_of_list = 0
	for price in price_list:
		sum_of_list = price * factor + sum_of_list
		
	print(sum_of_list)
	
list_sum(cart_prices, generaltaxfactor)
list_sum(foodprices, foodtaxfactor)
list_sum(foodprices)
list_sum()

# 2.) Schreibe eine Funktion, die für einen Artikel eine Preis-Tabelle erstellt!
# Nun wünscht sich die Mathmagierin eine Funktion, der sie einen Artikelnamen
# und den Verkaufspreis übergeben kann. Daraus soll die Funktion eine 
# Liste erstellen, in der die Preise von einem, zwei, drei, bis zehn Einheiten des Artikels stehen.
# Genauer soll jedes Element in der Liste so aussehen: 
# "Anzahl x Artikel: Preis".

# Du wunderst dich nur kurz über die Ansprüche der Mathemagierin.
def prices_list(name, price):
	list_of_prices = []
	
	for i in range(10):
		# calculate parts
		factor = i + 1
		factored_price = factor * price
		# concatenate string from parts
		article_price_string = str(factor) + " x " + name + ": " + str(factored_price)
		# alternative ohne factored_price
		#article_price_string = str(factor) + " x " + name + ": " + str(factor * price)
		list_of_prices.append(article_price_string)
		
	return list_of_prices


print(prices_list("Wunderkeks", 0.79))

# 3.) Schreibe eine Funktion, die die Listen mit den Artikeln auffüllt.
# Von nun an soll auch eine Funktion die Waren in die virtuellen Regale 
# einräumen, d. h. an die erste, noch leere Position in der Liste shelf packen. 
# Als Parameter soll der Funktion add_shelf() der einzusortierende Artikel übergeben werden. 
# Die Funktion aktualisiert dann die Liste shelf, und der neue Artikel wurde in das erste leere Regalfach eingeräumt.
shelf = ["Zaubersäge", "leer", "Wunderkekse", "Trickarten", "leer"]

def add_to_shelf(article):
	# hier kommt dein Code hin. 
	# Du darfst von innerhalb der Funktion direkt auf die Variable "shelf"
	# zugreifen, diese muss nicht als Parameter übergeben werden, da sie
	# schon außerhalb der Funktion existiert.

	# ohne leere Regalplätze zu beachten:
	shelf.insert(0, article)

	# mit Beachtung leere Regalplätze:
	for i in range(0, len(shelf)):
		if shelf[i] == "leer":
			shelf[i] = article
		break

add_to_shelf("Rubik's Cube")
add_to_shelf("Feuerwerk")
add_to_shelf("Schatz")
print(shelf)

# 4.) Finde heraus, wie oft der Name "Max" als männlicher Vorname in Kalifornien 
# zwischen 1950 und 2000 (jeweils einschließlich) vergeben wurde. Verwende dazu die 
# bereitgestellte .csv - Datei(../data/names.csv)!
with open("../data/names.csv", "r") as file:
	for line in file:
		line_element_list = line.strip().split(",")
		print(line_element_list)
		break
# ['Id', 'Name', 'Year', 'Gender', 'State', 'Count']

with open("../data/names.csv", "r") as file:
	for line in file:
		line_element_list = line.strip().split(",")

		if line_element_list[2] == "Year":
			continue

		year = int(line_element_list[2])
		name = line_element_list[1]
		gender = line_element_list[3]
		state = line_element_list[4]

		if name  == "Max" and \
			 year >= 1950 and \
			 year <= 2000 and \
			 gender == "M" and \
			 state == "CA":
			print(line_element_list)
			break
# ['587639', 'Max', '1950', 'M', 'CA', '57']

total_count = 0

with open("../data/names.csv", "r") as file:
	for line in file:
		line_element_list = line.strip().split(",")	

		if line_element_list [2] == "Year":
			continue

		year = int(line_element_list[2])
		name = line_element_list[1]
		gender = line_element_list[3]
		state = line_element_list[4]
		count = line_element_list[5]

		if name == "Max" and \
			year >= 1950 and \
			year <= 2000 and \
			gender == "M" and \
			state == "CA":
			total_count = total_count + int(count)

print(total_count)

# 6385