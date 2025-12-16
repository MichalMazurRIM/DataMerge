import matplotlib.pyplot as plt
import os

def generuj_wykresy(df, output_dir):
    wykres_folder = os.path.join(output_dir, "wykresy")
    if not os.path.exists(wykres_folder):
        os.makedirs(wykres_folder)

    # Kolumny liczbowe → histogramy
    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns
    for col in numeric_cols:
        plt.figure()
        df[col].plot(kind="hist", bins=10, title=col)
        plt.xlabel(col)
        plt.ylabel("Ilość")
        plt.tight_layout()
        save_path = os.path.join(wykres_folder, f"{col}_hist.png")
        plt.savefig(save_path)
        plt.close()
        print("Wygenerowano wykres:", save_path)

    # Kolumny tekstowe → wykresy słupkowe top5 wartości
    text_cols = df.select_dtypes(include=["object"]).columns
    for col in text_cols:
        counts = df[col].value_counts().head(10)
        if counts.empty:
            continue
        plt.figure()
        counts.plot(kind="bar", title=col)
        plt.xlabel("Wartość")
        plt.ylabel("Ilość")
        plt.tight_layout()
        save_path = os.path.join(wykres_folder, f"{col}_top.png")
        plt.savefig(save_path)
        plt.close()
        print("Wygenerowano wykres:", save_path)
