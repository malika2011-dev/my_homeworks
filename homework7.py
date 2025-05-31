from datetime import date, datetime

bugun = date.today()
oy = int(input("Tug'ilgan oyingizni kiriritng: "))
kun = int(input("Tug'ilgan kuniningizni kiriting: "))

sana = date(bugun.year, oy, kun)
if bugun > sana:
    sana = date(bugun.year+1, oy, kun)
    print(f"Sizning tug'ilgan kuningiznga yana {(sana - bugun).days} kun qoldi")
elif sana > bugun:
    sana = date(bugun.year, oy, kun)
    print(f"Sizning tug'ilgan kuningiznga yana {(sana - bugun).days} kun qoldi")
