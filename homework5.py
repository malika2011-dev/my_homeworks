
"""1-mashq"""

numbers = [6, 4, 3, 0]

try:
    user = int(input("Son kiriting: "))
    for son in numbers:
        print(f"{son} : {user} = {son / user}")
except ZeroDivisionError:
    print("Xatolik!! Har qanday sonni 0 ga bo'lish mumkin emas!!")
except ValueError:
    print("Xatolik!! Faqat son kiritishingiz mumkin!")
except:
    print("Xatolik!! Qaytadan urinib ko'ring")

"""2-mashq"""
sonlar2 = list(range(1, 1000))
def qoldiqsiz(son:int) -> int:
    x = []
    try:
        for son1 in sonlar2:
            if son1 % son == 0:
                x.append(son1) 
    except ZeroDivisionError:
        print("Xatolik!! Har qanday sonni 0 ga bo'lish mumkin emas!!")
    except ValueError:
        print("Xatolik!! Faqat son kiritishingiz mumkin!")
    except:
         print("Xatolik!! Qaytadan urinib ko'ring")

"""3-mashq"""

try:
    mevalar = ["olma", "nok", "anor", "uzum", "olcha", "shaftoli", "gilos", "behi",  "tarvuz", "qovun"]
    mevalar2 = ["mandarin", "apelsin", "banan", "kivi", "mango"]

    mevalar.remove("olcha")
    mevalar.remove("gilos")

    del mevalar[1]
    del mevalar[-1]

    print(mevalar)

    for meva in mevalar2:
        mevalar.append(meva)
    print(mevalar)

    del mevalar
    mevalar.clear()
    print(mevalar)

except NameError:
    print("xatolik!!! Mevalar ro'yxati o'chib ketgan! uni tozlashga xarakat qilmang")
except:
    print("Xatolik! qaytadan urinib ko'ring")


from datetime import date
bugun = date.today()
yil = int(input("Yil kiriting: "))
oy = int(input("Oy kiriting: "))
kun = int(input("Kun kiriting: "))
uyqichi = date(yil, oy, kun)
print(uyqichi)

print(f"Siz tug'ilganingizga {(bugun-uyqichi).days} kun bo'ldi.")





