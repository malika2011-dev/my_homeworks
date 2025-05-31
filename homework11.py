import time

parol = "aaa"
urinishlar = 3

while urinishlar > 0:  # Foydalanuvchidan parolni kiritishni so'rash uchun faqat bitta sikl
    vaqt = 30
    savol = input("Parolni kiriting: ")
    
    if savol != parol:
        urinishlar -= 1
        print(f"Sizda {urinishlar} ta urinish qoldi")
    else:
        print("Xush kelibsiz")
        break  # Parol to'g'ri bo'lsa, dastur tugaydi

    if urinishlar == 0:  # Agar urinishlar tugasa, 30 soniya kutib yana urinishni so'rash
        print("Siz 3 martadan ortiq harakat qildingiz.")
        print("30 soniyadan keyin kiritishingiz mumkin: ")
        
        while vaqt > 0:  # 30 soniya sanash
            print(f"{vaqt} soniya qoldi")
            vaqt -= 1
            time.sleep(1)  # 1 soniya kutadi
        
        # 30 soniya tugagandan keyin yangi urinishni boshlash
        print("Yana 3 marta urinish uchun davom eting!")
        urinishlar = 3  # Urinishlar sonini qayta tiklaymiz


"""chatgpt ni yordami bu time.slepp(1)"""
