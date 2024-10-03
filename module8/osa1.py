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
    sql = f"SELECT name,municipality FROM airport where IDENT='{country}'"
    kursori = con.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount >0 :
        for rivi in tulos:
            print(f"Hei! Olen {rivi[0]}. Sijaitseen {rivi[1]} ")
    return

country = input("ICAO code: ")
hae_lentokentat(country)