class Inson(): # Super class
    """ Inson haqidagi klass """

    def __init__(self, ism, familiya, t_yil, manzil, passport):
        """  """
        self.ism = ism
        self.familiya = familiya
        self.t_yil = t_yil
        self.manzil = manzil
        self.passport =passport

    def __str__(self):
        """  """
        return f"{self.ism} {self.familiya}"
    
    def get_info(self):
        """ Inson haqidagi ma'lumotlarni beruvchi funksiya """
        from datetime import date
        info = f"Ism: {self.ism} \nFamiliya: {self.familiya} \nYosh: {date.today().year-self.t_yil} \nTug'ilgan yil {self.t_yil}-yil  \
            \nManzil: {self.manzil}"
        return info
        
    def get_age(self):
        from datetime import date
        """ Insonning yoshini topuvchi funksiya """
        
        return date.today().year-self.t_yil
             
person1 = Inson("Temur", "Amir", 1336, "Kesh, Samarqand", "AA0000001")

print(person1.get_info())
print(person1.get_age())


class Shifokor(Inson): # Voris klass
    """  """

    def __init__(self, ism, familiya, t_yil, manzil, passport, turi, daraja, ish_haqi):
        super().__init__(ism, familiya, t_yil, manzil, passport)
        self.turi = turi
        self.daraja = daraja
        self.ish_haqi = ish_haqi
           
    def get_info(self):
        """ Inson haqidagi ma'lumotlarni beruvchi funksiya """
        from datetime import date
        info = f"Ism: {self.ism} \nFamiliya: {self.familiya} \nYosh: {date.today().year-self.t_yil} \nTug'ilgan yil {self.t_yil}-yil  \
            \nManzil: {self.manzil} \nKasbi: {self.turi} \nDarajasi: {self.daraja} \nIsh haqi: {self.ish_haqi} so'm"
        return info
      
    def ishhaqini_bilish(self):
        return f"{self.ism} ning maoshi {self.ish_haqi} so'm"
    
    def ishhaqini_ozgartirish(self, yangi_maosh):
        
        self.ish_haqi = yangi_maosh
        return f"Maosh {yangi_maosh} so'm ga almashdi"
      
    def darajani_oshirish(self, yangi_darja):
        self.daraja = yangi_darja
        return f"Daraja {yangi_darja} ga almashdi"

        
malika = Shifokor("Malika", "Abdulahadova", 2011, "Yangi hayot", "A122324423", "Bolalar shifokori", "Hamshira", 3_000_000)  
print(malika)
print(malika.get_age())
print(malika.get_info())


class Teacher(Inson):
    """  """

    def __init__(self, ism, familiya, t_yil, manzil, passport, students:list, maosh:int, subject:str, sertificates:list, gender:str):
        super().__init__(ism, familiya, t_yil, manzil, passport)

        self.students = students
        self.maosh = maosh
        self.subject = subject
        self.sertificates = sertificates
        self.gender = gender

    def get_job_info(self):
         return f"O'qtuvchi: {self.ism} {self.familiya}({self.gender}) \nFani: {self.subject} \nSertifikatlari: {len(self.sertificates)} ta, {self.sertificates} \
             \nMaoshi: {self.maosh} so'm"

    def add_student(self, new_student):
         
        try:

            if type(new_student) != str:
                return f"Siz faqat matn kiritishingiz kerak !"
            
            elif new_student not in self.students:
                self.students.append(new_student)
                return f"{new_student} do'stlar ro'yhatiga qo'shildi !"
            
            else:
                return f"{new_student} ro'yhatda bor. Iltimos uni boshqa nom bilan kiriting !"
            
        except:
            return f"Funksiya ishlashida xatolik yuzaga keldi !"
    
    def delete_student(self, student):

        try:

            if type(student) != str:
                return f"Siz faqat matn kiritishingiz kerak !"
            
            elif student in self.students:
                self.students.remove(student)
                return f"{student} do'stlar ro'yhatidan o'chirildi !"
            
            else:
                return f"{student} ro'yhatda yo'q !"
            
        except:
            return f"Funksiya ishlashida xatolik yuzaga keldi !"
   
    def maoshni_ozgartirish(self, yangi_maosh):
         
        self.maosh = yangi_maosh
        return f"Maosh {yangi_maosh} so'm ga almashdi"
    
    def add_serificate(self, new_sertificate_name):

        try:

            if type(new_sertificate_name) != str:
                return f"Siz faqat matn kiritishingiz kerak !"
            
            elif new_sertificate_name not in self.sertificates:

                self.sertificates.append(new_sertificate_name)
                return f"{new_sertificate_name} do'stlar ro'yhatiga qo'shildi !"
            
            else:
                return f"{new_sertificate_name} ro'yhatda bor. Iltimos uni boshqa nom bilan kiriting !"
            
        except:
            return f"Funksiya ishlashida xatolik yuzaga keldi !"
    
    



muslima = Teacher("Muslima", "Makhmudova", 2002, "Yangi Namangan tumani", "AS4568877", ['Nigora', 'Masrura', 'Kumushbegim', 'Nodira'], 8_500_000, 'Ingliz tili', ['IELTS 8', 'CEFR C1'], 'Female')


print(muslima)
print(muslima.get_info())
print(muslima.get_job_info())
