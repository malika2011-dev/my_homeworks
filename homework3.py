"""Uyga vazifa"""

"""1-mashq"""

yosh = []

yosh.append(int(input("Otangizni yoshini kiriting: ")))
yosh.append(int(input("Onangizni yoshini kiriting: "))) 
yosh.append(int(input("Buvingizni yoshini kiriting: "))) 
yosh.append(int(input("Akangizni yoshini kiriting: ")))
yosh.append(int(input("Opangizni yoshini kiriting: "))) 

print(f"Eng katta yosh : {max(yosh)}")
print(f"Eng kichik yosh : {min(yosh)}")
print(f"Yoshlar yig'indisi : {sum(yosh)}")
print(f"Yoshlar o'sish tartibida : {sorted(yosh)}")


"""2-mashq"""
sonlar = []

sonlar.append(int(input("Biron bir son kiriting: ")))
sonlar.append(int(input("Yana biron bir son kiriting: ")))
sonlar.append(int(input("Yana biron bir son kiriting: ")))

print(f"Bu sonlarning eng kattasi {max(sonlar)}")
print(f"Bu sonlarning eng kichigi {min(sonlar)}")
print(f"Bu sonlarning yig'indisi {sum(sonlar)}")


"""3-mashq"""

sonlar2 = [45, -96, 0, 63.2, 1257, -6752.2, 42, 3, 542 ]

print(f"O'sish tartibi : {sorted(sonlar2)}")
print(f"Kamayish tartibi : {sorted(sonlar2, reverse = True)}")
sonlar2.reverse()
print(sonlar2)


"""4-mashq"""

print(list(range(201, 400, 2)))
print(list(range(302, 500, 2)))
print(list(range(25, 600, 25)))


"""5-mashq"""

ism = input("Ismingizni kiriting : ")
books = []
books.append(input("1-o'qigan kitobingizni nomini kiriting: "))
books.append(input("2-o'qigan kitobingizni nomini kiriting: "))
books.append(input("3-o'qigan kitobingizni nomini kiriting: "))
books.append(input("4-o'qigan kitobingizni nomini kiriting: "))
books.append(input("5-o'qigan kitobingizni nomini kiriting: "))
books.pop()
books.insert(2,"Mehrobdan chayon")
books.insert(3, "Jannati odamlar")
print(books)

"""6-mashq"""
fanlar =["Informatika", "Matematika"]
fanlar.append("Rus tili")
fanlar.insert(1,"Ingiliz tili")
fanlar.pop()
del fanlar[1]
fanlar.pop(0)
print(fanlar)

"""8-mashq"""
mashinalar = ["bmw", "mers", "onix", "trecker", "toyato", "monza", "malibu", "kaptiva", "gelik", "gentre"]

print(mashinalar)
print(f"{len(mashinalar)} ta mashina")
mashinalar.sort()
print(mashinalar)
mashinalar.sort(reverse = True)
print(mashinalar)

