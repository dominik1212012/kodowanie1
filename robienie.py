nazwa = "damian"
print(nazwa[2:])

def odw(nazwa):
    s = ""
    for i in nazwa[0:]:
        s = i + s
    print(s)
print(odw(nazwa))

