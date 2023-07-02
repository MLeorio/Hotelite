from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror, showinfo
import schema
from utils import num_room
import main
import datetime

categorie = [
    "Selectionner une categorie",
    "Piece simple",
    "Piece avec deux places"
]

police_label = "comic sans MS"
police_entry = "book antiqua"


class Chambre:
    def __init__(self, root):
        self.root = root
        pad = 20
        self.root.title("Ajout de chambre")
        self.root.geometry(
            f"{self.root.winfo_screenwidth()-pad}x{self.root.winfo_screenheight()-pad}"
        )
        
        self.top = LabelFrame(self.root)
        self.top.pack(side="top")
        
        self.bottom = Frame(self.root)
        self.bottom.pack(side="top")
        
        self.checkbox =Frame(self.root)
        self.checkbox.pack(side="top", pady=40)
        
        self.label = Label(self.top, font=("sans serif", 40, "bold"),
                           text="Ajout de chambre", fg="#E70739", anchor="center")
        self.label.grid(row=0, column=3, pady=50)
        
        self.libelle = Label(self.bottom, font=(police_label, 20, "bold"), text="Entrer le libelle :", fg="#046380", anchor="w")
        self.libelle.grid(row=0, column=0, pady=30)
        
        self.libelle_var = StringVar()
        self.libelle_input = Entry(self.bottom, width=40, textvariable=self.libelle_var, font=(police_entry,18, "bold"), justify="center", validate="focusout", border=0, fg="#3B0405")
        self.libelle_input.grid(row=0, column=1, padx=10, pady=30, ipady=15)
        
        self.categorie = Label(self.bottom, font=(police_label, 20, "bold"), text="Choisir la categorie :", fg="#046380", anchor="w")
        self.categorie.grid(row=0, column=2, padx=10, pady=30)

        self.categorie_input = ttk.Combobox(self.bottom, width=40, values=categorie, font=(police_entry,18, "bold"), justify="center")
        self.categorie_input.current(0)
        self.categorie_input.grid(row=0, column=3, padx=10, pady=30, ipady=15)
        
        self.nombre_place = Label(self.bottom, font=(police_label, 20, "bold"), text="Le nombre de place :", fg="#046380", anchor="w")
        self.nombre_place.grid(row=1, column=0, pady=30)
        
        self.place_var = IntVar()
        self.place_input = Entry(self.bottom, width=40, textvariable=self.place_var, font=(police_entry,18, "bold"), justify="center", validate="focusout", border=0, fg="#3B0405")
        self.place_input.grid(row=1, column=1, padx=10, pady=30, ipady=15)
        
        self.tarif = Label(self.bottom, font=(police_label, 20, "bold"), text="Definir le tarif / jour :", fg="#046380", anchor="w")
        self.tarif.grid(row=1, column=2, padx=10, pady=30)
        
        self.tarif_var = IntVar()
        self.tarif_input = Entry(self.bottom, width=40, textvariable=self.tarif_var, font=(police_entry,18, "bold"), justify="center", validate="focusout", border=0, fg="#3B0405" )
        self.tarif_input.grid(row=1, column=3, padx=10, pady=30, ipady=15)
        
        self.description = Label(self.bottom, font=(police_label, 20, "bold"), text="Description de la chambre :", fg="#046380", anchor="w")
        self.description.grid(row=2, column=1, padx=10, pady=30)
        
        self.description_var = StringVar()
        self.description_input = Entry(self.bottom, width=40, textvariable=self.description_var, font=(police_entry,18, "bold"), justify="left", validate="focusout", border=0, fg="#3B0405")
        self.description_input.grid(row=2, column=2, padx=10, pady=30, ipady=15)
        
        def valider():
            global ans
            libelle = self.libelle_input.get()
            categorie = self.categorie_input.get()
            nombre_place = self.place_input.get()
            tarif = self.tarif_input.get()
            description = self.description_input.get()
            
            self.erreur = None
            
            try:
                nombre = int(nombre_place)
                frais =  int(tarif)
            except ValueError:
                self.erreur = "Veuillez saisir des donnees numerique pour le nombre de place et le tarif !!"
            
            if libelle == "" or categorie == "" or nombre_place == "" or tarif == "":
                showerror("Erreur","Veuillez remplir tous les champs corectement !!")
            elif self.erreur :
                showerror("Erreur", self.erreur)
            else:
                # print(libelle, categorie, nombre, frais, description)
                n = num_room(libelle, nombre)
                room = schema.Chambre(
                    n,
                    libelle,
                    description,
                    frais,
                    categorie,
                    nombre,
                    "Disponible",
                    datetime.datetime.now()
                )
                msg = room.save_chb()
                showinfo("Succes", msg)
        
        def close():
            self.root.destroy()
            main.home_fen()
            
                    
        self.bout_valider = Button(self.checkbox, text="Valider",font=(police_label, 16, "bold"), bg="#B0CC99", relief=RIDGE, height=2, width=50, fg="#3C108A", anchor="center", command=valider)  
        self.bout_valider.grid(row=0, column=1, padx=10, pady=10) 
         
        self.bout_retour = Button(self.checkbox, text="Retour",font=(police_label, 16, "bold"), bg="maroon", relief=RIDGE, height=2, width=50, fg="aliceblue", anchor="center", command=close)  
        self.bout_retour.grid(row=1, column=1, padx=10, pady=10)    
        
        
def add_chambre():
    root = Tk()
    Chambre(root)
    root.mainloop()

# add_chambre()