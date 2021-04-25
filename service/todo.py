import os

import cerver

from errors import *
from runtime import *

RUNTIME = runtime_from_string (os.environ.get ("RUNTIME"))

PORT = int (os.environ.get ("PORT"))

CERVER_RECEIVE_BUFFER_SIZE = int (os.environ.get ("CERVER_RECEIVE_BUFFER_SIZE"))
CERVER_TH_THREADS = int (os.environ.get ("CERVER_TH_THREADS"))
CERVER_CONNECTION_QUEUE = int (os.environ.get ("CERVER_CONNECTION_QUEUE"))

MONGO_APP_NAME = os.environ.get ("MONGO_APP_NAME")
MONGO_DB = os.environ.get ("MONGO_DB")
MONGO_URI = os.environ.get ("MONGO_URI")

PRIV_KEY = os.environ.get ("PRIV_KEY")
PUB_KEY = os.environ.get ("PUB_KEY")

ENABLE_USERS_ROUTES = os.environ.get ("ENABLE_USERS_ROUTES")
if (ENABLE_USERS_ROUTES == "TRUE"):
	ENABLE_USERS_ROUTES = True
else:
	ENABLE_USERS_ROUTES = False

def todo_config ():
	print ("RUNTIME: ", runtime_to_string (RUNTIME))

	print ("PORT: ", PORT)

	print ("CERVER_RECEIVE_BUFFER_SIZE: ", CERVER_RECEIVE_BUFFER_SIZE)
	print ("CERVER_TH_THREADS: ", CERVER_TH_THREADS)
	print ("CERVER_CONNECTION_QUEUE: ", CERVER_CONNECTION_QUEUE)

	print ("MONGO_APP_NAME: ", MONGO_APP_NAME)
	print ("MONGO_DB: ", MONGO_DB)
	print ("MONGO_URI: ", MONGO_URI)

	print ("PRIV_KEY: ", PRIV_KEY)
	print ("PUB_KEY: ", PUB_KEY)

	print ("ENABLE_USERS_ROUTES: ", ENABLE_USERS_ROUTES)

	todo_errors_init ()

def todo_end ():
	todo_errors_end ()
