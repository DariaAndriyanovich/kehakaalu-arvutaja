def kmi(kaal,pikkus):
    return round(kaal / (pikkus **2), 1)

def terviseklass(kmi_v):
    if kmi_v < 18.5:
        return "Alakaal"
    elif kmi_v <= 24.9:
        return "Normaalkaal"
    elif kmi_v <= 29.9:
        return "Ülekaal"
    else:
        return "Rasvumine"
    
faili_nimi = input("Sisesta faili nimi:")
pikkus = float(input("Sisesta pikkus:"))
    
kmi_väärtused = []

with open(faili_nimi, encoding="utf-8") as f:
    for rida in f:
        kaal= int(rida.strip())
        kmi_v= kmi(kaal,pikkus)
        klass = terviseklass(kmi_v)
        print(f"Kaal {kaal},KMI {kmi_v}, Klass {klass} ")
        kmi_väärtused.append(kmi_v)
        
        
suurim=max(kmi_väärtused)
print(f"Suurim KMI oli {suurim}")

