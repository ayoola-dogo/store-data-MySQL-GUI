import os
import dotenv
dotenv.load_dotenv('.env')

# create dictionary to hold connection info
dbConfig = {
    'user': os.environ['user'], # use your admin name
    'password': os.environ['password'],
    'host': '127.0.0.1'  # IP address of localhost
}
