# DataMerge

## Opis projektu
**DataMerge** to narzędzie do automatycznego łączenia i raportowania danych z plików CSV i XLSX.  
Program umożliwia:
- Wczytanie wielu plików CSV i XLSX z wybranego folderu
- Normalizację kolumn w plikach (uzupełnianie brakujących kolumn)
- Usuwanie duplikatów danych
- Tworzenie zbiorczego raportu w formacie CSV i XLSX
- Obsługę poprzez prosty interfejs GUI (Python tkinter)
- Generowanie gotowego pliku EXE do uruchomienia na Windows

---

## Funkcje
1. **Automatyczne wczytywanie plików** – CSV i XLSX  
2. **Normalizacja danych** – brakujące kolumny są uzupełniane  
3. **Usuwanie duplikatów** – tylko unikalne wiersze trafiają do raportu  
4. **Zapis raportów** – w formacie CSV i XLSX  
5. **Gotowe do uruchomienia EXE** – nie wymaga instalacji Pythona  

---

## Screenshot GUI
![GUI](assets/gui_screenshot.png)  

---

## Wymagania
- Python 3.10+  
- Biblioteki Python:
  ```bash
  pip install pandas openpyxl
