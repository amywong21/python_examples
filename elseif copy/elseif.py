def example_else_if():
	print("Running example_else_if from module elseif")
	currency = "€"

	if currency == "$":
		print("US-Dollar")
	elif currency == "¥":
		print("Japanischer Yen")
	elif currency == "€":
		print("Euro")
	elif currency == "฿":
		print("Thai Baht")
	else: 
		print("sonstige Währung")