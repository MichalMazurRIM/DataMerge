import os
import tkinter as tk
from tkinter import filedialog, messagebox
from moduly.loader import load_files, load_and_merge
from moduly.analizator import analizuj_dane
from moduly.wykresy import generuj_wykresy

def start_analysis():
    input_dir = filedialog.askdirectory(title="Wybierz folder z plikami CSV/XLSX")
    if not input_dir:
        return

    output_dir = os.path.join(input_dir, "wyniki")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    files = load_files(input_dir)
    if not files:
        messagebox.showinfo("Info", "Nie znaleziono plików CSV/XLSX w folderze.")
        return

    df = load_and_merge(files)
    if df.empty:
        messagebox.showinfo("Info", "Brak danych po połączeniu. Koniec.")
        return

    df = df.drop_duplicates(ignore_index=True)

    # Zapis zbiorczy Excel
    excel_path = os.path.join(output_dir, "raport_zbiorczy.xlsx")
    df.to_excel(excel_path, index=False)

    # Analiza i wykresy
    analizuj_dane(df, output_dir)
    generuj_wykresy(df, output_dir)

    messagebox.showinfo("Gotowe", f"Analiza zakończona!\nWyniki w: {output_dir}")

# --- GUI ---
root = tk.Tk()
root.title("Mini-Analiza CSV/XLSX")
root.geometry("400x150")

label = tk.Label(root, text="Kliknij przycisk, aby wybrać folder z plikami:", wraplength=350)
label.pack(pady=10)

btn = tk.Button(root, text="Wybierz folder i uruchom analizę", command=start_analysis)
btn.pack(pady=20)

root.mainloop()
