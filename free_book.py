from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror, showinfo
from schema import Reserver
import db_config
import datetime


police_label = "comic sans MS"
police_entry = "book antiqua"
police = "sans serif"


class Free_Book:
    def __init__(self,root):
        self.root = root
        pad = 0
        self.root.title("Liberer une chambre")
        self.root.geometry(
            f"{self.root.winfo_screenwidth()-pad}x{self.root.winfo_screenheight()-pad}"
        )
        
        self.list_booking = Reserver.get_valid_booking_list(self)
        
        
        
        def free():
            res_sel = self.list.focus()
            book = self.list.item(res_sel)['values']
            # print(type(book), book)
            
            
            if type(book) == str:
                showerror("Erreur", "Veuillez choir une reservation !")
            else:
                etat = "TERMINER"
                dt = datetime.datetime.now()
                
                req = """ UPDATE reserver SET etat = ?,  free_at = ?  WHERE client = ? AND chambre = ? AND book_at = ? """
                db_config.cur.execute(req, [etat, dt, book[0], book[1], book[2]])
                
                req2 = """ UPDATE chambre SET etat = 'DISPONIBLE' WHERE numero = ? """
                db_config.cur.execute(req2, [book[1]])
                
                db_config.con.commit()
                
                showinfo("Reussi", "Chambre libierer avec success !")
                
                self.list.delete(*self.list.get_children())
                
                self.list_booking = Reserver.get_valid_booking_list(self)
                
                for book in self.list_booking:
                    self.list.insert("", END, value=book)
                
            
             
        
        self.top = LabelFrame(self.root)
        self.top.pack(side="top")
        
        
        self.table = Frame(self.root)
        self.table.pack(side="top")
        
        self.bottom = Frame(self.root)
        self.bottom.pack(side="top")
        
        self.label = Label(self.top, font=(police, 40, "bold"),
                           text="Liberer une chambre", fg="#E70739", anchor="center")
        self.label.grid(row=0, column=3, pady=50, columnspan=3)
        
        self.bout_val = Button(self.bottom, text="Liberer la chambre",font=(police_label, 16, "bold"), bg="#B0CC99", relief=RIDGE, height=2, width=50, fg="#3C108A", anchor="center", command=free)
        self.bout_val.grid(row=2, column=2, padx=10, pady=10)
        
        self.list = ttk.Treeview(self.table, columns=(1, 2, 3, 4, 5, 6), show="headings")
        self.list.grid(row=0, column=1, padx=10, pady=60, columnspan=2)
        
        self.list.heading(1, text="Client")
        self.list.heading(2, text="Chambre")
        self.list.heading(3, text="Date de reservation")
        self.list.heading(4, text="Nombre de jour")
        self.list.heading(5, text="Etat")
        self.list.heading(6, text="FIN")
        
        for book in self.list_booking:
            self.list.insert("", END, value=book)

def free():
    root = Tk()
    Free_Book(root)
    root.mainloop()

# free()