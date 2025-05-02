# Kehakaalu Arvutaja 🧮

See on lihtne Python programm, mis arvutab kasutajate kehamassiindeksi (KMI) sisestatud pikkuse ja kaalu põhjal. Programm töötleb tekstifaili, kus igal real on inimese kaal, ning annab igale kasutajale vastava KMI väärtuse ja klassifikatsiooni.

## 📦 Funktsionaalsus

- Arvutab kehamassiindeksi valemiga: `KMI = kaal / (pikkus ** 2)`
- Klassifitseerib tulemuse järgmiselt:
  - Alla 18.5 → **Alakaal**
  - Kuni 24.9 → **Normaalkaal**
  - Kuni 29.9 → **Ülekaal**
  - Üle 30 → **Rasvumine**
- Väljastab suurima KMI väärtuse

## ▶️ Kasutamine

1. Veendu, et Python 3 on paigaldatud
2. Käivita terminalis:

```bash
python kehakaalud.py
3.Sisesta:
Failinimi (tekstifail kaaludega)
Pikkus (meetrites, nt 1.75)

## 📘 Näide

Sisesta faili nimi: andmed.txt  
Sisesta pikkus: 1.75  
Kaal 55, KMI 17.96, Klass Alakaal  
Kaal 85, KMI 27.76, Klass Ülekaal  
Kaal 120, KMI 39.18, Klass Rasvumine  
Suurim KMI oli 39.18  

---

## 👩‍💻 Autor  
**Daria Andriyanovich**  
University of Tartu – Estonian and Finno-Ugric Studies + Digital Humanities


