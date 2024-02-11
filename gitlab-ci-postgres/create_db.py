import records

DB_HOST = "postgres"
DB_PORT = 5432
DB_NAME = "places"
DB_USER = "traveler"
DB_PASSWORD = "ticket"
DB_CONNECTION_STRING = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

CREATE_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS destinations (
    id SERIAL PRIMARY KEY,
    place_name VARCHAR(256) NOT NULL,
    country VARCHAR(256) NOT NULL
)
"""

CREATE_SEED_DATA_SQL = """
INSERT INTO destinations(place_name, country) VALUES
('Honolulu', 'USA'),
('Stockholm', 'Sweden'),
('San Diego', 'USA')
"""

def create_table_with_seed_data():
    db = records.Database(DB_CONNECTION_STRING)
    db.query(CREATE_TABLE_SQL)
    db.query(CREATE_SEED_DATA_SQL)

create_table_with_seed_data()

