import sqlite3

def init_db():
    # Création (ou ouverture) de collection.db
    conn = sqlite3.connect("collection.db")
    cur = conn.cursor()

    # Création de la table des cartes
    cur.execute("""
    CREATE TABLE IF NOT EXISTS cards (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        expansion TEXT,
        collector_number TEXT,
        condition TEXT,
        language TEXT,
        foil BOOLEAN,
        quantity INTEGER DEFAULT 1,
        purchase_price REAL,
        listing_id INTEGER,
        mk_id INTEGER
    );
    """)

    # Sauvegarde et fermeture
    conn.commit()
    conn.close()

if __name__ == '__main__':
    # Exécution
    init_db()
