import tkinter as tk
import h_funktionen as hf
#Fenster erstellen
main_win = tk.Tk()
main_win.title("Sternzeichen Programm")
main_win.config(width=650, height=500)
#texte und buttons erstellen( main seite)
text_one = tk.Label(main_win, text="Welches Sternzeichen hast du?")
wasserman_Button = tk.Button(main_win, text="Wassermann", command=hf.button_click_wassermann)
fisch_Button = tk.Button(main_win, text="Fisch", command=hf.button_click_fisch)
widder_Button = tk.Button(main_win, text="Widder", command=hf.button_click_widder)
#Events platzieren
text_one.place(x=225, y=50, width=200, height=10)
wasserman_Button.place(x=50, y=100, width=150, height=50)
fisch_Button.place(x=250, y=100, width=150, height=50)
widder_Button.place(x=450, y=100, width=150, height=50)
#Ausführung
main_win.mainloop()

