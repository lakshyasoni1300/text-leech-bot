# SudoR2spr WOODcraft
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os

API_ID    = os.environ.get("API_ID", "29640188")
API_HASH  = os.environ.get("API_HASH", "e470abc84a3bc445997ee4ea5be87deb")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6387010477:AAHMA84X8bn-qJWyw5omeDyVEp4KoJ858kg") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set

