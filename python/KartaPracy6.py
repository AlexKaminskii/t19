# zad 1

# a = int(input())
# b = int(input())
# c = int(input())

# if a - b == b - c:
#     print("Arytmetyczny - TAK")
# else:
#     print("Arytemtyczny - NIE")

# if a * b == c:
#     print("Geometryczny - TAK")
# else:
#     print("Geometryczny - NIE")

# if a < b < c:
#     print("Rosnący - TAK")
# else:
#     print("Rosnący - NIE")

# if a > b > c:
#     print("Malejący - TAK")
# else:
#     print("Malejący - NIE")

# zad 2

# suma = 0
# for i in range(100, 1000):
#     if i % 8 == 0 and i % 16 != 0:
#         suma += i
# print(suma)


# zad 3

# liczba = 0
# for i in range(10,100):
#     if i % 7 == 0:
#         liczba = i
# ilosc = 0
# for j in range(1000, 10000):
#     if j % liczba == 0:
#         ilosc += 1
# print(ilosc)


# zad 4



# suma = 0
# for i in range(10,100):
#     if i % 10 <= (i // 10) * 2:
#         suma += 1
# print(suma)


# zad 5


# suma = 0
# ilosc = 0
#
# for i in range(100,1000):
#     if i//100 > (1%10) + (1//10)%10:
#         suma += i
#         ilosc += 1
# print("Suma: ", suma)
# print("Ilość: ", ilosc)


# zad 6


# n = int(input())
# suma = 0
# for i in range(10, 100):
#     if i % 19 == 0:
#         suma += i
#         n -= 1
#     if n == 0:
#         break
#     else:
#         continue
# print(suma)

# zad 7

# n = int(input())
# suma = 0
#
# for i in range(999,99,-1):
#     if i % 37 == 0:
#         suma += i
#         n -= 1
#     if n == 0:
#         break
#     else:
#         continue
# print(suma)


# zad 8


# n = int(input())
# suma = 0
# znak = 3
# a = 2
# for i in range(n):
#     suma += a * znak
#     a += 1
#     znak = znak * -1
# print(suma)


# zad 9


# n = int(input())
# wynik = 1
# a = 1
# b = 0
# znak = 1
# for i in range(n):
#     wynik = wynik * ((a * -2) * znak)
#     a = (a * -2) * znak
#     znak = znak * -1
# print(wynik)


# zad 10


# n = int(input())
# wynik = 0

# def silnia(n):
#     wynik = 1
#     while n > 0:
#         wynik = wynik * n
#         n -= 1
#     return wynik

# for i in range(n):
#     wynik = wynik + silnia(n)
#     n -= 1
# print(wynik)
