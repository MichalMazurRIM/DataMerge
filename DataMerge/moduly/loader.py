import os
import pandas as pd

def load_files(input_dir):
    full_path = os.path.abspath(input_dir)
    print("Szukanie plików w:", full_path)

    if not os.path.exists(input_dir):
        print("Folder nie istnieje!")
        return []

    files = [f for f in os.listdir(input_dir) if f.endswith((".csv", ".xlsx"))]
    files = [os.path.join(input_dir, f) for f in files]
    return files

def load_and_merge(file_list):
    dataframes = []

    for file in file_list:
        name = os.path.basename(file)
        print("Wczytuję:", name)
        try:
            if file.endswith(".csv"):
                df = pd.read_csv(file)
            else:
                df = pd.read_excel(file)
        except Exception as e:
            print(f"Błąd wczytania {name}: {e}")
            continue

        df["_source_file"] = name
        dataframes.append(df)

    if not dataframes:
        return pd.DataFrame()

    # Normalizacja kolumn
    all_columns = set()
    for df in dataframes:
        all_columns.update(df.columns.tolist())
    all_columns = list(all_columns)

    normalized = []
    for df in dataframes:
        for col in all_columns:
            if col not in df.columns:
                df[col] = pd.NA
        df = df[all_columns]
        normalized.append(df)

    merged_df = pd.concat(normalized, ignore_index=True, sort=False)
    return merged_df
