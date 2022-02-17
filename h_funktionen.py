import tkinter as tk
#Event Funktionen
def button_click_wassermann():
    wassermann_win = tk.Tk()
    wassermann_win.title("Wassermann Info")
    wassermann_win.config(width=800, height=100)
    wassermann_text = tk.Label(wassermann_win, text="Der zwischen dem 21. Januar und 19. Februar geborene Wassermann ist ein individueller Charakter.\n " \
    "Sein Planet ist der Saturn und der Uranus und sein Element die Luft.\n Er ist originell und außergewöhnlich und man findet ihn so kein zweites Mal.")
    wassermann_text.place(x=50, y=10, width=700, height=80)
def button_click_fisch():
    fisch_win = tk.Tk()
    fisch_win.title("Fische Info")
    fisch_win.config(width=900, height=100)
    fisch_text = tk.Label(fisch_win, text="Der Fisch besteht aus einem wahren Meer der Gefühle. \n" \
    "Geboren zwischen dem 20. Februar und 20. März sind Fische typisch für die Jahreszeit ebenso aufblühend und warm wie der bevorstehende Frühling.\n " \
    "Ihr Planet ist der Neptun und ihr Element, wie sollte es anders sein, das Wasser.")
    fisch_text.place(x=50, y=10, width=800, height=80)
def button_click_widder():
    widder_win = tk.Tk()
    widder_win.title("Fische Info")
    widder_win.config(width=900, height=100)
    widder_text = tk.Label(widder_win, text="Ganz getreu dem Motto 'Hier bin ich' ist der Widder ein Kind des Frühlings.\n" \
    "Geboren zwischen dem 21. März und dem 20. April sorgen Sie für viel neue Energie in Ihrem Umfeld. \n" \
    "Aufbruchsstimmung und Impulsivität kennzeichnet nicht nur Ihren Geburtsmonat, sondern spiegelt sich auch ganz klar in Ihrem Sternbild wider. ")
    widder_text.place(x=50, y=10, width=800, height=80)

