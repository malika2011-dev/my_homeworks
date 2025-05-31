# "9G005"

# """1-mashq"""
from math import sqrt

# for son in range(5, 483 , 2):
#     print(f"{son} ning ildizi {sqrt(son)} ga teng")

# # qolganlari oldin qilganakanman
    
# "9G007"

# """2-mashq"""

# friend = {}
# friend["ism"] = input("Do'stingizni ismini kiriting: ")
# friend["familya"] = input("Do'stingizni familyasini kiriting: ")
# friend["yosh"] = int(input("Do'stingizni yoshini kiriting: "))
# friend["manzil"] = input("Do'stingizni manzilini kiriting: ")
# friend["e-mail"] = input("Do'stingizni e- mailini kirting: ")
# print(friend)

# """3-mashq"""
# eng_uzb = {"book":"kitob", "pen":"qalam", "pencil":"ruchka"}
# for key, values in eng_uzb.items():
#     javob = input("Ingilizcha so'z kiriting : ").lower()
#     if javob in eng_uzb:
#         print(eng_uzb[javob])
#     else:
#         print("Kechirasiz bizda bunday so'z mavjud emas!")

"""4-mashq"""
books = {"kitob1":"mehrobdan chayon", "kitob2":"kichkina shahzoda"}
books["kitob3"] = "hamsa"
books.get("book4" , "dunyoning ishlari")
books["kitob1"] = "jannati odamlar"
books.get("kitob4", "bilmasvoy")
print(books)
del books["kitob1"]
books.pop("kitob2")
books.pop("kitob3")

print(books)
# man o'chirish qo'shish, yangilashni hammasini 1 tadan usulini bilaman

"""9GCH1"""
name = " AnToNy "
print(name.rstrip())
print(name.lstrip())
print(name.upper())
print(name.lower())

"""2-mashq"""
ismlar = ["malika", "zilola", "shohsanam", "fotima", "zuhra", "iroda"]
print(len(ismlar))
print(sorted(ismlar))
print(sorted(ismlar, reverse = True))
ismlar.remove("malika")
ismlar.insert(0, "saida")
ismlar.insert(-1, "sevara")
print(ismlar)


"""3-mashq"""
sonlar = list(range(101 ,700 , 2))
for son in sonlar:
    if son<200:
     print(f"{son} ning 2-darajasi {son**2}")
    elif son>300 and son<400:
     print(f"{son} ning ildizi {sqrt(son)}")
    elif son>500 and son<700:
     print(f"{son} ning 4 - darajasi {son**4}")
    
"""4-mashq"""
yosh = int(input("Yoshingizni kiriting: "))
if yosh>=7 and yosh<=18:
  input("Nechanchi sinfda o'qiysiz: ")
elif yosh<=0 and yosh>=101:
  print("Notog'ri yosh kiritdingiz! ")
else:
  print()

"""5-mashq"""
davlatlar = {
    "o'zbekiston":'toshkent',
    'aqsh':'washington d.c.',
    'rossiya':'moskva',
    'tojikiston':'dushanbe',
    "qirg'iziston":'bishkek',
    'qozog\'iston':'nursulton',
    'malayziya':'kuala-lumpur',
    'singapur':'sungapur',
    'italiya':'rim'}

savol = input("Davlat yoki davlatning poytaxtini kiriting: ")
if savol in davlatlar:
      print(f"{savol.capitalize} davlatining poytaxti {davlatlar[savol].capitalize()} shahri")
      
elif savol in davlatlar.values():
      for davlat, poytaxt in davlatlar.items():
        if savol.lower() == poytaxt.lower():
           print(f"{savol.capitalize()} shahri {davlat.capitalize()} ning poytaxti")
        else:
          print("Bizda bunday ma'lumot yo'q")

  




