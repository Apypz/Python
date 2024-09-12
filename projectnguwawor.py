#ada library namanya tktinker, cara memanggilnya cukup mudah
from tkinter import * #bintang artinya semua
#di tktinker itu selalu melewati 2 proses, proses 1 membuat, proses 2 menammpilkan ke layar
layar = Tk() #tk disini adalah fungsi untuk menampilkan GUI (Graphic User Interface)
#kemudian di tktinker juga ada fungsi label untuk menempatkan sebuah objek, misal kita buat variabel label_saya
label_saya = Label(layar, text="Halo nama saya skibidi")

#pack disini untuk menempatkan label saya ke sebuah layar 

button = Button(layar, text="Yang mau panci gratis klik")


listbox = Listbox(layar)
listbox.insert(1, "Sigma")
listbox.insert(2, "Mewing")
listbox.insert(3, "Rizz")

button.pack()
label_saya.pack()
listbox.pack()
layar.mainloop()
#untuk menampilkan tktinker, jika temen2 familiar dengan arduino, maka mainloop ini mirio dengan looping yang ada di arduino