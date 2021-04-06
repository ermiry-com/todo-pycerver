import os

import cerver

from runtime import *

RUNTIME = RUNTIME_TYPE_NONE

PORT = 5000

CERVER_RECEIVE_BUFFER_SIZE = cerver.CERVER_DEFAULT_RECEIVE_BUFFER_SIZE
CERVER_TH_THREADS = cerver.CERVER_DEFAULT_POOL_THREADS
CERVER_CONNECTION_QUEUE = cerver.CERVER_DEFAULT_CONNECTION_QUEUE

MONGO_APP_NAME = None
MONGO_DB = None
MONGO_URI = None

PRIV_KEY = None
PUB_KEY = None

def todo_init ():
	global RUNTIME

	global PORT

	global CERVER_RECEIVE_BUFFER_SIZE
	global CERVER_TH_THREADS
	global CERVER_CONNECTION_QUEUE

	global MONGO_APP_NAME
	global MONGO_DB
	global MONGO_URI

	global PRIV_KEY
	global PUB_KEY

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
