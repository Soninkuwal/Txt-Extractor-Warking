"""
from os import getenv


API_ID = int(getenv("API_ID", "22215080"))
API_HASH = getenv("API_HASH", "6ab80ad5d78fee18fdd9b909edfbafd5")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = int(getenv("OWNER_ID", "7841292070"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7841292070 7491167754").split()))
MONGO_URL = getenv("MONGO_DB", "mongodb+srv://daxxop:daxxop@daxxop.dg3umlc.mongodb.net/?retryWrites=true&w=majority")

CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002461666553"))
PREMIUM_LOGS = int(getenv("PREMIUM_LOGS", "-1002461666553"))

"""
#




# --------------M----------------------------------

import os
from os import getenv
# ---------------R---------------------------------
API_ID = os.environ.get("API_ID")
# ------------------------------------------------
API_HASH = os.environ.get("API_HASH")
# ----------------D--------------------------------
BOT_TOKEN = os.environ.get("BOT_TOKEN")
# -----------------A-------------------------------
BOT_USERNAME = os.environ.get("BOT_USERNAME")
# ------------------X------------------------------
OWNER_ID = os.environ.get("OWNER_ID")
# ------------------X------------------------------

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
# ------------------------------------------------
CHANNEL_ID = os.environ.get("CHANNEL_ID")
# ------------------------------------------------
MONGO_URL = os.environ.get("MONGO_URL")
# -----------------------------------------------
PREMIUM_LOGS = os.environ.get("PREMIUM_LOGS")

