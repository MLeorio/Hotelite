from db_config import con, cur
import datetime

req = "CREATE TABLE CHAMBRE(numero VARCHAR(50) NOT NULL PRIMARY KEY, libelle VARCHAR(80) NOT NULL, description VARCHAR(150), categorie VARCHAR(80) NOT NULL, nbrPlace INT NOT NULL, tarif INT NOT NULL, etat VARCHAR(50) NOT NULL, created_at DATE)"
cur.execute(req)

req = "CREATE TABLE CLIENT(id_client VARCHAR(20) NOT NULL PRIMARY KEY ,nom VARCHAR(50) NOT NULL,prenom VARCHAR(50) NOT NULL,telephone VARCHAR(50) NOT NULL,book_at DATE NOT NULL)"
cur.execute(req)

req = "CREATE TABLE RESERVER(client VARCHAR(50) NOT NULL,chambre VARCHAR NOT NULL, book_at DATE NOT NULL, sejour INT, etat VARCHAR(80) NOT NULL,free_at DATE)"
cur.execute(req)


con.commit()
cur.close()
con.close()


                # dt = datetime.datetime.fromtimestamp(book)