import os
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if SUPABASE_URL and SUPABASE_KEY:
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
else:
    supabase = None

def save_analysis_record(data):
    if not supabase:
        print("Supabase not configured, skipping save.")
        return
    try:
        supabase.table("stock_analysis").insert({
            "symbol": data["symbol"],
            "summary": data["summary"],
            "sentiment": data["sentiment"],
            "risk_level": data["risk_level"]
        }).execute()
    except Exception as e:
        print(f"Error saving to database: {e}")
