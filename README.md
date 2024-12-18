Aplicația Depozit Manager este un program simplu, dezvoltat folosind biblioteca Tkinter în Python, care permite gestionarea articolelor într-un depozit. Include funcții precum adăugarea și ștergerea articolelor, căutarea acestora, filtrarea pe secțiuni și salvarea datelor într-un fișier text.

Funcționalități
Adăugarea unui articol: Permite utilizatorului să adauge un articol în depozit completând un formular cu ID-ul, numele și secțiunea articolului.

Ștergerea unui articol: Permite ștergerea unui articol selectat din listă.

Căutarea unui articol: Permite căutarea articolelor după ID sau nume.

Filtrarea articolelor pe secțiuni: Permite filtrarea articolelor după secțiunea selectată (de exemplu, Unelte, Electrocasnice, Materiale electrice, etc.).

Salvarea datelor: Articolele sunt salvate într-un fișier text numit depozit.txt, iar datele sunt încărcate de acolo la fiecare pornire a aplicației.

Fișiere Incluse
main.py: Codul principal al aplicației care gestionează interfața grafică și logica aplicației.

gui_settings.py: Un fișier pentru configurarea stilurilor și culorilor interfeței grafice.

depozit.txt: Un fișier text în care sunt stocate articolele adăugate în depozit.

Descrierea Fișierelor
main.py
Acesta este fișierul principal al aplicației și conține logica aplicației, precum și interfața grafică creată cu Tkinter. Funcțiile principale sunt:

incarca_date(): Încarcă articolele din fișierul depozit.txt la pornirea aplicației.

salveaza_date(): Salvează articolele în fișierul depozit.txt.

adauga_articol(): Permite adăugarea unui nou articol în depozit.

sterge_articol(): Permite ștergerea unui articol selectat.

cauta_articole(): Permite căutarea articolelor după ID sau nume.

filtreaza_dupa_sectiune(): Permite filtrarea articolelor după secțiune.

actualizeaza_treeview(): Actualizează afișarea listei de articole în interfața grafică.

gui_settings.py
Acest fișier conține setările pentru personalizarea aspectului grafic al aplicației. Acestea includ culorile și fonturile utilizate în aplicație, cum ar fi:

BACKGROUND_COLOR: Culoarea de fundal a aplicației.

TREEVIEW_BG_COLOR: Culoarea de fundal a listei de articole.

TREEVIEW_FG_COLOR: Culoarea textului în lista de articole.

BUTTON_BG_COLOR: Culoarea de fundal a butoanelor.

BUTTON_FG_COLOR: Culoarea textului butoanelor.

ENTRY_FONT
