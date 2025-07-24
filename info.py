# Configuration variables (to be filled by user)
import os

# --- Bot Credentials ---
API_ID = int(os.environ.get("API_ID", "123456"))
API_HASH = os.environ.get("API_HASH", "your_api_hash")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "your_bot_token")

# --- MongoDB Connection ---
MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://...")

# --- Channels & Admins ---
AUTH_CHANNEL = int(os.environ.get("AUTH_CHANNEL", "-1001234567890"))      # Free user channel
PREMIUM_CHANNEL = int(os.environ.get("PREMIUM_CHANNEL", "-1009876543210")) # Premium channel
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001122334455"))
UPDATE_CHANNEL = int(os.environ.get("UPDATE_CHANNEL", "-1009988776655"))
OWNER_ID = int(os.environ.get("OWNER_ID", "123456789")) # Admin Telegram ID

# --- Bot Controls ---
IS_VERIFY = True       # Enable verification step
AUTO_REPLY = True      # Auto-response on any message
FLIRT_MODE = True      # Flirt mode toggle
PROTECTOR = True       # Profanity/anti-link toggle
LONG_IMDB_DESCRIPTION = True  # If True, long movie descriptions

# --- Deployment ---
PORT = os.environ.get("PORT", 8080)
HOST = os.environ.get("HOST", "0.0.0.0")

# --- Start Image & Premium Details ---
START_IMG = "https://telegra.ph/file/abcxyz123456.jpg"
UPI_IMAGE = "https://telegra.ph/file/your-upi-qr.jpg"
UPI_ID = "beard@ybl"

# --- Dynamic URLs ---
PYTHON_URL = "https://www.python.org/"
MONGO_URL_INFO = "https://www.mongodb.com/"
OWNER_INSTAGRAM = "https://instagram.com/beard"

# --- Premium Pricing ---
PREMIUM_PRICE = {
    "1_day": 1,
    "2_days": 2,
    "2_months": 60
}
