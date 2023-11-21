from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3


def main():
    app = FastAPI()

    class Risultato(BaseModel):
        risultato: int

    @app.get("/add")
    def add(a: int, b: int):
        return {"result": a + b}

    @app.get("/subtract")
    def subtract(a: int, b: int):
        return {"result": a - b}

    @app.post("/inserisci/")
    async def inserisci_risultato(risultato: Risultato):
        conn = sqlite3.connect('calcolatricd.db')
        c = conn.cursor()

        # Inserisci il risultato nella tabella
        c.execute("INSERT INTO risultati (risultato) VALUES (?)", (risultato.risultato,))

        conn.commit()
        conn.close()

        return {"messaggio": "Risultato inserito con successo"}


if __name__ == "__main__":
    main()