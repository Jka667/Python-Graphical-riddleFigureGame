import tkinter as tk
from tkinter import messagebox
import random

class JeuDevinette(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Jeu de Devinette de Nombres")
        self.geometry("500x300")

        self.nombre_magic = random.randint(0, 9999)

        self.label_rules = tk.Label(self, text="Bienvenue dans le jeu de devinette de nombres!\n\n"
                                               "Règles du jeu:\n"
                                               "1. Devinez le nombre mystère entre 0 et 9999.\n"
                                               "2. Utilisez la zone de saisie pour proposer votre nombre.\n"
                                               "3. Obtenez des indications si le nombre mystère est plus grand ou plus petit.\n"
                                               "4. Amusez-vous et trouvez le nombre mystère!")
        self.label_rules.pack(pady=10)

        self.label_decorative = tk.Label(self, text="****************")
        self.label_decorative.pack(pady=10)

        self.entry = tk.Entry(self, width=10)
        self.entry.pack(pady=10)

        self.button = tk.Button(self, text="Proposer", command=self.verifier_proposition)
        self.button.pack(pady=10)

    def verifier_proposition(self):
        try:
            proposition = int(self.entry.get())
            if 0 <= proposition <= 9999:
                if proposition < self.nombre_magic:
                    message = "Le nombre à deviner est plus grand. Augmentez."
                elif proposition > self.nombre_magic:
                    message = "Le nombre à deviner est plus petit. Diminuez."
                else:
                    message = f"Félicitations ! Vous avez trouvé le nombre exact qui est {self.nombre_magic}."
                    self.entry.config(state=tk.DISABLED)
                    self.button.config(state=tk.DISABLED)
            else:
                message = "Veuillez saisir un nombre entre 0 et 9999."
            self.label_decorative.config(text="**********")
            self.label_rules.config(text=message)
        except ValueError:
            self.label_rules.config(text="Veuillez saisir un nombre valide.")

if __name__ == "__main__":
    app = JeuDevinette()
    app.mainloop()
