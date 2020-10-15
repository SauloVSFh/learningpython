#Creating a sqlite3 data base using the json data
import sqlite3
import json

conn = sqlite3.connect("MPBDataSet.sqlite3")
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Caracteristica;
DROP TABLE IF EXISTS Interpretes;
DROP TABLE IF EXISTS Arranjadores;
DROP TABLE IF EXISTS Gravadora;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Faixa''')

cur.executescript('''
CREATE TABLE Caracteristica (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, name Text UNIQUE);
CREATE TABLE Interpretes (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, name Text UNIQUE);
CREATE TABLE Arranjadores (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, name Text UNIQUE);
CREATE TABLE Gravadora (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, name Text UNIQUE);
CREATE TABLE Album (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, name Text UNIQUE, gravadora_id INTEGER, interprete_id INTEGER, caracteristica_id INTEGER);
CREATE TABLE Faixa (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,name Text UNIQUE,album_id INTEGER, arranjadores_id INTEGER);
''')

def variavel(path):
    try:
        var = path.strip()
        return var
    except:
        return None

with open("MPBDataSet.json", encoding='utf8') as fr:
    js = json.load(fr)
    for item in js:
        album = variavel(item['album'])
        try: caracteristica = variavel(item['info_album']['Característica']) #vocal / vocal e instrumental / instrumental
        except: caracteristica = None
        gravadora = variavel(item['info_album']['Gravadora'])
        interpretes = variavel(item['interpretes'][0])
        for ms in item['faixas'].items():
            try: faixa = (ms[1]['musica'][0])
            except: faixa = None
            try: arranjadores = (ms[1]['arranjadores'][0])
            except: arranjadores = None
        if album is None or interpretes is None or faixa is None: continue

        # print(album, caracteristica, gravadora, interpretes, faixa, arranjadores)

        cur.execute('''INSERT OR IGNORE INTO Caracteristica (name)
            VALUES (?)''', (caracteristica,))
        cur.execute('''INSERT OR IGNORE INTO Interpretes (name)
            VALUES (?)''', (interpretes,))
        cur.execute('''INSERT OR IGNORE INTO Arranjadores (name)
            VALUES (?)''', (arranjadores,))
        cur.execute('''INSERT OR IGNORE INTO Gravadora (name)
            VALUES (?)''', (gravadora,))

        cur.execute('''SELECT id FROM Caracteristica WHERE name = ?''', (caracteristica,))
        try : caracteristica_id = cur.fetchone()[0]
        except: caracteristica_id = None
        cur.execute('''SELECT id FROM Interpretes WHERE name = ?''', (interpretes,))
        interpretes_id = cur.fetchone()[0]
        cur.execute('''SELECT id FROM Arranjadores WHERE name = ?''', (arranjadores,))
        try : arranjadores_id = cur.fetchone()[0]
        except: arranjadores_id = None
        cur.execute('''SELECT id FROM Gravadora WHERE name = ?''', (gravadora,))
        gravadora_id = cur.fetchone()[0]

        cur.execute('''INSERT OR IGNORE INTO Album (name,gravadora_id,interprete_id,caracteristica_id)
            VALUES (?,?,?,?)''', (album,gravadora_id,interpretes_id,caracteristica_id))
        cur.execute('''SELECT id FROM Album WHERE name = ?''', (album,))
        album_id = cur.fetchone()[0]

        cur.execute('''INSERT OR REPLACE INTO Faixa (name,album_id,arranjadores_id)
            VALUES (?,?,?)''', (faixa,album_id,arranjadores_id))
        conn.commit()

    cur.execute('''
    SELECT
    	Faixa.name AS Tracks,
    	Album.name AS Albums,
    	Caracteristica.name AS Style,
    	Interpretes.name AS Interpreters,
    	Gravadora.name AS Producers
    FROM
    	Faixa
    INNER JOIN Album ON Faixa.album_id = Album.id
    INNER JOIN Caracteristica ON Album.caracteristica_id = Caracteristica.id
    INNER JOIN Interpretes ON Album.interprete_id = Interpretes.id
    INNER JOIN Gravadora ON Album.gravadora_id = Gravadora.id
    ORDER BY
    	Faixa.name
    ''')
    #

conn.close()
