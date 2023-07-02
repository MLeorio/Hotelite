import db_config
import datetime


class Chambre:
    def __init__(self, numero, libelle, description, tarif, categorie, nbrPlace, etat, created_at):
        self.numero = numero.upper()
        self.libelle = libelle.upper()
        self.description = description.upper()
        self.tarif = tarif
        self.categorie = categorie.upper()
        self.nbrPlace = nbrPlace
        self.etat = etat.upper()
        self.created_at = created_at

    def __str__(self):
        return self.numero
    
    def save_chb(self):
        """Methode d'enregistrement des infos de la chamnbre dans la base de donnees
        """
        req = "INSERT INTO chambre(libelle, categorie, tarif, nbrPlace, etat, description, created_at, numero) VALUES(?, ?, ?, ?, ?, ?, ?, ?)"
        val =  (self.libelle, self.categorie, self.tarif, self.nbrPlace, self.etat, self.description, self.created_at, self.numero)
        db_config.cur.execute(req,val)
        
        
        db_config.con.commit()
        
        return "Objet Chambre enregistre avec succes"
    
    def get_rooms_list(self):
        req = "SELECT * FROM chambre"
        db_config.cur.execute(req)
        res = db_config.cur.fetchall()
        return res
    
    def get_free_rooms_list(self):
        req = "SELECT * FROM chambre WHERE etat = 'DISPONIBLE' "
        db_config.cur.execute(req)
        res = db_config.cur.fetchall()
        return res
    

class Client:
    def __init__(self,id_client, nom, prenom, telephone, book_at):
        self.id_client = id_client.upper()
        self.nom = nom.upper()
        self.prenom = prenom.upper()
        self.telephone = telephone
        self.book_at = book_at
        
    
    def save_clt(self):
        """Methode save_clt :
        permet d'enregistrer un client dans la base de donnees
        """
        val = (self.id_client, self.nom, self.prenom, self.telephone, self.book_at)
        req = "INSERT INTO client (id_client, nom, prenom, telephone, book_at) VALUES(?, ?, ?, ?, ?)"
        
        db_config.cur.execute(req, val)
        
        db_config.con.commit()
        
        return "Objet Client enregistre avec succes"
    
    def get_client_list(self):
        """ Methode get_client_list :
        permet de recuperer la liste des clients enregistres
        """
        
        req = "SELECT * FROM client"
        db_config.cur.execute(req)
        
        res = db_config.cur.fetchall()
        return res
    
    def get_last_client(self):
        """Methode get_last_client :
        permet de recuperer le dernier client enregistre
        """
        req = "SELECT * FROM client"
        db_config.cur.execute(req)
        
        res = db_config.cur.fetchall()
        
        return res[-1]


class Reserver:
    def __init__(self, client, chambre, date, sejour, etat):
        self.client = client.upper()
        self.chambre = chambre.upper()
        self.date = date
        self.sejour = sejour
        self.etat = etat.upper()
    
    def __str__(self):
        return self.client + " " + self.date
    
    def save_booking(self):
        val = [self.client, self.chambre, self.date, self.sejour, self.etat]
        req = " INSERT INTO reserver(client, chambre, book_at, sejour, etat) VALUES(?, ?, ?, ?, ?) "
        db_config.cur.execute(req, val)
        
        req = " UPDATE chambre SET etat = 'RESERVER' WHERE numero = ?"
        db_config.cur.execute(req, [self.chambre])
        
        db_config.con.commit()  
        
        return "Reservation effectuee avec succes"
    
    def get_valid_booking_list(self):
        """"Methode get_valid_booking_list:
        renvoie la liste des reservation effective
        """
        req = "SELECT * FROM reserver WHERE etat='ACTIVE' "
        db_config.cur.execute(req)
        res = db_config.cur.fetchall()
        
        return res