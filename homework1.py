"""1-mashq"""
a = int(input("1-sonni kiriting: "))
b = int(input("2-sonni kiriting: "))
c = int(input("3-sonni kiriting: "))

if a >= b and a >= c:
    print(f"Eng kattasi {a}")
elif b >= a and b >= c:
    print(f"Eng kattasi {b}")
elif c >= b and c >= c:
    print(f"Eng kattasi {c}")
elif a == b == c:
    print("Bu sonlar teng")




"""2-mashq"""
havo = float(input("Havo haroratinin kiriting : "))
if havo <= -8:
    print("Havo judayam sovuq uydan chiqmasligingizni maslahat beraman ❗")
elif havo >= -7 and  havo <= 0:
    print("Havo sovuq 🥶 ") 
elif havo > 0 and havo <= 10:
    print("Havo iliq 🙂")
elif havo > 10 and havo <= 30:
    print("Havo juda ham yaxshi 🤩")
elif havo > 30:
    print("Siz Afrikadansiz 👨🏿‍🦱")

"""3-mashq"""
from math import sqrt
from random import randrange
print("Hozir komputer (1-10) gach son tanlaydi uni topishga urininb ko'ring")
f = int(input("Sonni kiriting: "))
c = randrange(1, 11)
if f == c:
    print(f"Tabriklaymiz 🤩🥳🥳. Siz komputer bilan bir xil son o'yladingiz . Bu {c} edi")
elif f != c and c >= 0 or c <= 10:
    print(f"Yutqazdingiz 😛😛😝😜. Komputer {c} ni o'ylagan edi.")
else:
    print("Siz faqatgina 1 - 10 gacha sonlarni kirita olasiz . 🤔")

"""4-mashq"""
sonlar = list(range(101, 700, 2))
for son in sonlar :
    if son < 200 :
        print(f"{son} ning kvadrati {son**2} ga teng")
    elif son > 300 and son < 400:
        print(f"{son} ning ildizi {sqrt(son)} ga teng ")
    elif son > 500 and son < 700:
        print(f"{son} ning 4 - darajasi {son**4}  ga teng")

"""5-mashq"""
yosh = int(input("Yoshingizni kiriting: "))
if  yosh >= 7 and yosh <= 18:
    sinf = int(input("Sinfingizni kiriting: "))
elif yosh < 0 and yosh > 101:
    print("Notog'ri son kiritdingiz 🤨")

"""6-mashq"""
sonlar2 = list(range(201, 500, 2))
for son2 in sonlar2:
    if son2 > 200 and son2 < 300:
        print(f"{son2} ning 4 - darajasi {son2**4}  ga teng")
    elif son2 > 350 and son2 < 400:
        print(f"{son2} ning ildizi {sqrt(son2)} ga teng ")
    elif son2 > 420 and son2 < 480:
        print(f"{son2} ni 3.5 ga bo'lib uch xona aniqlikda yaxlidlasa {round(son2/3.5 , 3)}")
    elif son2 > 480 and son2 < 500:
        print(f"{son2} ning 6 - darajasi {son2**6}  ga teng")

"""7-mashq"""
mevalar = ["olma", "gilos", "oshqovoq", "sabzi", "anjir", "malina"]
for meva in mevalar:
    if meva == "oshqovoq" or meva == "sabzi":
        print(meva.upper())
    else:
        print(meva.title())

"""8-mashq"""

parol = input("Yangi parol kiriting: ")
parol2 = input("Parolingizni tasdiqlash uchun yana bir marta kiriting: ")
if len(parol) >= 8 and parol == parol2:
    print("Parol muvaffaqiyatli bo'ldi")
elif parol != parol2:
    print("Xatolik ! Iltimos parolni qaytadan kiriting ")
else:
    print("Parol eng kamida 8 ta belgidan iborat bo'lishi kerak")  

parol3 = input("Xush kelibsiz parolni kiriting: ")
if parol3 == parol:
     print("Xush kelibsiz!")
else:
    print("Kechirasiz ! Parol xato")
parol3 = int(input("Parolingizni unitdingizmi: ").lower().strip())
if parol3 == "ha" or "xa":
    print("Unda parolni biz o'chirib tashladik . Parolni qaytadan o'rnatishingiz mumkin.")
elif parol3 == "yo'q":
    print("Yaxshi unda parolni kiriitng")

ism = "Malika"
print(f"{ism} eng yaxshisi")
print(f"{ism} eng zo'ri")
print(f"{ism} eng tezkori")





