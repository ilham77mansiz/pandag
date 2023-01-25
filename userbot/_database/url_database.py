# Copyright (C) 2021-2022 TeamUltroid
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/TeamUltroid/pyUltroid/blob/main/LICENSE>.

# Recode by @robotrakitangakbagus, @diemmmmmmmmmm
# Import PandaX_Userbot <https://github.com/ilhammansiz/PandaX_Userbot>
# t.me/PandaUserbot & t.me/TeamSquadUserbotSupport

import logging
import ast
import os
import sys

run_as_module = False

def where_hosted():
    if os.getenv("DYNO"):
        return "heroku"
    if os.getenv("RAILWAY_STATIC_URL"):
        return "railway"
    if os.getenv("OKTETO_TOKEN"):
        return "okteto"
    if os.getenv("KUBERNETES_PORT"):
        return "qovery | kubernetes"
    if os.getenv("RUNNER_USER") or os.getenv("HOSTNAME"):
        return "github actions"
    if os.getenv("ANDROID_ROOT"):
        return "termux"
    return "[ local ]"


HOSTED_ON = where_hosted()

LOGS = logging.getLogger("PandaUserbot")
loop = None

if run_as_module:
    from ._var import Var

from ._var import Var



Redis = MongoClient = Database = None
if (Var.REDIS_URI or Var.REDISHOST):
    try:
        from redis import Redis
    except ImportError:
        LOGS.info("Installing 'redis' for database.")
        os.system("pip3 install -q redis hiredis")
        from redis import Redis
elif Var.MONGO_URI:
    try:
        from pymongo import MongoClient
    except ImportError:
        LOGS.info("Installing 'pymongo' for database.")
        os.system("pip3 install -q pymongo[srv]")
        from pymongo import MongoClient
else:
    try:
        from .localdb import Database
    except ImportError:
        LOGS.info("Using local file as database.")
        os.system("pip3 install -q localdb.json")
        from localdb import Database


class _BaseDatabase:
    def __init__(self, *args, **kwargs):
        self._cache = {}

    def getdb(self, key):
        if key in self._cache:
            return self._cache[key]
        value = self._get_data(key)
        self._cache.update({key: value})
        return value

    def re_cache(self):
        self._cache.clear()
        for key in self.keys():
            self._cache.update({key: self.getdb(key)})

    def ping(self):
        return "Active"

    @property
    def usage(self):
        return 0

    def keys(self):
        return []

    def deldb(self, key):
        if key in self._cache:
            del self._cache[key]
        self.delete(key)
        return True

    def _get_data(self, key=None, data=None):
        if key:
            data = self.get(str(key))
        if data:
            try:
                data = ast.literal_eval(data)
            except BaseException:
                pass
        return data

    def setdb(self, key, value):
        value = self._get_data(data=value)
        self._cache[key] = value
        return self.set(str(key), str(value))

    def rename(self, key1, key2):
        _ = self.getdb(key1)
        if _:
            self.deldb(key1)
            self.setdb(key2, _)
            return 0
        return 1



class MongoDB(_BaseDatabase):
    def __init__(self, key, dbname="DatabaseCute"):
        self.dB = MongoClient(key, serverSelectionTimeoutMS=5000)
        self.db = self.dB[dbname]
        super().__init__()

    def __repr__(self):
        return f"<Panda.MonGoDB\n -total_keys: {len(self.keys())}\n>"

    @property
    def name(self):
        return "MongoDB"

    @property
    def usage(self):
        return self.db.command("dbstats")["dataSize"]

    def ping(self):
        if self.dB.server_info():
            return "MongoTrue"

    def keys(self):
        return self.db.list_collection_names()

    def setdb(self, key, value):
        if key in self.keys():
            self.db[key].replace_one({"_id": key}, {"value": str(value)})
        else:
            self.db[key].insert_one({"_id": key, "value": str(value)})
        self._cache.update({key: value})
        return True

    def delete(self, key):
        self.db.drop_collection(key)

    def get(self, key):
        if x := self.db[key].find_one({"_id": key}):
            return x["value"]

    def flushall(self):
        self.dB.drop_database("DatabaseCute")
        self._cache.clear()
        return True



class RedisDB(_BaseDatabase):
    def __init__(
        self,
        host,
        port,
        password,
        platform="",
        logger=LOGS,
        *args,
        **kwargs,
    ):
        if host and ":" in host:
            spli_ = host.split(":")
            host = spli_[0]
            port = int(spli_[-1])
            if host.startswith("http"):
                logger.error("Your REDIS_URI should not start with http !")
                import sys

                sys.exit()
        elif not host or not port:
            logger.error("Port Number not found")
            import sys

            sys.exit()
        kwargs["host"] = host
        kwargs["password"] = password
        kwargs["port"] = port

        if platform.lower() == "qovery" and not host:
            var, hash_, host, password = "", "", "", ""
            for vars_ in os.environ:
                if vars_.startswith("QOVERY_REDIS_") and vars.endswith("_HOST"):
                    var = vars_
            if var:
                hash_ = var.split("_", maxsplit=2)[1].split("_")[0]
            if hash:
                kwargs["host"] = os.environ(f"QOVERY_REDIS_{hash_}_HOST")
                kwargs["port"] = os.environ(f"QOVERY_REDIS_{hash_}_PORT")
                kwargs["password"] = os.environ(f"QOVERY_REDIS_{hash_}_PASSWORD")
        self.db = Redis(**kwargs)
        self.set = self.db.set
        self.get = self.db.get
        self.keys = self.db.keys
        self.delete = self.db.delete
        super().__init__()

    @property
    def name(self):
        return "RedisDB"

    @property
    def usage(self):
        return sum(self.db.memory_usage(x) for x in self.keys())


class LocalDB(_BaseDatabase):
    def __init__(self):
        self.db = Database("panda")
        super().__init__()

    def keys(self):
        return self._cache.keys()

    def __repr__(self):
        return f"<Panda.LocalDB\n -total_keys: {len(self.keys())}\n>"


def DatabaseCute():
    _er = False
    try:
        if Redis:
            return RedisDB(
                host=Var.REDIS_URI or Var.REDISHOST,
                password=Var.REDIS_PASSWORD or Var.REDISPASSWORD,
                port=Var.REDISPORT,
                platform=HOSTED_ON,
                decode_responses=True,
                socket_timeout=5,
                retry_on_timeout=True,
            )
        if MongoClient:
            return MongoDB(Var.MONGO_URI)
    except BaseException as err:
        LOGS.exception(err)
        _er = True
    if not _er:
        LOGS.critical(
            "No DB requirement fullfilled!\nPlease install redis, mongo or sql dependencies...\nTill then using local file as database."
        )
    if HOSTED_ON == "termux":
        return LocalDB()
    exit()
