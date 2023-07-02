CREATE TABLE client(
    id_client VARCHAR(20) not null PRIMARY KEY,
    nom varchar(50) not null,
    prenom varchar(100) not null,
    numero varchar(10) not null UNIQUE,
    book_at DATE not null
)

CREATE TABLE chambre(
	numero VARCHAR(50) NOT NULL PRIMARY KEY,
	libelle VARCHAR(50) NOT NULL,
	description VARCHAR(150),
	categorie VARCHAR(80) NOT NULL,
	nbrPlace INT NOT NULL,
	tarif INT NOT NULL,
	etat VARCHAR(50) NOT NULL,
	created_at DATE
)

create table reserver(
	client varchar(50) not null,
	chambre varchar(50) not null,
	book_at date not null,
	sejour int not null,
	etat varchar(50) not null,
	free_at date,
	
	foreign key (client) References client(id_client),
	foreign key (chambre) References chambre(numero),
	
	primary key(client, chambre, book_at)
)