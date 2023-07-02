from tkinter import *
import create_chambre, list_chambre, list_clients, booking, free_book
import os


police = "comic sans MS"


class Hotel:
    def __init__(self, root):
        self.root = root
        pad = 20
        self.root.title("Gestion des reservation de chambres")
        self.root.geometry(
            f"{self.root.winfo_screenwidth()-pad}x{self.root.winfo_screenheight()-pad}"
        )

        # creation de la frame principale pour ajouter les messages
        top = Frame(self.root)
        top.pack(side="top")

        # creation de la frame pour ajouter les boutons
        bottom = Frame(self.root)
        bottom.pack(side="top")

        # Affichage des messages
        self.label = Label(top, font=("sans serif", 50, "bold"),
                           text="BIENVENUE A LYSE ENT HOTEL", fg="#E70739", anchor="center")
        self.label.grid(row=0, column=3, pady=45)

        # creation du bouton reservation check_in
        self.reserver = Button(bottom, text="Faire une reservation", font=(police, 20), bg="#15d3ba", relief=RIDGE, height=2,
                               width=50,
                               fg="black", anchor="center",
                               command=booking.book
                               )
        self.reserver.grid(row=0, column=2, padx=10, pady=10)

        # creation du bouton reservation check_out
        self.check_out = Button(bottom, text="Liberer une chambre", font=(police, 20), bg="#15d3ba", relief=RIDGE, height=2,
                                width=50,
                                fg="black",
                                anchor="center", command=free_book.free
                                )
        self.check_out.grid(row=1, column=2, padx=10, pady=10)

        # Creation du bouton d'ajout de chambres
        self.add_room = Button(bottom, text="Ajouter une chambre", font=(police, 20), bg="#15d3ba", relief=RIDGE, height=2,
                                width=50,
                                fg="black",
                                anchor="center",
                                command= create_chambre.add_chambre)
        self.add_room.grid(row=2, column=2, padx=10, pady=10)
        
        # Creation du bouton de la liste des chambres
        self.room_list = Button(bottom, text="Liste des chambres", font=(police, 20), bg="#15d3ba", relief=RIDGE, height=2,
                                width=50,
                                fg="black",
                                anchor="center",
                                command=list_chambre.list_chambre)
        self.room_list.grid(row=3, column=2, padx=10, pady=10)

        # creation du bouton de la liste des clients
        self.guest_list = Button(bottom, text="Liste des clients", font=(police, 20), bg="#15d3ba", relief=RIDGE, height=2,
                                 width=50,
                                 fg="black",
                                 anchor="center", command=list_clients.client_ui)
        self.guest_list.grid(row=4, column=2, padx=10, pady=10)

        # Bouton pour quitter l'application
        self.exit_button = Button(bottom, text="Quitter", font=('book antiqua', 16, "bold"), bg="#B9121B", relief=RIDGE, height=2, width=50,
                                  fg="#C4D7ED",
                                  anchor="center", command=quit)
        self.exit_button.grid(row=5, column=2, padx=10, pady=10)


def home_fen():
    root = Tk()
    Hotel(root)
    root.mainloop()


if __name__ == "__main__":
    home_fen()
