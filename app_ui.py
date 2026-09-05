import tkinter as tk
from tkinter import messagebox

def run_gui():
    def get_weather():
        city = city_entry.get().strip()
        if not city:
            messagebox.showwarning("Peringatan", "Masukkan nama kota terlebih dahulu!")
            return
        
        result_label.config(
            text=f"=== PREDIKSI CUACA GEMINI AI ===\n\n"
                 f"Kota: {city}\n"
                 f"Kondisi: Cerah Berawan (31°C)\n"
                 f"Saran: Gunakan pakaian ringan & bawa air minum!"
        )

    app = tk.Tk()
    app.title("Gemini Weather App - SSD1030")
    app.geometry("400x350")
    app.configure(bg="#1e1e2e")

    title_label = tk.Label(app, text="Aplikasi Cuaca Gemini", font=("Arial", 16, "bold"), fg="#cdd6f4", bg="#1e1e2e")
    title_label.pack(pady=15)

    city_entry = tk.Entry(app, font=("Arial", 12), width=25, justify="center")
    city_entry.insert(0, "Jakarta")
    city_entry.pack(pady=10)

    search_btn = tk.Button(app, text="Cek Cuaca", command=get_weather, bg="#89b4fa", fg="#11111b", font=("Arial", 11, "bold"), padx=10, pady=5)
    search_btn.pack(pady=10)

    result_label = tk.Label(app, text="", font=("Arial", 10), fg="#a6e3a1", bg="#1e1e2e", justify="left")
    result_label.pack(pady=15)

    app.mainloop()

if __name__ == "__main__":
    run_gui()