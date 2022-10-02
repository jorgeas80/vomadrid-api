import os

# Scheme: "postgres+psycopg2://<USERNAME>:<PASSWORD>@<IP_ADDRESS>:<PORT>/<DATABASE_NAME>"
DATABASE_URI = f'postgresql+psycopg2://{os.environ["DBUSER"]}:{os.environ["DBPASSWORD"]}@{os.environ["DBHOST"]}:{os.environ["DBPORT"]}/{os.environ["DBNAME"]}'
