import datetime
import sys

print ("Podaj nazwe uzytkownika:")
username = str(input())


def questions():

	print("Wybierz, co ma wykonac program: \n")
	print("1. Pokaz informacje o uzytkowniku i wszystkie wpisy z waga. \n")
	print("2. Dodaj wpis z aktualna waga. \n")
	print("3. Wyswielt informacje odnosnie osiagniecia idealnego BMI. \n")
	print("4. Zamknij program \n")
# Wykonanie polecenia nr 1:

def show():

	with open(username, "r") as f:
		try:
			a = f.read()
		finally:
			print(a) 
# Wykonanie polecenia nr 2:

def add():

	data = datetime.datetime.now()
	info = data.strftime("%H:%M:%S %p %d. %b. %y")
	print("Aktualizacja wartosci BMI \n")
	print("Ile teraz wazysz[kg]? \n")
	mass = float(input())
	print("Ile masz teraz wzrostu[m]?")
	height = float(input())
	BMI = mass/(height ** 2)
	BMI = round(BMI,2)
	mass = str(mass)
	BMI = str(BMI)
	height = str(height)
	with open(username, "a") as f:
		f.write("\n")
		f.write("Aktualizacja danych: " + info)
		f.write("\n")
		f.write("Waga: ")
		f.write(mass)
		f.write(" Wzrost: ")
		f.write(height)
		f.write(" BMI: ")
		f.write(BMI)
# Wykonanie polecenia nr 3:

def predict_ext():
# Pobieranie poczatkowej wagi:
	with open(username, "r") as f:
		lines = f.readlines()
		for x in lines:
			x = lines[5]
	x= x[6:8]
	x = int(x)
# Pobieranie ostatniej lini:
	with open(username, "r") as f:
		lines = f.readlines()
		for line in lines:
			line = lines[-1]
# Pobieranie aktualnej wagi:
	y = line[6:10]
	y = float(y)
# Pobieranie aktualnego wzrostu:
	height_1 = line[19:23]
	height_1 = float(height_1)
# Prawidlowe BMI na podstawie sredniej:
	BMI = float(21.75)
# Obliczanie prawidlowej masy ciala:
	mass_1 = BMI*(height_1**2)
	if y == mass_1:
		print("Masz prawidlowa wage!")
	elif y < mass_1:
		print("Wazysz za malo!")
		if x >y:
			print("Tracisz na wadze w stosunku do Twojej poczatkowej wartosci! Musisz przybrac na wadze!")
		elif x < y:
			print("Przybrales na wadze w stosunku do poczatkowej wartosci, jednak to nadal za malo! Pracuj dalej, a osiagniesz sukces!")
		else:
			print("Wazysz tyle samo, co na poczatku pomiaru. Musisz koniecznie popracowac nad dieta, aby przybrac na wadze!")
	else:
		print("Wazysz za duzo!")
		if x < y:
			print("Przytyles w stosunku do poczatkowej wartosci! Musisz zrzucic zbedne kilogramy!")
		elif x >y:
			print("Straciles na wadze w stosunku do poczatkowej wartosci, jednak to dalej za malo! Pracuj dalej, a osiagniesz sukces!")
		else:
			print("Wazysz tyle samo, co na poczatku pomiaru. Musisz koniecznie popracowac nad dieta, aby stracic na wadze!")
# Wykonanie glownej funkcji predict

def predict_main():

	with open(username, "r") as f:
		lines = f.readlines()
		for line in lines:
			line = lines[-1]
	BMI_1 = float(line[29:34])
	if BMI_1 < 16:
		print("Aktualna wartosc BMI wskazuje na wyglodzenie.\n")
		predict_ext()
	elif BMI_1 > 16 and BMI_1 < 17:
		print("Aktualna wartosc BMI wskazuje na wychudzenie.\n")
		predict_ext()
	elif BMI_1 > 17 and BMI_1 < 18.5:	
		print("Aktualna wartosc BMI wskazuje na niedowage.\n")
		predict_ext()
	elif BMI_1 > 18.5 and BMI_1 < 25:
		print("Aktualna wartosc BMI wskazuje na prawidlowa wage.\n")
		predict_ext()
	elif BMI_1 > 25 and BMI_1 < 30:
		print("Aktualna wartosc BMI wskazuje na nadwage.\n")
		predict_ext()
	elif BMI_1 > 30 and BMI_1 < 35:
		print("Aktualna wartosc BMI wskazuje na I stopien otylosci.\n")
		predict_ext()
	elif BMI_1 > 35 and BMI_1 < 40:
		print("Aktualna wartosc BMI wskazuje na II stopien otylosci.\n")
		predict_ext()
	else:
		print("Aktualna wartosc BMI wskazuje na skrajna otylosc.\n")
		predict_ext()
# Wykonanie polecenia nr 4:

def exit():
	
	sys.exit()
# Glowne dzialanie programu:


def main():

	try:
		f = open(username, "r")
		f.close()
	except FileNotFoundError:
		with open(username, "w") as f:
			name = str(input("Imie: "))
			surname = str(input("Nazwisko: "))
			age = str(input("Wiek: "))
			sex = str(input("Plec: "))
			height = str(input("Wzrost: "))
			mass = str(input("Waga: "))
			f.write("Imie: " + name)
			f.write("\n")
			f.write("Nazwisko: " + surname)
			f.write("\n")
			f.write("Wiek: " + age)
			f.write("\n")
			f.write("Plec: " + sex)
			f.write("\n")
			f.write("Wzrost: " + height)
			f.write("\n")
			f.write("Waga: " + mass)
			f.write("\n")
	questions()
	x = int(input())
	if x == 1:
		show()
	elif x == 2:
		add()
	elif x == 3:
		predict_main()
	else:
		exit()
	
while True:
	main()


