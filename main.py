#aplikasi pemantauan proses download
import tkinter as tk
import time
# from threading import Thread

# Kode menggunakan Timer
def download_step(step =0):
    if step <= 10:
        progress_var.set(step * 10)
        label_percent.config(text=f"{step * 10}%")
        label_status.config(text="Mengunduh ... ")
        root.after(1000, download_step, step + 1)
    else:
        label_status.config(text="Download Selesai")

def start_download():
    download_step()

# Thread memungkinkan aplikasi menjalankan proses secara bersamaan, sehingga antarmuka GUI lebih responsif
# def start_download():
#     Thread(target=download_process).start()

root = tk.Tk()

root.title("Download Monitor")
root.geometry("400x300")

label_status = tk.Label(root, text="Menunggu", font=("Helvetica", 14))
label_status.pack(pady=10)

progress_var = tk.IntVar()
progress_bar = tk.Scale(root, from_=0, to=100, orient='horizontal', variable=progress_var, length=300)
progress_bar.pack(pady=20)

label_percent = tk.Label(root, text="0%", font=("Helvetica", 12))
label_percent.pack()

start_button = tk.Button(root, text="Download", command=start_download)
start_button.pack()

root.mainloop()