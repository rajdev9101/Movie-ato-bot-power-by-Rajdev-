# Main bot file
import os
from pyrogram import Client
from config.info import BOT_TOKEN, API_ID, API_HASH, PORT, HOST
from database.mongodb import db
from handlers.start import register_start
from handlers.about import register_about
from handlers.movie_search import register_search_handlers
from handlers.premium import register_premium
from handlers.settings import register_settings
from handlers.deleter import register_deleter
from handlers.logger import register_logger
from handlers.indexer import register_indexer
from handlers.updater import register_updater
from handlers.shortlink import register_shortlink
from handlers.filters import register_filters

app = Client(
    "riya_bot",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH,
)

# Register handlers
register_start(app)
register_about(app)
register_search_handlers(app)
register_premium(app)
register_settings(app)
register_deleter(app)
register_logger(app)
register_indexer(app)
register_updater(app)
register_shortlink(app)
register_filters(app)

@app.on_ready()
async def startup(cli: Client):
    print("🤖 Riya Bot is now online and ready!")
    await db.connect()

@app.on_disconnect()
async def shutdown(cli: Client):
    print("⚠️ Riya Bot is going offline...")
    await db.disconnect()

def main():
    if os.environ.get("WEBHOOK", "false") == "true":
        app.run(webhook=True, host=HOST, port=int(PORT))
    else:
        app.run()

if __name__ == "__main__":
    main()
  
