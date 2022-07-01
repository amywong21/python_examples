
def example_datetime_all():
	example_datetime_01()
	example_datetime_02()
	example_datetime_03()
	example_datetime_04()

from datetime import datetime

def example_datetime_01():
	now = datetime.now()
	print(now)

	# Datetime zu einem bestimmten Datum erstellen.
	date = datetime(2017, 8, 20, 20,0, 0)
	print(date)

	date = datetime(2017, 8, 20, 20,0, 0)
	print(date.year)
	print(date.month)
	print(date.day)
	print(date.hour)
	print(date.minute)
	print(date.second)

def example_datetime_02():
	# Mit der day.timestamp Funktion kommt eine Unix Timestamp zurück.
	date = datetime(2021, 8, 20, 20,0, 0)
	print(date.timestamp())

	# Zeitunterschied in Sekunden zu berechnen.
	now = datetime.now()
	print(date.timestamp() - now.timestamp())

	# Das Python Modul datetime stellt auch die Klassen date und time zur Verfügung,
	# die wir verwenden können, um mit Datumsangaben zu arbeiten. 
	# Nur Datumsangabe:
	from datetime import date, time
	d = date(2017, 8, 20)
	print(d)

	# Nur Zeitangabe
	t = time(20, 1, 4)
	print(t)

	# Vergleichen
	print(date(2017, 8, 20) == date(2017, 8, 20))
	print(datetime(2017, 8, 20, 20, 0, 0) == datetime(2017, 8, 20, 15, 0, 0))

	dt = datetime(2017, 8, 20, 20, 0, 0)
	print(dt.time())
	print(dt.date())

	# Kombinieren von date und time.
	print(datetime.combine(date(2017, 8, 20), time(20, 30, 0)))

def example_datetime_03():
	# Mit Formatierung ausgeben. Nur Tag und Monat ausgeben.
	from datetime import datetime
	now = datetime.now()
	print(now) 
	print(now.strftime("%d.%m.%y"))

	# Abkürzung für Wochentag
	print(now.strftime("%a, %d.%m.%y"))

	# Kann Bindestriche als Zeichen dazwischen setzen.
	print(now.strftime("%d.%m.%y"))
	print(now.strftime("%Y-%m-%d"))
	print(now.strftime("%Y%m%d"))

	# Datumswerte einlesen und verarbeiten
	d =  "18.07.2017"
	print(datetime.strptime(d, "%d.%m.%Y"))

def example_datetime_04():
	# Mit timedelta beschreibe ich eine Zeit oder Datumsdifferenz.
	from datetime import datetime, timedelta
	now = datetime.now()
	print(now)
	print(now + timedelta(days = 20, hours = 4, minutes = 3, seconds = 1)) # dazu gerechnet

	# Wenn du zwei Datumswerte voneinander abziehst,
	# kommt als Ergebnis ein timedelta-Objekt heraus:
	day = datetime(2017, 8, 20)
	timedelta = day - now
	print(timedelta)
	#print(day - now)

	# Oder die Differenz als Sekunden ausgeben.
	day = datetime(2017, 8, 20)
	timedelta = day - now
	print(timedelta.total_seconds())
	
	# Kann datetime auch auf ein datetime aufaddieren.
	print(datetime(2018, 1, 1) + timedelta)

	# Wie erstellt du für das `datetime` -Objekt `day` , das per `day = datetime.now()` erzeugt wurde, 
	# eine Datumsanzeige in der folgenden Gestalt?: `Monday, 12th of January`
	from datetime import datetime
	import locale

	# je nach Betriebssystem heißt die 'de_DE.UTF-8' oder unter Windows 'deu', 'german'
	locale.setlocale(locale.LC_ALL, 'de_DE')
	day = datetime.now()
	print(day.strftime("%A, %dth of %B"))

example_datetime_all()