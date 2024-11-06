from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

def hae_kentan_tiedot(icao):
    try:
        yhteys = sqlite3.connect('airports.sqlite')
        kursori = yhteys.cursor()
        sql = "SELECT icao, name, city FROM airports WHERE icao=?"
        kursori.execute(sql, (icao,))
        tulos = kursori.fetchone()
        yhteys.close() # MEMORY LEAK IF NOT CLOSED -WISSAM, SPEAKING FROM EXPERIENCE.

        if tulos:
            return {
                "ICAO": tulos[0],
                "Name": tulos[1],
                "Municipality": tulos[2]
            }
        return None

    except sqlite3.Error as virhe:
        print(f"Tietokantavirhe: {virhe}")
        return None

@app.route('/kentta/<icao>')
def kentan_tiedot(icao):
    icao = icao.upper()
    kentta = hae_kentan_tiedot(icao)
    if kentta:
        return jsonify(kentta)
    return jsonify({"error": f"Lentokenttää koodilla {icao} ei löytynyt"}), 404

app.run(host='127.0.0.1', port=3000)