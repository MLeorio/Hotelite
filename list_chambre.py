from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror, showinfo
from schema import Chambre
import main

import db_config

police_label = "comic sans MS"
police_entry = "book antiqua"



class Chambre_List:
    def __init__(self, root):
        self.root = root
        pad = 0
        self.root.title("Liste des chambres")
        self.root.geometry(
            f"{self.root.winfo_screenwidth()-pad}x{self.root.winfo_screenheight()-pad}"
        )
        
        self.top = LabelFrame(self.root)
        self.top.pack(side="top")
        
        self.bottom = Frame(self.root)
        self.bottom.pack(side="top")
        
        self.checkbox =Frame(self.root)
        self.checkbox.pack(side="top", pady=40)
        
        self.list = Frame(self.root)
        self.list.pack(side="top", pady=30)
        
        self.filter =Frame(self.root)
        self.filter.pack(side="top", pady=20)
        
        self.label = Label(self.top, font=("sans serif", 40, "bold"),
                           text="Liste de nos chambres", fg="#E70739", anchor="center")
        self.label.grid(row=0, column=3, pady=50)
        
        self.libelle = Label(self.bottom, font=(police_label, 20, "bold"), text="Entrer le libelle :", fg="#046380", anchor="w")
        self.libelle.grid(row=0, column=0, pady=30)
        
        self.libelle_var = StringVar()
        self.libelle_input = Entry(self.bottom, width=40, textvariable=self.libelle_var, font=(police_entry,18, "bold"), justify="center", validate="focusout", border=0, fg="#3B0405")
        self.libelle_input.grid(row=0, column=1, padx=10, pady=30, ipady=15)
        
        self.place = Label(self.bottom, font=(police_label, 20, "bold"), text="Entrer le nombre de place :", fg="#046380", anchor="w")
        self.place.grid(row=0, column=2, padx=10, pady=30)
        
        self.place_var = IntVar()
        self.place_input = Entry(self.bottom, width=40, textvariable=self.place_var, font=(police_entry,18, "bold"), justify="center", validate="focusout", border=0, fg="#3B0405")
        self.place_input.grid(row=0, column=3, padx=10, pady=30, ipady=15)
        
        
        self.table = ttk.Treeview(self.list, columns=(1, 2, 3, 4, 5, 6, 7, 8), show="headings")
        self.table.grid(row=0, column=1, padx=10, pady=10)
        
        self.table.heading(1, text="Numero") #8
        self.table.heading(2, text="Libelle") #1
        self.table.heading(3, text="Description") #6
        self.table.heading(4, text="Categorie") #2
        self.table.heading(5, text="Nombre de place") #4
        self.table.heading(6, text="Tarif")  #3
        self.table.heading(7, text="Etat") #5
        self.table.heading(8, text="Date") #7
        
        self.table.column(1, width=150)
        self.table.column(2, width=140)
        self.table.column(3, width=200)
        self.table.column(4, width=140)
        self.table.column(5, width=100)
        self.table.column(6, width=100)
        self.table.column(7, width=140)
        self.table.column(8, width=160)
        
        room_list = Chambre.get_rooms_list(self)
        
        for room in room_list:
            self.table.insert("", END, value=room)
        
        
        def recherche():
            libelle = self.libelle_input.get()
            nombre = self.place_input.get()
            
            if nombre != "" and nombre.isdigit() == False:
                showerror("Erreur", "Entrer une valeure numerique")
            else:
                val = (libelle.upper(), nombre)
                req = "SELECT * FROM CHAMBRE WHERE libelle = ? OR nbrPlace = ? "
                db_config.cur.execute(req, val)
                res = db_config.cur.fetchone()
                
                if res is not None:
                    self.table.delete(*self.table.get_children())
                    
                    self.table.insert("", END, value=res)
                    
                    showinfo("Trouve ! ", "Chambre Trouvee !")
                    self.libelle_input.delete(0, END)
                    self.place_input.delete(0, END)
                else:
                    showerror("Erreur", f"Chambre {libelle} de {nombre} places non trouvee")
                    self.libelle_input.delete(0, END)
                    
        def close():
            self.root.destroy()
            main.home_fen()
        
        def filtre():
            rooms = Chambre.get_free_rooms_list(self)
            self.table.delete(*self.table.get_children())
            
            for room in rooms:
                self.table.insert("", END, value=room)
            
            showinfo("Resultat", "Nombre de chambre Disponible : {}".format(len(rooms)))
        
        def all():
            rooms = Chambre.get_rooms_list(self)
            self.table.delete(*self.table.get_children())
            for room in rooms:
                self.table.insert("", END, value=room)
                
            showinfo("Resultat", "Nombre de toutes les chambres : {}".format(len(rooms)))
            
        
        
        self.bout_valider = Button(self.checkbox, text="Valider",font=(police_label, 16, "bold"), bg="#B0CC99", relief=RIDGE, height=2, width=50, fg="#3C108A", anchor="center", command=recherche)  
        self.bout_valider.grid(row=0, column=1, padx=10, pady=10) 
        
        self.bout_retour = Button(self.filter, text="Retour",font=(police_label, 16, "bold"), bg="maroon", relief=RIDGE, height=2, width=50, fg="aliceblue", anchor="center", command=close)  
        self.bout_retour.grid(row=1, column=0, padx=10, pady=30, columnspan=2)
        
        self.bout_disp = Button(self.filter, text="Chambre Disponible",font=(police_label, 16, "bold"), bg="#B0CC99", relief=RIDGE, height=2, width=30, fg="#3C108A", anchor="center", command=filtre)  
        self.bout_disp.grid(row=0, column=0, padx=10, pady=10)
        self.bout_init = Button(self.filter, text="Toutes les Chambres",font=(police_label, 16, "bold"), bg="#B0CC99", relief=RIDGE, height=2, width=30, fg="#3C108A", anchor="center", command=all)  
        self.bout_init.grid(row=0, column=1, padx=10, pady=10)
        
        
    
def list_chambre():
    root =Tk()
    Chambre_List(root)
    root.mainloop()
    

# list_chambre()