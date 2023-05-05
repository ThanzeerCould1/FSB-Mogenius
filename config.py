#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5091442931:AAFpZ0RwdMRhxUx13eOV30ENJ6TfyC_D66o")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "5494681"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "7a274228068e92e24de55cd254f9c2cd")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001646714416"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1482016419"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://thanzeer:thanzeer@cluster0.bkv6h.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "filesharexbot")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001685129077"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nI can store private files in Specified Channel and other users can access it from special link.")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "1482016419").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "<b>⚠️ {mention} YOU ARE NOT SUBSCRIBED OUR CHANNEL ⚠️  🤗 JOIN ON OUR CHANNEL TO GET NOW ✅  ⚠️ താങ്കൾ ഞങ്ങളുടെ ചാനൽ സബ്സ്ക്രൈബ് ചെയ്തിട്ട് ഇല്ല!! ⚠️  🤗 ആദ്യം ഞങ്ങളുടെ ചാനലിൽ ജോയിൻ ചെയ്യുക എങ്കിൽ മാത്രമേ നിങ്ങൾക്ക് വേണ്ടത് കിട്ടുകയുള്ളൂ ✅</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>{previouscaption}</b>")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", "True")

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot!"

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
