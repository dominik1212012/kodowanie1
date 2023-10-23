import math
import sys

# A
sum_parzystych = 0
for i in range(1, 101):
    if i % 2 == 0:
        sum_parzystych += i
print("Suma liczb parzystych od 1 do 100 (włącznie) wynosi: ", sum_parzystych)

# B
sum_kwadratowych = 0
for i in range(1, 101):
    sum_kwadratowych += i ** 2
print("Suma kwadratów liczb od 1 do 100(włącznie) wynosi: ", sum_kwadratowych)

# C
suma_poteg = 0
for liczba in range(1, 64):
    suma_poteg += 2 ** liczba
print("Suma Potęg Liczby 2 od 1 da 63 (Włącznie) wynosi: ", suma_poteg)

#  D
input_a = int(input("Wprowadz liczbę A: "))
input_b = int(input("Wprowadz liczbę B: "))
sum_ab = 0
for liczba_nie_parzysta in range(input_a, input_b + 1):
    if liczba_nie_parzysta % 2 == 1:
        sum_ab += liczba_nie_parzysta

    elif input_a > input_b:
        sum_ab = 0
        print("O")
print("Suma liczb nieparzystych na odcinku od A do B(włącznie) wynosi: ", sum_ab)

# ZADANIE 2
'''Do każdego z poniższych punktów należy napisać odpowiedni program. W każdym z tych
programów wczytać liczbę naturalną n, a następnie wczytując kolejno n liczb rzeczywistych
obliczyć wartość odpowiednich wyrażeń:
-- >(a) a1 + a2 + . . . + an

-- >(b) a1 · a2 · . . . · an

-- >(c) |a1| + |a2| + . . . + |an|

-- >(d) p |a1| + p |a2| + . . . + p |an|

-- >(e) |a1| · |a2| · . . . · |an|

-- >(f) a21 + a22 + . . . + a2n

-- >(g) a1 + a2 + . . . + an oraz a1 · a2 · . . . · an

-- >(h) a1 − a2 + a3 − . . . + (−1)n+1· an

-- >(i) −a1 1 1! + a2 2! − . . . + (−1)n·an n!'''


# 2.A.1
def suma_liczb():
    n = int(input(" Podaj ilosć liczb: "))
    suma = 0
    for i in range(1, n + 1):
        j = float(input(" Podaj kolejną liczbe rzeczywistą: "))
        suma += j
    print(" Suma podanych ", n, " liczb wynosi: ", suma)


suma_liczb()


# 2.B
def mnozenie():
    n = int(input("Podaj liczbę: "))
    wielomian_liczb = 1
    for i in range(1, n + 1):
        j = float(input(f" Podaj liczbę a{i} : "))
        wielomian_liczb *= i
    print("Mnożenie liczb od 1 do ", n, " wynosi: ", wielomian_liczb)


mnozenie()


# 2.C
def suma_modul():
    n = int(input(" Podaj ilosć liczb: "))
    suma = 0
    for i in range(1, n + 1):
        j = abs(float(input("Podaj kolejną liczbe rzeczywistą:")))
        suma += j
    print(" Suma modulów podanych ", n, " liczb wynosi: ", suma)


suma_modul()


# 2.D
def suma_pierwiastkow():
    n = int(input(" Podaj ilosć liczb: "))
    suma = 0
    for i in range(1, n + 1):
        j = abs(float(input("Podaj kolejną liczbe rzeczywistą:")))
        suma += math.sqrt(j)
    print(" Suma pierwiastków podanych ", n, " liczb wynosi: ", suma)


suma_pierwiastkow()


# 2.E
def wilomian_modulow():
    n = int(input(" Podaj ilosć liczb: "))
    suma = 1
    for i in range(1, n + 1):
        j = abs(float(input("Podaj kolejną liczbe rzeczywistą:")))
        suma *= j
    print(" Suma pierwiastków podanych ", n, " liczb wynosi: ", suma)


wilomian_modulow()


# 2.F
def suma_kwadratow():
    n = int(input("Podaj ilosć liczb: "))
    suma_kwadrat = 0
    for przeganianie_petli in range(1, n + 1):
        j = float(input("Podaj kolejną liczbe rzeczywistą: "))
        suma_kwadrat += j ** 2

    print(" Suma kwadratów podanych ", n, " liczb wynosi: ", suma_kwadrat)


suma_kwadratow()


# 2.G
def suma_i_wielomian():
    n = int(input(" Podaj ilosć liczb : "))
    suma = 0
    wielomian = 1
    for i in range(1, n + 1):
        j = float(input(" Podaj kolejną liczbe rzeczywista : "))
        suma += j
        wielomian *= j
    print("Suma podanycch ", n, " liczb wynosi: ", suma)
    print("Wielomian podanycch ", n, " liczb wynosi: ", wielomian)


suma_i_wielomian()


# 2.H
def suma_i_roznica():
    n = int(input(" Podaj ilosć liczb : "))
    suma_i_roznica = 0
    for i in range(1, n + 1):
        j = int(input(" Podaj kolejną liczbe rzeczywista :"))
        j = j * ((-1) ** (i + 1))
        suma_i_roznica += j

    print("Suma i roznica podanych ", n, " liczb wynosi: ", suma_i_roznica)


suma_i_roznica()


# 2.I
def suma_i_rozn_dzielen():
    n = int(input(" Podaj ilosć liczb : "))
    suma_i_rozn_dzielen = 0
    for i in range(1, n + 1):
        j = float(input(" Podaj kolejną liczbe rzeczywistą: "))
        j = j * ((-1) ** i)
        suma_i_rozn_dzielen += j / math.factorial(i)

    print("Suma i roznica dzielen podanych ", n, " liczb: ", suma_i_rozn_dzielen)


suma_i_rozn_dzielen()


# Zadanie nr 3 Wczytać liczbę naturalną n, a następnie wczytując kolejno ciąg n liczb rzeczywistych
# a1, a2, . . . , an wypisać w kolejnych liniach liczby tego ciągu w następującej kolejności:
# a2, a3, . . . , an, a1.
# Przykładowe działanie programu dla n = 3 i ciągu 10, 20, 30:

def wyswiewl_kolejnosc():
    n = int(input("Podaj iłość liczb: "))
    liczby = []

    for i in range(1, n + 1):
        j = float(input(f"Podaj kolejną liczbe rzeczywistą a{i}: "))
        liczby.append(j)

    przetasuje_liczby = liczby[1:] + [liczby[0]]

    for liczba in przetasuje_liczby:
        print(liczba)


wyswiewl_kolejnosc()

# ZADANIE NR4 print("Mężny bądź, chroń pułk twój i sześć flag") 64 razyz

ilosc = 0
while ilosc < 65:
    print("Mężny bądź, chroń pułk twój i sześć flag.")
    ilosc += 1




