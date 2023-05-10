# getenv для того чтобы достать значение из .env
from os import getenv

# load_dotenv() для того чтобы связвть config с .env
from dotenv import load_dotenv
load_dotenv()

TOKEN = getenv("TOKEN")
ADMIN = getenv("ADMIN_USER")


PGHOST = getenv("PGHOST")
PGDATABASE = getenv("PGDATABASE")
PGUSER = getenv("PGUSER")
PGPASSWORD = getenv("PGPASSWORD")
PGPORT = getenv("PGPORT")


IMAGE = [
    "source/image/img1.jpg",
    "source/image/img2.jpeg",
    "source/image/img3.jpeg",
    "source/image/img4.jpg",
    "source/image/img5.jpg",
]