import json
import os
import app_ui

def load_config():
    if not os.path.exists("config.json"):
        print("Peringatan: File 'config.json' tidak ditemukan!")
        print("Silakan salin 'config.json.example' menjadi 'config.json' dan masukkan API Key kamu.")
        return None
    
    try:
        with open("config.json", "r") as file:
            return json.load(file)
    except Exception as e:
        print(f"Error membaca config.json: {e}")
        return None

def main():
    print("Membuka aplikasi cuaca GUI...")
    config = load_config()
    # Tetap jalankan GUI
    app_ui.run_gui()

if __name__ == "__main__":
    main()