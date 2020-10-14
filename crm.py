#!/usr/bin/python3
# -*- coding: utf-8 -*
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showwarning
from tkinter import messagebox
import sqlite3

# -------------------------------definicje--------------------------------

# czyszczenie pól w formularzu wyszukiwania


def wyczysc_pola():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)

# czyszczenie pól w formularzu dodawania nowego klienta


def wyczysc_pola_2():
    e5.delete(0, END)
    e6.delete(0, END)
    e7.delete(0, END)
    e8.delete(0, END)
    e9.delete(0, END)
    e10.delete(0, END)
    e11.delete(0, END)
    e12.delete(0, END)
    e13.delete(0, END)
    e14.delete(0, END)
    e15.delete(0, END)
    e16.delete(0, END)
# zapis danych do bazy


def zapisz_nowego_klienta():
    conn = sqlite3.connect('CRM.db')
    c = conn.cursor()
    c.execute("INSERT INTO ludzie VALUES(NULL, :imie, :nazwisko, :pesel, :nip, :ulica, :nr_ulicy, :nr_mieszkania, :miasto, :kod, :email, :telefon, :uwagi)",
              {
                  'imie': imieKlient.get(),
                  'nazwisko': nazwiskoKlient.get(),
                  'pesel': peselKlient.get(),
                  'nip': nipKlient.get(),
                  'ulica': ulicaKlient.get(),
                  'nr_ulicy': nrUlicyKlient.get(),
                  'nr_mieszkania': nrMieszkaniaKlient.get(),
                  'miasto': miastoKlient.get(),
                  'kod': kodKlient.get(),
                  'email': emailKlient.get(),
                  'telefon': telefonKlient.get(),
                  'uwagi': uwagiKlient.get()
              })
    conn.commit()
    conn.close()
    messagebox.showinfo("Informacja", "Nowy klient wpisany\n do bazy")
    e5.delete(0, END)
    e6.delete(0, END)
    e7.delete(0, END)
    e8.delete(0, END)
    e9.delete(0, END)
    e10.delete(0, END)
    e11.delete(0, END)
    e12.delete(0, END)
    e13.delete(0, END)
    e14.delete(0, END)
    e15.delete(0, END)
    e16.delete(0, END)

# wyszukiwanie klienta w bazie


def wyszukaj_klienta():
    ramka3 = tk.LabelFrame(root, text="Wynik wyszukiwania", padx=10, pady=10)
    ramka3.pack(padx=30, side=RIGHT)
    x_imie = szuk_imie.get()
    x_nazwisko = szuk_nazwisko.get()
    x_pesel = szuk_pesel.get()
    x_nip = szuk_nip.get()

    kolorKlienta = "green"
    fontKlienta = "Arial"
    czcionkaKlienta = 13
    p17 = tk.Label(ramka3, text="").grid(row=0, column=0, sticky=W)
    p17 = tk.Label(ramka3, text="Imie:", font=(
        fontKlienta, czcionkaKlienta), fg=kolorKlienta).grid(row=1, column=0, sticky=W)
    p18 = tk.Label(ramka3, text="Nazwisko:", font=(
        fontKlienta, czcionkaKlienta), fg=kolorKlienta).grid(row=2, column=0, sticky=W)
    p19 = tk.Label(ramka3, text="PESEL:", font=(
        fontKlienta, czcionkaKlienta), fg=kolorKlienta).grid(row=3, column=0, sticky=W)
    p20 = tk.Label(ramka3, text="NIP:", font=(
        fontKlienta, czcionkaKlienta), fg=kolorKlienta).grid(row=4, column=0, sticky=W)
    p21 = tk.Label(ramka3, text="Ulica:", font=(
        fontKlienta, czcionkaKlienta), fg=kolorKlienta).grid(row=5, column=0, sticky=W)
    p22 = tk.Label(ramka3, text="Nr ulicy:", font=(
        fontKlienta, czcionkaKlienta), fg=kolorKlienta).grid(row=6, column=0, sticky=W)
    p23 = tk.Label(ramka3, text="Nr mieszkania:", font=(
        fontKlienta, czcionkaKlienta), fg=kolorKlienta).grid(row=7, column=0, sticky=W)
    p24 = tk.Label(ramka3, text="Miasto:", font=(
        fontKlienta, czcionkaKlienta), fg=kolorKlienta).grid(row=8, column=0, sticky=W)
    p25 = tk.Label(ramka3, text="Kod:", font=(
        fontKlienta, czcionkaKlienta), fg=kolorKlienta).grid(row=9, column=0, sticky=W)
    p26 = tk.Label(ramka3, text="Email:", font=(
        fontKlienta, czcionkaKlienta), fg=kolorKlienta).grid(row=10, column=0, sticky=W)
    p27 = tk.Label(ramka3, text="Telefon:", font=(
        fontKlienta, czcionkaKlienta), fg=kolorKlienta).grid(row=11, column=0, sticky=W)
    p28 = tk.Label(ramka3, text="Uwagi:", font=(
        fontKlienta, czcionkaKlienta), fg=kolorKlienta).grid(row=12, column=0, sticky=W)

    conn = sqlite3.connect('CRM.db')
    c = conn.cursor()
    c.execute('SELECT * , oid FROM ludzie')
    records = c.fetchall()
    for r in records:
        imieK = str(r[1])
        nazwiskoK = str(r[2])
        peselK = str(r[3])
        nipK = str(r[4])
        ulicaK = str(r[5])

        if imieK == x_imie or nazwiskoK == x_nazwisko or peselK == x_pesel or nipKlient == x_nip:
            linia1 = tk.Label(ramka3, text=imieK, font=(
                "Arial", 13, "italic", "bold"), fg="black")
            linia2 = tk.Label(ramka3, text=nazwiskoK, font=(
                "Arial", 13, "italic"), fg="black")
            linia3 = tk.Label(ramka3, text=peselK, font=(
                "Arial", 13, "italic"), fg="black")
            linia4 = tk.Label(ramka3, text=nipK, font=(
                "Arial", 13, "italic"), fg="black")
            linia5 = tk.Label(ramka3, text=str(r[5]), font=(
                "Arial", 13, "italic"), fg="black")
            linia6 = tk.Label(ramka3, text=str(r[6]), font=(
                "Arial", 13, "italic"), fg="black")
            linia7 = tk.Label(ramka3, text=str(r[7]), font=(
                "Arial", 13, "italic"), fg="black")
            linia8 = tk.Label(ramka3, text=str(r[8]), font=(
                "Arial", 13, "italic"), fg="black")
            linia9 = tk.Label(ramka3, text=str(r[9]), font=(
                "Arial", 13, "italic"), fg="black")
            linia10 = tk.Label(ramka3, text=str(r[10]), font=(
                "Arial", 13, "italic"), fg="black")
            linia11 = tk.Label(ramka3, text=str(r[11]), font=(
                "Arial", 13, "italic"), fg="black")
            textbox = tk.Text(ramka3, width=50, height=10)
            textbox.grid(row=12, column=1)
            textbox.insert(tk.END, "\n\n")
            textbox.insert(tk.END, str(r[12]), ("p"))
            textbox.tag_add("p", "1.0", "1.0")
            textbox.tag_config("p", foreground=kolorKlienta)

            linia1.grid(row=1, column=1, sticky=W)
            linia2.grid(row=2, column=1, sticky=W)
            linia3.grid(row=3, column=1, sticky=W)
            linia4.grid(row=4, column=1, sticky=W)
            linia5.grid(row=5, column=1, sticky=W)
            linia6.grid(row=6, column=1, sticky=W)
            linia7.grid(row=7, column=1, sticky=W)
            linia8.grid(row=8, column=1, sticky=W)
            linia9.grid(row=9, column=1, sticky=W)
            linia10.grid(row=10, column=1, sticky=W)
            linia11.grid(row=11, column=1, sticky=W)
        else:
            tk.Label(ramka3, text="Brak rekordu!!!", font=(
                "Arial", 13), fg="red", bg="black").grid(row=0, column=0)

    tk.Button(ramka3, text="wyczysc", command=ramka3.destroy).grid(
        row=13, column=1)

    conn.close()


# -------------------------------głowny program------------------------------
root = tk.Tk()
root.geometry("1200x700")
root.title("Mini Baza CRM")
# Tworzenie bazy i tabeli jesli nie istnieje
conn = sqlite3.connect('CRM.db')
c = conn.cursor()
c.execute(
    """CREATE TABLE IF NOT EXISTS ludzie(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        imie text NOT NULL,
        nazwisko text NOT NULL,
        pesel text NOT NULL,
        nip text NOT NULL,
        ulica text NOT NULL,
        nr_ulicy text NOT NULL,
        nr_mieszkania text NOT NULL,
        miasto text NOT NULL,
        kod text NOT NULL,
        email text NOT NULL,
        telefon text NOT NULL,
        uwagi text NOT NULL);""")
conn.commit()
conn.close()

# kreator ramek *** dodaj klienta *** szukaj klienta
ramka1 = tk.LabelFrame(root, text="Odszukaj klienta", padx=10, pady=10)
ramka1.pack(padx=10, pady=10, side=TOP)

ramka2 = tk.LabelFrame(root, text="Dodaj klienta", padx=10, pady=10)
ramka2.pack(padx=30, side=LEFT)


# formularz wyszukiwania klienta
szuk_imie = StringVar()
szuk_nazwisko = StringVar()
szuk_pesel = StringVar()
szuk_nip = StringVar()
p1 = tk.Label(ramka1, text="Podaj imie:", font=("Arial", 13))
p1.grid(row=0, column=0)
e1 = tk.Entry(ramka1, textvariable=szuk_imie)
e1.grid(row=0, column=1)

p2 = tk.Label(ramka1, text="Podaj nazwisko:",
              font=("Arial", 13)).grid(row=0, column=2)
e2 = tk.Entry(ramka1, textvariable=szuk_nazwisko)
e2.grid(row=0, column=3)

p3 = tk.Label(ramka1, text="Podaj PESEL:", font=(
    "Arial", 13)).grid(row=0, column=4)
e3 = tk.Entry(ramka1, textvariable=szuk_pesel)
e3.grid(row=0, column=5)

p4 = tk.Label(ramka1, text="Podaj NIP:", font=(
    "Arial", 13)).grid(row=0, column=6)
e4 = tk.Entry(ramka1, textvariable=szuk_nip)
e4.grid(row=0, column=7)

p5 = tk.Label(ramka1, text="").grid(row=1, column=0)

b1 = tk.Button(ramka1, text="Szukaj klienta", fg="red",
               command=wyszukaj_klienta).grid(row=2, column=3)
b2 = tk.Button(ramka1, text="Wyczyść pola", fg="green",
               command=wyczysc_pola).grid(row=2, column=4)

# formularz dodawania nowego klienta
rozmiarCzcionki = 13
kolorCzcionki = "blue"
p6 = tk.Label(ramka2, text="Imie:", font=("Arial", rozmiarCzcionki),
              fg=kolorCzcionki).grid(row=0, column=0, sticky=W)
p7 = tk.Label(ramka2, text="Nazwisko:", font=(
    "Arial", rozmiarCzcionki), fg=kolorCzcionki).grid(row=1, column=0, sticky=W)
p8 = tk.Label(ramka2, text="PESEL:", font=("Arial", rozmiarCzcionki),
              fg=kolorCzcionki).grid(row=2, column=0, sticky=W)
p9 = tk.Label(ramka2, text="NIP:", font=("Arial", rozmiarCzcionki),
              fg=kolorCzcionki).grid(row=3, column=0, sticky=W)
p10 = tk.Label(ramka2, text="Nazwa ulicy:", font=(
    "Arial", rozmiarCzcionki), fg=kolorCzcionki).grid(row=4, column=0, sticky=W)
p11 = tk.Label(ramka2, text="Nr ulicy:", font=(
    "Arial", rozmiarCzcionki), fg=kolorCzcionki).grid(row=5, column=0, sticky=W)
p12 = tk.Label(ramka2, text="Nr mieszkania:", font=(
    "Arial", rozmiarCzcionki), fg=kolorCzcionki).grid(row=6, column=0, sticky=W)
p13 = tk.Label(ramka2, text="Miasto:", font=(
    "Arial", rozmiarCzcionki), fg=kolorCzcionki).grid(row=7, column=0, sticky=W)
p14 = tk.Label(ramka2, text="Kod:", font=("Arial", rozmiarCzcionki),
               fg=kolorCzcionki).grid(row=8, column=0, sticky=W)
p15 = tk.Label(ramka2, text="Email:", font=("Arial", rozmiarCzcionki),
               fg=kolorCzcionki).grid(row=9, column=0, sticky=W)
p16 = tk.Label(ramka2, text="Nr telefonu:", font=(
    "Arial", rozmiarCzcionki), fg=kolorCzcionki).grid(row=10, column=0, sticky=W)
p17 = tk.Label(ramka2, text="Uwagi:", font=("Arial", rozmiarCzcionki),
               fg=kolorCzcionki).grid(row=11, column=0, sticky=W)

imieKlient = StringVar()
nazwiskoKlient = StringVar()
peselKlient = StringVar()
nipKlient = StringVar()
ulicaKlient = StringVar()
nrUlicyKlient = StringVar()
nrMieszkaniaKlient = StringVar()
miastoKlient = StringVar()
kodKlient = StringVar()
emailKlient = StringVar()
telefonKlient = StringVar()
uwagiKlient = StringVar()

e5 = tk.Entry(ramka2, textvariable=imieKlient, width=30)
e6 = tk.Entry(ramka2, textvariable=nazwiskoKlient, width=30)
e7 = tk.Entry(ramka2, textvariable=peselKlient, width=30)
e8 = tk.Entry(ramka2, textvariable=nipKlient, width=30)
e9 = tk.Entry(ramka2, textvariable=ulicaKlient, width=30)
e10 = tk.Entry(ramka2, textvariable=nrUlicyKlient, width=10)
e11 = tk.Entry(ramka2, textvariable=nrMieszkaniaKlient, width=10)
e12 = tk.Entry(ramka2, textvariable=miastoKlient, width=30)
e13 = tk.Entry(ramka2, textvariable=kodKlient, width=10)
e14 = tk.Entry(ramka2, textvariable=emailKlient, width=30)
e15 = tk.Entry(ramka2, textvariable=telefonKlient, width=30)
e16 = tk.Entry(ramka2, textvariable=uwagiKlient, width=30)

e5.grid(row=0, column=1, pady=5)
e6.grid(row=1, column=1, pady=5)
e7.grid(row=2, column=1, pady=5)
e8.grid(row=3, column=1, pady=5)
e9.grid(row=4, column=1, pady=5)
e10.grid(row=5, column=1, pady=5, sticky=W)
e11.grid(row=6, column=1, pady=5, sticky=W)
e12.grid(row=7, column=1, pady=5)
e13.grid(row=8, column=1, pady=5, sticky=W)
e14.grid(row=9, column=1, pady=5)
e15.grid(row=10, column=1, pady=5)
e16.grid(row=11, column=1, pady=5)

b3 = tk.Button(ramka2, text="Zapisz do bazy", fg="red",
               command=zapisz_nowego_klienta).grid(row=13, column=0)
b4 = tk.Button(ramka2, text="Wyczyść pola", fg="green",
               command=wyczysc_pola_2).grid(row=13, column=1)

root.mainloop()
