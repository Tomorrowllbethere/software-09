import configparser
from mongoengine import connect


config = configparser.ConfigParser()
config.read('config.ini')

mongo_user = config.get('DB', 'user')
mongodb_pass = config.get('DB', 'pass')
db_name = config.get('DB', 'db_name')
domain = config.get('DB', 'domain')

# # connect to cluster on AtlasDB with connection string
# uri=f"mongodb+srv://{mongo_user}:{mongodb_pass}@{domain}/{db_name}?retryWrites=true&w=majority&appName=Fantom"

# # Create a new client and connect to the server
# client = MongoClient(uri, server_api=ServerApi('1'))

def connect_db():
    connect(
        host=f"""mongodb+srv://{mongo_user}:{mongodb_pass}@{domain}/{db_name}?retryWrites=true&w=majority&appName=Fantom""",
        ssl=True
    )
    if connect:
        print("Pinged your deployment. You successfully connected to MongoDB!")
if __name__=="__main__":

    connect_db()
# Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)
