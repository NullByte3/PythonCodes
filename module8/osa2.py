import mysql.connector

con = mysql.connector.connect(
    host='localhost',
    port= 3306,
    database='flight_game',
    user='vivsam',
    password='123',
    autocommit=True
)

def hae_lentokentat(country):
    sql = f"SELECT type, COUNT(type) AS maara FROM airport where iso_country='{country}'GROUP by type asc"
    kursori = con.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount >0 :
        for rivi in tulos:
            print(f"{rivi[0]} on x{rivi[1]}")
    return

country = input("Maa koodi: ")
hae_lentokentat(country)