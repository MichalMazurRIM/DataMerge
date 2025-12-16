import os
from moduly.loader import load_files, load_and_merge
from moduly.analizator import analizuj_dane
from moduly.wykresy import generuj_wykresy

if __name__ == "__main__":
    print("Start analizy...")

    INPUT_DIR = "pliki_testowe"
    OUTPUT_DIR = "wyniki"

    # Tworzymy folder na wyniki
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    files = load_files(INPUT_DIR)
    print("Znalezione pliki:", len(files))

    if not files:
        print("Brak danych do połączenia. Koniec.")
        exit()

    # Łączenie plików i usuwanie duplikatów
    df = load_and_merge(files)

    if df.empty:
        print("Brak danych po połączeniu. Koniec.")
        exit()

    df = df.drop_duplicates(ignore_index=True)
    print("Usunięto duplikaty. Liczba wierszy po deduplikacji:", len(df))

    # Zapis do Excel
    excel_path = os.path.join(OUTPUT_DIR, "raport_zbiorczy.xlsx")
    df.to_excel(excel_path, index=False)
    print("Zapisano raport zbiorczy:", excel_path)

    # Analiza danych
    analizuj_dane(df, OUTPUT_DIR)

    # Wykresy
    generuj_wykresy(df, OUTPUT_DIR)

    print("\nGotowe. Wszystkie wyniki w folderze:", OUTPUT_DIR)
