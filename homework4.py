

"""1-mashq"""

ism = input(" Do'stingizni ismini kiriting: ")
famiiya = input(" Do'stingizni familiyasini kiriting: ")
nomer = input(" Do'stingizni nomerini kiriting: ")
print(f"Do'stimni ismi {ism}, familiyasi {famiiya}, nomeri: {nomer}")

"""2-mashq"""
while True:
    son = input("son kiriting: ")
    if son == "stop" or son == "quit":
        print("dastur tugadi!!!")
        break
    son1 = input("ikkinchi sonni kiriting: ")
    if son1 == "stop" or son1 == "quit":
        print("dastur tugadi!!!")
        break
    if son > son1:
        print(f"{son} > {son1}")
    elif son < son1:
        print(f"{son} < {son1}")
    else:
        print(f"{son} = {son1}")


ishora = True
while ishora:
    yil = int(input("Yilingizni kiriting:"))
    print(f"Siz {202-yil} yoshdasiz")
    
    savol = input("Davom etasizmi ?") 
    if savol == "exit":
        print("Dastur tugadi !")
        ishora = False




sonlar = list(range(1,100))
for son in sonlar:
    print(round(son))


# 1 dan 500 gacha ro'yhatni chiqaz va 1 dan 100 ildizini chiqar 
# keyin 1 dan 500 gacha bo'lgan sonlarni tasodif son chiqsun va hammasini konsilga chiqaz

from math import sqrt
sonlar = list(range(2, 500, 2))
for s in sonlar:
    print(sqrt(s))
from random import randrange
for son in sonlar:
    print(randrange(son))


"""sort() operatori"""
ism = ["alisher", "malika", "hadicha", "zakariyo"]
ism.append("umida")
print(ism)
ism.insert(3, "rano")
print(ism)
del ism[-1]
print(ism)
ism.pop
print(ism)
ism.pop(-3)
print(ism)
qiz = []
qiz.append(ism.pop(-1))
print(qiz)

ism.sort()
print(ism)
ism.sort(reverse=True)
print(ism)

"""mashq"""
print("Assalomu aleykum do'konimizga hush kelibsiz")
makazin = ["olma", "sut", "chips", "limon", "non", "banan"]
print(f"Do'konimizda quidagi mahsulotlar bor: Ular {makazin} ", end="")
olaman = []


savol = input("nechta mahsulot olmoqchisiz: ")
for x in range(savol):
    olaman.append(f"{x+1}-mahsulotni kiriting: ")
for ol in olaman:
    if ol in makazin:
        print("Bu mahsulot bizda bor")
    else:
        print("Bizda bu mahsulot yo'q")



    