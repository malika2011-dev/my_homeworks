"""9G004"""

"""1-mashq"""

sonlar = []
sonlar.append(int(input("1-sonni kiriting: ")))
sonlar.append(int(input("2-sonni kiriting: ")))
sonlar.append(int(input("3-sonni kiriting: ")))

print(f"Siz kiritigan sonlarning ichida {max(sonlar)} soni eng kattasi")
print(f"Siz kiritigan sonlarning ichida {min(sonlar)} soni eng kichigi")
print(f"Bu sonlarning yigindi {sum(sonlar)} ga teng")

"""2-mashq"""
sonlar2 = [45, -96, 0, 63.2, 1257, -6752.2, 42, 3, 542]
print(f"O'sish tartibi {sorted(sonlar2)}")
print(f"Kamayish tartibi {sorted(sonlar2, reverse =True)}")
sonlar2.reverse()
print(f"Aylantirilgani  {sonlar2} ")

"""3-mashq"""
mevalar = ["olma", "o'rik", "shaftoli", "apelsin", "malina", "xurmo"]
for meva in mevalar:
    if meva == "olma" or meva == "malina":
        print(meva.upper())
    else:
        print(meva.title())

"""4-mashq"""
son = int(input("Nechta meva nomini kiritmoqchisiz: "))
mevalar =[]
for s in range(son):
    meva = input(f"{s+1} - mevangiz nomini kiriting: ")
    mevalar.append(meva)
print(f" Siz kiritgan mevalar : {mevalar}")


"""5-mashq"""
print("Hozir siz ikki son kiritasiz men sizga ularni taqqoslab beraman")
son1 = int(input("1-sonni kiriting: "))
son2 = int(input("2-sonni kiriting: "))
if son1>son2:
    print(f"{son1} > {son2}")
elif son1 ==son2:
    print(f"{son1} = {son2}")
else:
    print(f"{son2} > {son1}")

#  yoki
# sonlar = []
# sonlar.append(son1)
# sonlar.append(son2)
# print(f"{max(sonlar)} katta {min(sonlar)} kichik")
    

"""9G005"""
from math import sqrt
"""1-mashq"""
sonlar3 = list(range(5, 873 , 2))
for son in sonlar3:
    print(f"{son} ning ildizi {sqrt(son)}")


"""2-mashq"""
ism = input("Ismingizni kiriting: ").title()
if ism == "Muslima":
    print(f"Salom {ism}, Davramizga hush ko'rdik!")
elif ism == "Sevara" or "Zilola":
    print(f"Salom {ism} sizga qanday yordamim  kerak: ")
elif ism == "Anvar" or "Aziz":
    print(f"Salom {ism} bugun qayerga boramiz : ")
else :
    print("Kechirasiz")


"""3-mashq"""
sonlar4 = list(range(102, 2020))
for son2 in sonlar4:
    if son2 in sonlar4 and son2>1000:
        print(f"{son2} ning kubi {son2**3} ga teng")
    if son2 in sonlar4 and son2<1500:
        print(f"{son2} dan 4 ta keyin keluvchi son {son2+4} ")
    if son2 in sonlar4 and son2%7 ==0:
        print(f"{son2} ning ildizi {sqrt(son2)} ga teng")

"""4-mashq"""
sonlar6 = list(range(-321, -2, 2))
for son3 in sonlar6:
    print(f"{son3}ning 5-darajasi {son3**5} ga 7-darajasi esa {son3**7} ga teng")
    print(f"{son3} dan 4 taga kichik bo'lgan son {son3-4} ga teng")
print(f"Uzunligi: {len(sonlar6)}")
print(f"O'sish tartibi: {sorted(sonlar6)}")
print(f"Kamayish tartibi : {sorted(sonlar6, reverse = True )}")

"""5-mashq"""
a = int(input("1-sonni kiriting: "))
b= int(input("2-sonni kiriting: "))
if a>b:
    print(f"{a} > {b}")
elif a<b:
    print(f"{b} > {a}")
elif a==b:
    print(f"{a} = {b}")


"""9G006"""
"""1-mashq"""
x = list(range(201, 400, 2))
y = list(range(302, 500, 2))
z= list(range(25, 600, 25))

"""2-mashq"""
davlatlar = ["O'zbekiston", "Turkmaniston", "Qozog'iston", "Tojikiston", "Ozaybarjon", "Turkiya", "BAA", "AQSH"]
del davlatlar[-1]
davlatlar.pop()
davlatlar.pop(-1)
davlatlar.append("Qoraqalpog'iston")
davlatlar.insert(-1, "Qirg'ig'iston")
print(davlatlar)


"""3-mashq"""
names = ["Laylo", "Mastona", "Dilshoda", "Zinnatoy", "Muhlisa"]
ism_1 = input("Ismingizni kiriting: ")
if ism_1 in names:
    print("Kechirasiz, Sizning ismingiz mening ro'yxatimda bor ekan.")
else:
    print("Xush kelibsiz! ")

"""4-mashq"""
oquv_qurollari = ["Qalam", "Daftar", "Sumka", "Jazbar", "O'chirg'ich", "Chiqarg'ich", "Ruchka"]
sotuvlar=[]
print(f"Bizda bor mahsulotlar : {oquv_qurollari}")
sanoq = int(input("Nechta buyum olmoqchisiz: "))
for mahsulot in range(sanoq):
    sotuvlar.append(input(f"{mahsulot+1} - Mahsulot nomini kiriting: "))
for sotuv in sotuvlar:
    if sotuv in oquv_qurollari:
           print(f"Bizda {sotuv} mahsuloti bor")
    else:
           print(f"Kechirasiz bizda {sotuv} mahsuloti yo'q!")
           










    







