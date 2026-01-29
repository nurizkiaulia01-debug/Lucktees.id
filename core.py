import json
import os
from difflib import SequenceMatcher

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(BASE_DIR, "faq_toko.json")

def load_faq():
    if not os.path.exists(JSON_PATH):
        return []

    try:
        with open(JSON_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
    except:
        pass

    return []

def similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()

def get_bot_reply(user_text):
    user_text = (user_text or "").lower().strip()

    if not user_text:
        return "Silakan ketik pertanyaan Anda 😊"

    faq_data = load_faq()   # ⬅️ LOAD DI SINI (AMAN)

    if not faq_data:
        return "Maaf, data FAQ belum tersedia."

    best_score = 0
    best_answer = None

    for item in faq_data:
        keywords = item.get("keywords", [])
        answer = item.get("answer", "")

        if not isinstance(keywords, list):
            continue

        for keyword in keywords:
            score = similarity(user_text, keyword.lower())
            if score > best_score:
                best_score = score
                best_answer = answer

    if best_score >= 0.45 and best_answer:
        return best_answer

    return (
        "Mohon maaf, kami belum memahami pertanyaan Anda.\n"
        "Silakan tanyakan tentang jam operasional, produk, alamat, atau cara pemesanan."
    )
