from tkinter import *
def tombol():
    label_saya = Label(layar, text="Ini label dari tombol")
    label_saya.grid(row=2, column=0)

def nim():
    label_saya = Label(layar, text="NIM Saya K3523005")
    label_saya.grid(row=4, column=0)

def nama():
    label_saya = Label(layar, text="Afif Nur Azam")
    label_saya.grid(row=6, column=0)

layar = Tk()

label1 = Label(layar, text="Halo Saya Afif Cihuy, Mahasiswa PTIK UNS")

button = Button(layar, text="Tombol", command=tombol)
button2 = Button(layar, text="NIM", command=nim)
button3 = Button(layar, text="Nama", command=nama)

label1.grid(row=0, column=0)

button.grid(row=1, column=0)
button2.grid(row=3, column=0)
button3.grid(row=5, column=0)

layar.mainloop()
