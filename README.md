# TODO list - Beginner

## Setting up

### Venv

```bash
# create a venv

python3 -m venv "nameofyourvenv"

# activate a venv

source myvenv/bin/activate
```

### Postgres

```psql
# create the db

CREATE DATABASE todolist;
GRANT ALL PRIVILEGES ON DATABASE todolist TO youruser;

# select the db

\c todolist;

# create table "todos"

CREATE SEQUENCE todolist_id_seq START 1;

CREATE TABLE todos ( 
    id INT DEFAULT nextval('todolist_id_seq') PRIMARY KEY, 
    text VARCHAR(200),
    complete BOOLEAN
);

# to connect to database

psql -U youruser yourdb
```

### Requirements

```bash
pip install -r requirements.txt

if you are on Debian, you may need to do this installation :
sudo apt-get install libpq-dev
```

## Launch the project
```bash
export POSTGRES_USER='youruser'
export POSTGRES_PASSWORD='yourpassword'
python3 run.py
```

## Documentation

- https://flask.palletsprojects.com/en/2.3.x/
- https://pypi.org/project/psycopg2/
