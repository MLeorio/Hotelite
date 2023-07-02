from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror, showinfo
from schema import Client
from utils import num_clt
import datetime
import db_config
import main

police_label = "comic sans MS"
police_entry = "book antiqua"
police = "sans serif"



class Clients:
    def __init__(self, root):
        self.root = root
        pad = 0
        self.root.title("Liste des Client")
        self.root.geometry(
            f"{self.root.winfo_screenwidth()-pad}x{self.root.winfo_screenheight()-pad}"
        )
        
        def recherche():
            nom = self.nom_rech_input.get()
            
            if nom == "":
                showerror("Erreur", "Entrer une valeure a rechercher")
            else:
                req = """ SELECT * FROM client WHERE nom = ? """
                db_config.cur.execute(req, [nom.upper()])
                res = db_config.cur.fetchall()
                
                if len(res) == 0:
                    showerror("Erreur", "Client non trouve")
                for room in res:
                    # self.table.insert("", END, value=room)
                    showinfo("Trouve", f"Client {room[1]} trouve")
        
        def close():
            self.root.destroy()
            main.home_fen()
        
        def ajouter():
            nom = self.nom_input.get()
            prenom = self.prenom_input.get()
            numero = str(self.numero_input.get())
            
            if nom == "" or prenom == "" or numero == "":
                showerror("Erreur", "Veuillez remplir tous les champs ! ")
            elif numero.isdigit() == False or len(numero) == 0 or len(numero) < 8:
                showerror("Erreur", "Entrer un numero valide !!")
            else:
                clt = Client(
                             num_clt(nom, prenom),
                             nom,
                             prenom,
                             numero,
                             datetime.datetime.now()
                )
                msg = clt.save_clt()
                room = Client.get_last_client(self)
                
                
                self.table.insert("", END, value=room)
                    
                showinfo("Succes", msg)
                
                
                
        
        
        self.ttop = LabelFrame(self.root)
        self.ttop.pack(side="top")
        
        self.top = Frame(self.root)
        self.top.pack(side="top", pady=15, ipady=20)
        
        self.left = Frame(self.top, border="1", relief="raised")
        self.left.pack(side="left", padx=15, ipady=20, ipadx=15)
        
        self.top_right = Frame(self.top)
        self.top_right.pack(side="right", padx=15)
        
        self.right = Frame(self.top_right, border=1, relief="ridge")
        self.right.pack(side="top")
        
        self.right_botom = Frame(self.top_right)
        self.right_botom.pack(side="top")
                        
        self.list = Frame(self.root)
        self.list.pack(side="bottom", pady=50)
        
        self.label = Label(self.ttop, font=(police, 40, "bold"),
                           text="Liste des Clients", fg="#E70739", anchor="center")
        self.label.grid(row=0, column=3, pady=50)
        
        Label(self.left, font=(police,25, "bold"), text="Ajouter un client", fg="#3C108A", anchor="center").grid(row=0, column=1, pady=20)
        
        self.nom = Label(self.left, font=(police_label, 14, "bold"), text="Nom :", fg="#046380", anchor="e")
        self.nom.grid(row=1, column=0, pady=10, padx=10)
        
        self.nom_var = StringVar()
        self.nom_input = Entry(self.left, textvariable=self.nom_var, width=20, font=(police_entry, 14, "bold"), justify="center", border=0, fg="#3B0405")
        self.nom_input.grid(row=1, column=1, padx=30, pady=10, ipady=15)
        
        self.prenom = Label(self.left, font=(police_label, 14, "bold"), text="Prenom :", fg="#046380", anchor="e")
        self.prenom.grid(row=2, column=0, pady=10, padx=10)
        
        self.prenom_var = StringVar()
        self.prenom_input = Entry(self.left, textvariable=self.prenom_var, width=20, font=(police_entry, 14, "bold"), justify="center", border=0, fg="#3B0405")
        self.prenom_input.grid(row=2, column=1, padx=30, pady=10, ipady=15)
        
        self.numero = Label(self.left, font=(police_label, 14, "bold"), text="Numero :", fg="#046380", anchor="e")
        self.numero.grid(row=3, column=0, pady=10, padx=10)
        
        self.numero_var = IntVar()
        self.numero_input = Entry(self.left, textvariable=self.numero_var, width=20, font=(police_entry, 14, "bold"), justify="center", border=0, fg="#3B0405")
        self.numero_input.grid(row=3, column=1, padx=30, pady=10, ipady=15)
        
        self.bout_valid = Button(self.left, text="Valider",font=(police_label, 14, "bold"), bg="#B0CC99", relief=RIDGE, height=2, width=20, fg="#3C108A", anchor="center", command=ajouter)
        self.bout_valid.grid(row=4, column=1, padx=10, pady=10)
        
        Label(self.right, text="Trouver un client", font=(police,25, "bold"), fg="#3C108A", anchor="center").grid(row=0, column=1, pady=20)
        
        self.nom_lib = Label(self.right, text="Nom du client", font=(police_label, 14, "bold"), fg="#046380", anchor="e")
        self.nom_lib.grid(row=1, column=0, padx=10, pady=10)
        
        self.nom_rech_var = StringVar()
        self.nom_rech_input = Entry(self.right, width=40, textvariable=self.nom_rech_var, font=(police_entry,18, "bold"), justify="center", validate="focusout", border=0, fg="#3B0405")
        self.nom_rech_input.grid(row=1, column=1, padx=10, pady=30, ipady=15)
        
        self.bout_rech = Button(self.right, text="Rechercher",font=(police_label, 13, "bold"), bg="#B0CC99", relief=RIDGE, height=1, width=15, fg="#3C108A", anchor="center", command=recherche)
        self.bout_rech.grid(row=1, column=2, padx=10, pady=30)
         
        self.bout_retour = Button(self.right_botom, text="Retour",font=(police_label, 16, "bold"), bg="maroon", relief=RIDGE, height=1, width=15, fg="aliceblue", anchor="center", command=close)
        self.bout_retour.grid(row=0, column=1, padx=10, pady=40)
        
        self.table = ttk.Treeview(self.list, columns=(1, 2, 3, 4, 5), show="headings")
        self.table.grid(row=0, column=1, padx=10, pady=10)
        
        self.table.heading(1, text="Code")
        self.table.heading(2, text="Nom")
        self.table.heading(3, text="Prenoms")
        self.table.heading(4, text="Numero")
        self.table.heading(5, text="Date arrivee")
        
        self.clts = Client.get_client_list(self)
        
        for clt in self.clts:
            self.table.insert("", END, value=clt)
        
        
    
def client_ui():
    root = Tk()
    Clients(root)
    root.mainloop()
    

# client_ui()