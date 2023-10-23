n = int(input("podaj ilosc liczb"))
wypisz = []
for i in range(n):
    x = float(input(f"podaj a{i+1}"))
    wypisz.append(x)
    for y in wypisz[:2]:
        print(y)
print(wypisz[0])

