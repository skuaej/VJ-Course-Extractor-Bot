# Don't Remove Credit Tg - @VJ_Bots
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01

import os

api_id = int(os.environ.get("API_ID", "27479878"))
api_hash = os.environ.get("API_HASH", "05f8dc8265d4c5df6376dded1d71c0ff")
bot_token = os.environ.get("BOT_TOKEN", "8963099680:AAFaMhMz4XtUtlgE04G6OFW9AvM-v19nG2o")
auth_users = [int(x.strip()) for x in os.environ.get("AUTH_USERS", "8827902968").split(",") if x.strip().isdigit()]

if not api_id: raise ValueError("Set API_ID env var!")
if not api_hash: raise ValueError("Set API_HASH env var!")
if not bot_token: raise ValueError("Set BOT_TOKEN env var!")
if not auth_users: raise ValueError("Set AUTH_USERS env var!")

# Don't Remove Credit Tg - @VJ_Bots
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
