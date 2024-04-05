import math

def pole_kola(promien):
    return math.pi * (promien ** 2)

def pole_kwadratu(bok):
    return bok ** 2

def pole_trojkata(podstawa, wysokosc):
    return (podstawa * wysokosc) / 2

# Podanie wartości 
promien_kola = 8
bok_kwadratu = 12
podstawa_trojkata = 14
wysokosc_trojkata = 16

# Obliczenia
pole_k = pole_kola(promien_kola)
pole_kw = pole_kwadratu(bok_kwadratu)
pole_tr = pole_trojkata(podstawa_trojkata, wysokosc_trojkata)

# Wyświetlenie wyników
print(f"Pole koła o promieniu {promien_kola} wynosi: {pole_k:.2f}")
print(f"Pole kwadratu o boku {bok_kwadratu} wynosi: {pole_kw:.2f}")
print(f"Pole trójkąta o podstawie {podstawa_trojkata} i wysokości {wysokosc_trojkata} wynosi: {pole_tr:.2f}")
