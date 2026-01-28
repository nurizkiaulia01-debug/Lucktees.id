import json
import os
from difflib import SequenceMatcher

# =====================
# LOAD FAQ
# =====================
def load_faq():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(base_dir, "faq_toko.json")

    if not os.path.exists(json_path):
        print("❌ faq_toko.json TIDAK DITEMUKAN")
        return []

    try:
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)

            if not isinstance(data, list):
                print("❌ Format JSON harus LIST")
                return []

            print(f"✅ FAQ berhasil dimuat: {len(data)} data")
            return data

    except Exception as e:
        print("❌ ERROR LOAD FAQ:", e)
        return []


faq_data = load_faq()

# =====================
# SIMILARITY
# =====================
def similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()


# =====================
# BOT LOGIC
# =====================
def get_bot_reply(user_text):
    user_text = user_text.lower().strip()

    if not user_text:
        return "Silakan ketik pertanyaan Anda 😊"

    if not faq_data:
        return "Maaf, data FAQ belum tersedia."

    best_score = 0
    best_answer = None

    for item in faq_data:
        keywords = item.get("keywords", [])
        answer = item.get("answer", "")

        # ⛔ PROTEKSI PENTING
        if not isinstance(keywords, list):
            continue

        for keyword in keywords:
            score = similarity(user_text, keyword.lower())
            print(f"[DEBUG] '{user_text}' vs '{keyword}' = {score}")

            if score > best_score:
                best_score = score
                best_answer = answer

    if best_score >= 0.45 and best_answer:
        return best_answer

    return (
        "Mohon maaf, kami belum memahami pertanyaan Anda.\n"
        "Silakan tanyakan tentang jam operasional, produk, alamat, atau cara pemesanan."
    )
