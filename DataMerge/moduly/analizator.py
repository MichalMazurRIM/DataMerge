import pandas as pd
import os

def analizuj_dane(df, output_dir):
    raport_path = os.path.join(output_dir, "raport_analiza.txt")

    with open(raport_path, "w", encoding="utf-8") as f:
        f.write("PODSUMOWANIE DANYCH\n")
        f.write("====================\n\n")
        f.write(f"Liczba wierszy: {len(df)}\n")
        f.write(f"Liczba kolumn: {len(df.columns)}\n\n")

        f.write("Kolumny:\n")
        for col in df.columns:
            f.write(f" - {col}\n")

        f.write("\nBraki danych (NA) w kolumnach:\n")
        for col, val in df.isna().sum().items():
            f.write(f" - {col}: {val}\n")

        # Statystyki liczbowe
        num_cols = df.select_dtypes(include=["int64", "float64"])
        if not num_cols.empty:
            f.write("\nStatystyki liczbowe:\n")
            f.write(str(num_cols.describe().T))
            f.write("\n")

        # Najczęstsze wartości kolumn tekstowych
        text_cols = df.select_dtypes(include=["object"])
        if not text_cols.empty:
            f.write("\nNajczęstsze wartości w kolumnach tekstowych:\n")
            for col in text_cols:
                counts = text_cols[col].value_counts().head(5)
                f.write(f"\n{col}:\n{counts.to_string()}\n")

    print("Zapisano raport analizy:", raport_path)
