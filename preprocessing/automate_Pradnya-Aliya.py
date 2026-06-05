import os
import pandas as pd

def preprocess_data(input_path, output_path):
    print("Memulai otomatisasi preprocessing data...")
    
    # 1. Muat data mentah
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Data mentah tidak ditemukan di {input_path}")
    df = pd.read_csv(input_path)
    
    # 2. Proses Preprocessing (Sesuaikan dengan eksperimen .ipynb kamu, contoh:)
    # Mengapus duplikasi jika ada
    df = df.drop_duplicates()
    
    # Memastikan tidak ada missing value pada kolom krusial
    df = df.dropna()
    
    # 3. Simpan data yang siap dilatih
    df.to_csv(output_path, index=False)
    print(f"Preprocessing selesai! Data siap dilatih disimpan di: {output_path}")

if __name__ == "__main__":
    # Path disesuaikan dengan struktur folder repo Eksperimen_SML
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    raw_data = os.path.join(base_dir, "Crop_recommendation.csv")
    clean_data = os.path.join(base_dir, "preprocessing", "crop_preprocessing.csv")
    
    preprocess_data(raw_data, clean_data)