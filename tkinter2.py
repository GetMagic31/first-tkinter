import tkinter as tk
#Event Funktionen
def button1_click():
    Fenster2 = tk.Tk()
    Anzeige2 = tk.Label(Fenster2, text="Das freut mich!")
    Anzeige2.pack()
def button2_click():
    Fenster3 = tk.Tk()
    Anzeige3 = tk.Label(Fenster3, text="Das tut mir leid!")
    Anzeige3.pack()

#Main Programm
Fenster = tk.Tk()
Anzeige = tk.Label(Fenster, text="Hallo, wie geht es dir?")
Anzeige.pack()
Button1 = tk.Button(Fenster, text="Gut!", command=button1_click)
Button2 = tk.Button(Fenster, text="Schlecht!", command=button2_click)
Button1.pack()
Button2.pack()
Fenster.mainloop()