import tkinter as tk
#Event Funktionen
def button1_click():
    Anzeige.config(text="Das freut mich!")
def button2_click():
    Anzeige.config(text="Das tut mir leid!")
#Main Programm
Fenster = tk.Tk()
Fenster.config(width=260, height=120)    #höhe und breite festlegen, worauf man danach die verschiedenen Komponenten einfach mit x und y darauf platzieren kann
Anzeige = tk.Label(Fenster, text="Hallo wie geht es dir?")
Anzeige.place(x=50, y=20, width=160, height=30)
Button1 = tk.Button(Fenster, text="Gut", command=button1_click)
Button2 = tk.Button(Fenster, text="Schlecht!", command=button2_click)
Button1.place(x=20, y=70, width=100, height=30)
Button2.place(x=140, y=70, width=100, height=30)
Fenster.mainloop()