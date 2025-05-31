"""7G008CH1"""
from math import sqrt
"""1-Mashq"""
ism = input("Ismingizni kiriting: ")
yosh = int(input("Yoshingizni kiriting: "))
print(f"Salom mening ismim {ism.title()} yoshim {yosh} da")

"""2-mashq"""
print((23**4) + (sqrt(32654)))
print((95**3) - (6**4))
print(round(52.8447 , 3))
print(sqrt(225))
print(2**9)

"""3-mashq"""
a = int(input("To'g'ri to'rtburchakning 1 - tomonini kiriting: "))
b = int(input("To'g'ri to'rtburchakning 2 - tomonini kiriting: "))
print(f"Tomonlari {a} va {b} bo'lgan tog'ri to'rtburcakning premetri {2*(a+b)} yuzi esa {a*b} ga teng")

"""4-mashq"""
c = list(range(1, 120, 2))
d = list(range(100, 200, 2))
e = list(range(14, 120, 14))
f = list(range(-14, 320, 7))
g = list(range(20, 100, 20))

"""5-mashq"""
ismlar = []
for ism in range(7):
    ismlar.append(input(f"{ism + 1} - Ismni kiriting: ").strip().title())
ismlar[0] = "Malika"
# ismlar[-1] = "Zilola"
# ismlar.append("Shphsanam")
# ismlar.insert(0, "Fotima")
# ismlar.remove("Malika")
# ismlar.pop()
# del ismlar[-1]
# print(ismlar)

import turtle 

# Ekran yaratish
screen = turtle.Screen()
screen.bgcolor("white")

# Turtle ob'ekti yaratish
pen = turtle.Turtle()
pen.shape("turtle")
pen.color("red")
pen.speed(3)

# Yurak shaklini chizish
pen.begin_fill()
pen.left(50)
pen.forward(133)
pen.circle(50, 200)
pen.right(140)
pen.circle(50, 200)
pen.forward(133)
pen.end_fill()

# Ekranni yopish uchun bosish
turtle.done2








