
from random import randint


def num_room(libelle:str, nombre_place:int):
    num = "LYSE-"
    n = 0
    while n <= 5:
        num += libelle[randint(0, len(libelle)-1)]
        n += 1
    num += f"/{nombre_place}"
    return num


def num_clt(nom:str, prenom:str):
    num = nom[:3] + prenom[:2]
    return num
