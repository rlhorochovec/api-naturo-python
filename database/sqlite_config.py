import sqlite3

def connect_to_db():
    conn = sqlite3.connect('database/naruto.db')
    return conn

def create_db_table():
    try:
        conn = connect_to_db()
        conn.execute('''
            CREATE TABLE IF NOT EXISTS ninjas (
                id INTEGER PRIMARY KEY NOT NULL,
                name TEXT NOT NULL,
                village TEXT NOT NULL
            );
        ''')
        conn.commit()
        print("Table created/found successfully.")
    except:
        print("Table creation failed!")
    finally:
        conn.close()

create_db_table()

def insert_ninja(ninja):
    inserted_ninja = {}
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO ninjas (name, village) VALUES (?, ?)", (ninja['name'], ninja['village']) )
        conn.commit()
        inserted_ninja = get_ninja_by_id(cur.lastrowid)
    except:
        conn().rollback()
    finally:
        conn.close()

    return inserted_ninja

def get_ninjas():
    ninjas = []
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM ninjas")
        rows = cur.fetchall()

        # convert row objects to dictionary
        for i in rows:
            ninja = {}
            ninja["id"] = i["id"]
            ninja["name"] = i["name"]
            ninja["village"] = i["village"]
            ninjas.append(ninja)
    except:
        ninjas = []

    return ninjas

def get_ninja_by_id(id):
    ninja = {}
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM ninjas WHERE id = ?", (id,))
        row = cur.fetchone()

        # convert row object to dictionary
        ninja["id"] = row["id"]
        ninja["name"] = row["name"]
        ninja["village"] = row["village"]
    except:
        ninja = {}

    return ninja


def update_ninja(ninja):
    updated_ninja = {}
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute("UPDATE ninjas SET name = ?, village = ? WHERE id =?", (ninja["name"], ninja["village"], ninja["id"]))
        conn.commit()
        #return the ninja
        updated_ninja = get_ninja_by_id(ninja["id"])

    except:
        conn.rollback()
        updated_ninja = {}
    finally:
        conn.close()

    return updated_ninja


def delete_ninja(id):
    message = {}
    try:
        conn = connect_to_db()
        conn.execute("DELETE from ninjas WHERE id = ?", (id,))
        conn.commit()
        message["status"] = "Deleted successfully."
    except:
        conn.rollback()
        message["status"] = "Cannot delete ninja!"
    finally:
        conn.close()

    return message