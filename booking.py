from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror, showinfo
import schema
import main
import db_config
import datetime


police_label = "comic sans MS"
police_entry = "book antiqua"
police = "sans serif"


class Book:
    def __init__(self, root):
        self.root = root
        pad = 0
        self.root.title("Faire un reservation")
        self.root.geometry(
            f"{self.root.winfo_screenwidth()-pad}x{self.root.winfo_screenheight()-pad}"
        )
        t = "Choisir une chambre"
        
        clients = ["Choisir un client"]
        rooms = ["Choisir une chambre"]
        
        self.clients_col = schema.Client.get_client_list(self)
        self.rooms_col = schema.Chambre.get_free_rooms_list(self) 

        
        for clt in self.clients_col:
            clients.append(str(clt[0]))
        
        for room in self.rooms_col:
            rooms.append(str(room[0]))
            
        
        def close():
            self.root.destroy()
            main.home_fen()
        
        def rechercher():
            nom = self.nom_input.get()
            prenom = self.prenom_input.get()
            numero = self.numero_input.get()
            
            req = """SELECT * from client WHERE nom = ? OR prenom = ? OR telephone = ? """
            db_config.cur.execute(req, [nom.upper(), prenom.upper(), numero])
            res = db_config.cur.fetchone()
            
            if res == None:
                showerror("Probleme", "Clients non trouve, veuillez l'ajouter a la base !")
            else:
                num_cli = res[0]
                self.resultat.configure(text=f"Le numero du client est << {num_cli} >>")
        
        
        def reserver():
            client = self.client.get()
            chambre = self.chambre.get()
            nbr_sejour = str(self.sejour_input.get())
            
            if client == "Choisir un client" or chambre == "Choisir une chambre" or nbr_sejour.isdigit() == False :
                showerror("Erreur", "Veuillez remplir tous les champs ! ")
            else:
                booking = schema.Reserver(
                    client,
                    chambre,
                    datetime.datetime.now(),
                    nbr_sejour,
                    "active")
                
                msg = booking.save_booking()
                showinfo("Succes", msg)
                
                rooms = [t]
                
                self.list_chambre = schema.Chambre.get_free_rooms_list(self)
                for room in self.list_chambre:
                    rooms.append(str(room[1]))
                    
                self.client.current(0)
                self.chambre.current(0)
                self.sejour_input.delete(0, END)
                
                
            
        
        self.top = LabelFrame(self.root)
        self.top.pack(side="top")
        
        self.bottom = Frame(self.root)
        self.bottom.pack(side="top")
        
        self.bout = Frame(self.root)
        self.bout.pack(side="top")
        
        self.label = Label(self.top, font=(police, 40, "bold"),
                           text="Faire une reservation", fg="#E70739", anchor="center")
        self.label.grid(row=0, column=3, pady=50, columnspan=3)
        
        self.left = Frame(self.bottom, border=2, relief=SOLID)
        self.left.grid(row=0, column=0, padx=50, pady=30, rowspan=3, ipadx=5, ipady=5)
        
        self.client_libelle = Label(self.bottom, font=(police_label, 20, "bold"), text="Choisir un client :", fg="#046380", anchor="w")
        self.client_libelle.grid(row=0, column=1, pady=30)
        
        self.client = ttk.Combobox(self.bottom, width=30, values=clients, font=(police_entry,18, "bold"), justify="center")
        self.client.current(0)
        self.client.grid(row=0, column=2, padx=10, pady=30, ipady=15)
        
        
        self.chambre_libelle = Label(self.bottom, font=(police_label, 20, "bold"), text="Choisir une chambre :", fg="#046380", anchor="w")
        self.chambre_libelle.grid(row=0, column=3, pady=30)
        
        self.chambre = ttk.Combobox(self.bottom, width=30, values=rooms, font=(police_entry,18, "bold"), justify="center")
        self.chambre.current(0)
        self.chambre.grid(row=0, column=4, padx=10, pady=30, ipady=15)
        
        self.sejour_libelle = Label(self.bottom, font=(police_label, 20, "bold"), text="Nombre de jour reserve :", fg="#046380", anchor="e")
        self.sejour_libelle.grid(row=1, column=3,  pady=25)
        
        self.sejour_var = IntVar()
        self.sejour_input = Entry(self.bottom, width=30, textvariable=self.sejour_var, font=(police_entry,18, "bold"), justify="center", validate="focusout", border=1, relief=SOLID, fg="#3B0405")
        self.sejour_input.grid(row=1, column=4,pady=30, ipady=15,)
        
        self.bout_valider = Button(self.bout,text="Reserver",font=(police_label, 16, "bold"), bg="#B0CC99", relief=RIDGE, height=2, width=30, fg="#3C108A", anchor="center", command=reserver)  
        self.bout_valider.grid(row=0, column=1, padx=10, pady=10)
        
        self.bout_retour = Button(self.bout, text="Retour",font=(police_label, 16, "bold"), bg="maroon", relief=RIDGE, height=2, width=30, fg="aliceblue", anchor="center", command=close)  
        self.bout_retour.grid(row=0, column=2, padx=10, pady=10)
        
        # Formulaire de recherche d'un client
        Label(self.left, font=(police,25, "bold"), text="Trouver un client", fg="#3C108A", anchor="center").grid(row=0, column=0, pady=20, columnspan=2)
        
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
        
        self.bout_valid = Button(self.left, text="Rechercher",font=(police_label, 12, "bold"), bg="#B0CC99", relief=RIDGE, height=1, width=10, fg="#3C108A", anchor="center", command=rechercher)
        self.bout_valid.grid(row=4, column=1, padx=10, pady=10)
        
        self.resultat = Label(self.left, font=(police,14, "bold"), text="", fg="#3C108A", anchor="center")
        self.resultat.grid(row=5, column=0, padx=5, pady=10, columnspan=2)
        
        

def book():
    root = Tk()
    Book(root)
    root.mainloop()
    

# book()