import records

DB_HOST = "mariadb"
DB_PORT = 3306
DB_NAME = "places"
DB_USER = "traveler"
DB_PASSWORD = "ticket"
DB_CONNECTION_STRING = f"mysql+mysqldb://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


def test_mariadb_access():
    db = records.Database(DB_CONNECTION_STRING)

    rows = db.query("SELECT * FROM destinations")

    actual_place_names = set([row["place_name"] for row in rows])

    assert actual_place_names == {"Stockholm", "Honolulu", "San Diego"}
