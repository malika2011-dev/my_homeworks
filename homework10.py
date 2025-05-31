"""1-mashq"""
def yil(ism, yosh, hozir = 2025):
    """Tuf'ilgan yilni topib beruvchi dastur"""
    return f"{ism.title()} siz {hozir-yosh} - yilda tug'ilgan ekansiz"

"""2-mashq"""
def daraja2(son):
    """Kadrati va kubini topib beruvchu dastur"""
    return f"kvadrati {son**2} kubi {son**3}" 

"""3-mashq"""
def juft_t(son):
    """Juft yoki toq son ekanligini topib beruvchu dastur"""

    if son%2 == 0:
        son= "Juft"
    else:
        son = "Toq"
    return son

"""4-mashq"""
def taqqosla(a,b):
    """Ikki sondan qaysi biri katta ekanligini topib beruvchu dastur"""
    if a>b:
        x = f"{a} katta"
    elif b>a:
        x = f"{b} katta"
    elif a ==b :
        x = f"Sonlar teng"
    return x

"""5-mashq"""

def qoldiq(son2):
   pass 

"""6-mashq"""
def oila(ism, yosh, kasb, **malumotlar):
    """Oila a'zolarimizning ma'lumotini konsolga chiqaruvchi dastur"""
    return f"Ismi {ism.title()}, yoshi {yosh} da {kasb.title()} bo'lib ishlaydi, {malumotlar}"


"""7-mashq"""


"""13"""
"""1-mashq"""
malumot = {}

def malumotni_jamla(ism, familya, t_yil, t_joy, t_raqam, e_raqam = "Nomalum"):
    malumot["ism"] = ism
    malumot["familya"] = familya
    malumot["t_yil"] = t_yil
    malumot["t_joy"] = t_joy
    malumot["t_raqam"] = t_raqam
    malumot["e_raqam"] = e_raqam

    return malumot

malika = malumotni_jamla("malika", "abdulahadova", "2011", "namangan", 56544545, 4343454)
print(malika)

"""2-mashq"""
def malumot_kirit():
    mijozlar = []
    while True:
        print("\n Quidagi ma'lumotlarni kiriting: ")
        ism = input("Ismni kriitng: ")
        familya = input("Familyani kiriting: ")
        t_yil = input("Tug'ilgan yilni kirting: ")
        t_joy = input("Shaharni kriting: ")
        t_raqam = input("Telefon raqamni kriitng: ")
        e_raqam = input("Email raqamni kriting: ")

        mijozlar.append(malumot(ism, familya, t_yil, t_joy, t_raqam, e_raqam))

        savol = input("Yana kiritishni hohlaysizmi (ha/yo'q): ")
        if savol != "ha":
            break
        return mijozlar
    
"""3-mashq"""
def katta(a,b,c):
    x = max(a,b,c)
    return x

"""4-mashq"""




    
