import tkinter as tk
from tkinter import ttk, messagebox
import os
import gui_settings

# Funcții pentru gestionarea datelor
def incarca_date():
    if os.path.exists("depozit.txt"):
        with open("depozit.txt", "r") as fisier:
            date = fisier.readlines()
        return [linie.strip().split("|") for linie in date if linie.strip() and not linie.startswith("#")]
    return []

def salveaza_date(date):
    with open("depozit.txt", "w") as fisier:
        fisier.write("# Articole din Depozit\n\n")
        for articol in date:
            fisier.write(" | ".join(articol) + "\n")

def adauga_articol():
    id_articol = entry_id.get()
    nume_articol = entry_nume.get()
    sectiune_articol = sectiune_var.get()
    if id_articol and nume_articol:
        articole.append([id_articol, nume_articol, sectiune_articol])
        salveaza_date(articole)
        actualizeaza_treeview()
        entry_id.delete(0, tk.END)
        entry_nume.delete(0, tk.END)
    else:
        messagebox.showerror("Eroare", "ID-ul și Numele sunt obligatorii")

def sterge_articol():
    try:
        item_selectat = treeview.selection()[0]
        articol_de_sters = treeview.item(item_selectat)['values']
        id_articol = articol_de_sters[0]
        global articole
        articole = [articol for articol in articole if articol[0] != id_articol]
        salveaza_date(articole)
        treeview.delete(item_selectat)
    except IndexError:
        messagebox.showerror("Eroare", "Selectează un articol din lista pentru a-l șterge")

def actualizeaza_treeview():
    for row in treeview.get_children():
        treeview.delete(row)
    for articol in articole:
        treeview.insert('', 'end', values=articol)

def cauta_articole():
    cauta_termen = entry_cauta.get().lower()
    articole_filtrate = []
    for articol in articole:
        if len(articol) > 1:
            if cauta_termen in articol[0].lower() or cauta_termen in articol[1].lower():
                articole_filtrate.append(articol)
    for row in treeview.get_children():
        treeview.delete(row)
    for articol in articole_filtrate:
        treeview.insert('', 'end', values=articol)

def filtreaza_dupa_sectiune():
    sectiune_selectata = sectiune_var.get()
    if not sectiune_selectata:
        messagebox.showerror("Eroare", "Te rog selectează o secțiune din listă!")
        return
    articole_filtrate = [articol for articol in articole if articol[2].strip().lower() == sectiune_selectata.lower()]
    for row in treeview.get_children():
        treeview.delete(row)
    if not articole_filtrate:
        messagebox.showinfo("Informație", f"Nu există articole în secțiunea '{sectiune_selectata}'")
    for articol in articole_filtrate:
        treeview.insert('', 'end', values=articol)

# Funcția de validare pentru ID (permite doar cifre)
def valideaza_id(text):
    return text.isdigit() or text == ""

# Interfața principală
root = tk.Tk()
root.title("Gestionare Depozit")
root.geometry("650x600")
root.configure(bg=gui_settings.BACKGROUND_COLOR)

# Stilizare
style = ttk.Style()
style.configure("Treeview", background=gui_settings.TREEVIEW_BG_COLOR, foreground=gui_settings.TREEVIEW_FG_COLOR, rowheight=gui_settings.TREEVIEW_ROW_HEIGHT, fieldbackground=gui_settings.TREEVIEW_BG_COLOR)
style.configure("Treeview.Heading", background="white", foreground="black", font=gui_settings.LABEL_FONT)
style.map('Treeview', background=[('selected', gui_settings.TREEVIEW_SELECTION_COLOR)], foreground=[('selected', 'black')])

# Etichete și câmpuri de input
label_id = tk.Label(root, text="ID Articol:", bg=gui_settings.BACKGROUND_COLOR, font=gui_settings.LABEL_FONT, fg="black")
label_id.grid(row=0, column=0, padx=10, pady=10, sticky="w")

label_nume = tk.Label(root, text="Nume Articol:", bg=gui_settings.BACKGROUND_COLOR, font=gui_settings.LABEL_FONT, fg="black")
label_nume.grid(row=1, column=0, padx=10, pady=10, sticky="w")

label_sectiune = tk.Label(root, text="Secțiune:", bg=gui_settings.BACKGROUND_COLOR, font=gui_settings.LABEL_FONT, fg="black")
label_sectiune.grid(row=2, column=0, padx=10, pady=10, sticky="w")

validare_id = root.register(valideaza_id)
entry_id = tk.Entry(root, width=20, font=gui_settings.ENTRY_FONT, bg=gui_settings.ENTRY_BACKGROUND_COLOR, validate="key", validatecommand=(validare_id, "%P"))
entry_id.grid(row=0, column=1, padx=10, pady=10)

entry_nume = tk.Entry(root, width=20, font=gui_settings.ENTRY_FONT, bg=gui_settings.ENTRY_BACKGROUND_COLOR)
entry_nume.grid(row=1, column=1, padx=10, pady=10)

sectiune_var = tk.StringVar()
sectiune_combobox = ttk.Combobox(
    root,
    textvariable=sectiune_var,
    values=["Unelte", "Electrocasnice", "Materiale electrice", "Instalatii sanitare",
            "Bucatarie", "Macarale", "Materiale de constructii"],
    height=10
)
sectiune_combobox.grid(row=2, column=1, padx=10, pady=10)

# Butoane
buton_adauga = tk.Button(root, text="Adaugă Articol", command=adauga_articol, font=gui_settings.BUTTON_FONT, bg=gui_settings.BUTTON_BG_COLOR, fg=gui_settings.BUTTON_FG_COLOR)
buton_adauga.grid(row=3, column=0, padx=10, pady=10)

buton_sterge = tk.Button(root, text="Șterge Articol", command=sterge_articol, font=gui_settings.BUTTON_FONT, bg=gui_settings.BUTTON_BG_COLOR, fg=gui_settings.BUTTON_FG_COLOR)
buton_sterge.grid(row=3, column=1, padx=10, pady=10)

label_cauta = tk.Label(root, text="Caută Articol:", bg=gui_settings.BACKGROUND_COLOR, font=gui_settings.LABEL_FONT, fg="black")
label_cauta.grid(row=4, column=0, padx=10, pady=10, sticky="w")

entry_cauta = tk.Entry(root, width=20, font=gui_settings.ENTRY_FONT, bg=gui_settings.ENTRY_BACKGROUND_COLOR)
entry_cauta.grid(row=4, column=1, padx=10, pady=10)

buton_cauta = tk.Button(root, text="Caută", command=cauta_articole, font=gui_settings.BUTTON_FONT, bg=gui_settings.BUTTON_BG_COLOR, fg=gui_settings.BUTTON_FG_COLOR)
buton_cauta.grid(row=4, column=2, padx=10, pady=10)

# Frame pentru Treeview și Scrollbar
frame_treeview = tk.Frame(root)
frame_treeview.grid(row=5, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

treeview = ttk.Treeview(frame_treeview, columns=("ID", "Nume Articol", "Secțiune"), show="headings", style="Treeview")
treeview.pack(side="left", fill="both", expand=True)

scrollbar = ttk.Scrollbar(frame_treeview, orient="vertical", command=treeview.yview)
scrollbar.pack(side="right", fill="y")

treeview.configure(yscrollcommand=scrollbar.set)

treeview.heading("ID", text="ID Articol")
treeview.heading("Nume Articol", text="Nume Articol")
treeview.heading("Secțiune", text="Secțiune")

articole = incarca_date()
actualizeaza_treeview()

buton_filtreaza = tk.Button(root, text="Filtrează", command=filtreaza_dupa_sectiune, bg=gui_settings.FILTER_BUTTON_COLOR, fg=gui_settings.BUTTON_TEXT_COLOR, font=gui_settings.BUTTON_FONT)
buton_filtreaza.grid(row=3, column=2, padx=10, pady=10)

root.mainloop()
