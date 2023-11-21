import sqlite3
conn = sqlite3.connect('calcolatrice.db')  # Crea una connessione al database SQLite
c = conn.cursor()  # Crea un cursore

# Crea una nuova tabella
c.execute('''
    CREATE TABLE risultati (
        id INTEGER PRIMARY KEY
    )
''')

conn.commit()  # Salva le modifiche
conn.close()  # Chiude la connessione al database