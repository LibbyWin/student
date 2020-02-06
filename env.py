import os

os.environ.setdefault("MONGO_DBNAME", "StudentLife")
os.environ.setdefault("MONGO_URI", "mongodb+srv://LWin_01:01Libby@StudentLife-ldsrb.mongodb.net/StudentLife?retryWrites=true&w=majority")
os.environ["secret_key"] = "Secret"
COLLECTION_NAME = "StudentLife"

