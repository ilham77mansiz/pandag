import os

import sys

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())


class Var(object):
    LOGGER = True
    MONGO_URI = os.environ.get("MONGO_DB_URI", None)
    DB_URI = os.environ.get("DATABASE_URL", None)
    REDIS_URI = os.environ.get("REDIS_URI", None)
    REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD", None)
    REDISPASSWORD = os.environ.get("REDISPASSWORD", None)
    REDISHOST = os.environ.get("REDISHOST", None)
    REDISPORT = os.environ.get("REDISPORT", None)
    REDISUSER = os.environ.get("REDISUSER", None)
    DTABASE_URL = DB_URI
