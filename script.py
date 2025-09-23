import json
from datetime import datetime

def fetch_data():
    # Här skulle du normalt hämta från ett API
    data = {
        "message": "Hej från GitHub Actions!",
        "last_updated": datetime.utcnow().isoformat()
    }

    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    fetch_data()
