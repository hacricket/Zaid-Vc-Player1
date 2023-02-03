## What's up Kangers
## Don't Kang without Creadits else I will rape your mom

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}

SESSION_NAME = getenv("BQEdBa8ARD7SGKdG1BzKHP6pfP-4P6RgwT3gYpywgzElYoAwaODyo-WhqnPWV2UfqVPhSTduZV-RW_DIOTS_FUnyuY5dLBGPePsFuY5l0QAccILiemg8isSVdfei9v_hbmi7HlhFSh-M_vJZh7VBM2fEeFNbE_cE1yr5At3vm_Wg86txyUFVcH7Wtoi3p_FrL8L8qUY_s-S210GUigHh5CYmTSe3YAEHg9_laBT3_DVB8YYM9nZreyHJiSUmtVDfjf002lRN0oeJw03QASaLU29OczAk-o62zPzW8Nj2_OoJFbCXBzVlq6mmRW9GmsykTnyUmTx3hEk7V0XSxU7bL4B0Uw-j_wAAAAB5-PZiAA")

if str(getenv("STRING_SESSION2")).strip() == "":
    SESSION2 = str(None)
else:
    SESSION2 = str(getenv("STRING_SESSION2"))

if str(getenv("STRING_SESSION3")).strip() == "":
    SESSION3 = str(None)
else:
    SESSION3 = str(getenv("STRING_SESSION3"))

if str(getenv("STRING_SESSION4")).strip() == "":
    SESSION4 = str(None)
else:
    SESSION4 = str(getenv("STRING_SESSION4"))

if str(getenv("STRING_SESSION5")).strip() == "":
    SESSION5 = str(None)
else:
    SESSION5 = str(getenv("STRING_SESSION5"))

BOT_TOKEN = getenv("BOT_TOKEN", "6051630839:AAGJ0uToVPTzFQnA5-paIUG79052z7aMB9Q")
BOT_NAME = getenv("BOT_NAME", "SLC Group Streaming")

API_ID = int(getenv("API_ID", "18679215"))
API_HASH = getenv("API_HASH", "09849f9f1481edfb639ed45b80a01991")
MONGO_DB_URL = getenv("MONGO_DB_URL", "mongodb+srv://zaidadi:adi@2008@cluster0.jibkvbp.mongodb.net/?retryWrites=true&w=majority")
OWNER_NAME = getenv("OWNER_NAME", "SLCgroup")
OWNER_USERNAME = getenv("OWNER_USERNAME", "www_SL_Cricket_com")
ALIVE_NAME = getenv("ALIVE_NAME", "SLcricket")
BOT_USERNAME = getenv("BOT_USERNAME", "SLC_Streaming_Group_Bot")
OWNER_ID = getenv("OWNER_ID", "2046359138")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Avenger_stream")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "www_SL_Cricket_com")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "SL_cricket_news")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "2046359138").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/edb7798e5e27dd5f948c7.jpg")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/b6c80defdb1cb8f992370.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "600"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/ITZ-ZAID/Zaid-Vc-Player")
PLAY_IMG = getenv("PLAY_IMG", "https://telegra.ph/file/10b1f781170b1e1867f68.png")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/b95c13eef1ebd14dbb458.png")
CMD_IMG = getenv("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
VIDEO_IMG = getenv("VIDEO_IMG", "https://telegra.ph/file/6213d2673486beca02967.png")
SKIP_IMG = getenv("SKIP_IMG", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
NEXT_IMG = getenv("NEXT_IMG", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
HEROKU_MODE = getenv("HEROKU_MODE", None)
