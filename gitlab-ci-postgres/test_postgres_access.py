import records

DB_HOST = "postgres"
DB_PORT = 5432
DB_NAME = "places"
DB_USER = "traveler"
DB_PASSWORD = "ticket"
DB_CONNECTION_STRING = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

def test_postgres_access():
    db = records.Database(DB_CONNECTION_STRING)

    rows = db.query("SELECT * FROM destinations")

    actual_place_names = set([row["place_name"] for row in rows])

    assert actual_place_names == {"Stockholm", "Honolulu", "San Diego"}
