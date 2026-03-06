import sqlite3

def add_card(card):
    conn = sqlite3.connect("./collection.db")
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO cards
        (name, expansion, collector_number, condition, language, foil, quantity, purchase_price)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        card["name"],
        card["expansion"],
        card["collector_number"],
        card["condition"],
        card["language"],
        card["foil"],
        card["quantity"],
        card["purchase_price"]
    ))

    conn.commit()
    conn.close()


if __name__ == '__main__':
    conn = sqlite3.connect("collection.db")
    cur = conn.cursor()

    cur.execute("SELECT * FROM cards;")
    print(cur.fetchall())

    conn.close()
