""""1-mashq"""
print("Assalomu aleykum!")
ism = input("Ismingizni kiriting: ")
yosh =int(input(("Yoshingizni kiriting: ")))

if yosh<=7 or yosh>=70:
    print("Sizga hayvonot bog'iga kirish bepul")
elif yosh>=8 and yosh<=18:
    print("Sizga hayvonot bog'iga kirish 5000 so'm")
elif yosh>=19 and yosh<=69:
    print("Sizga hayvonot bog'iga kirish 10000 so'm")
elif yosh<=0 :
    print("Musbat son kiriting: ")
elif yosh>=100:
    print("100 gacha bo'lgan son kiriting")


"""2-mashq"""
cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] 
for car in cars:
    if car == "gm":
        print(car.upper())
    else:
        print(car.title())
        
"""3-mashq"""
from math import sqrt
son = int(input("Biron bir son kiriting: "))
if son>=0:
    print(f"Siz kiritgan sonning ildizi {sqrt(son)} ga teng")
elif son<=0:
    print("Musbat son kiriting: ")


"""4-mashq"""
parol = input("Yangi parol kiriting: ")
parol2 = input("Parolingizni tasdiqlash uchun yana bir marta kiriting: ")
if len(parol) >= 8 and parol == parol2:
    print("Parol muvaffaqiyatli bo'ldi")
elif parol != parol2:
    print("Xatolik ! Iltimos parolni qaytadan kiriting ")
else:
    print("Parol eng kamida 8 ta belgidan iborat bo'lishi kk")
    
parol3 = input("Xush kelibsiz parolni kiriting: ")
if parol3 == parol:
     print("Xush kelibsiz!")
else:
    print("Kechirasiz ! Parol xato")


"""5-mashq"""

ism2 = input("Ismingizni kiriting: ")
yosh2 = int(input("Yoshingizni kiriting: "))
tur = input("O'gil bolamisiz yoki Qiz bola: ").lower()
if yosh2==15 and tur=="o'gil":
    print("Siz endilikda 9-Blue sinf o'quvchisisiz")
if yosh2==15 and tur=="qiz":
    print("Endilikda siz 9-Green sinfi o'quvchisisiz")
if yosh2 !=15:
    print("Kechirasiz biz faqat 15 yoshlilarni qabul qilamiz")
