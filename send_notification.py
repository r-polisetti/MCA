import requests, json
from datetime import datetime

# Load secrets from env
BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

# Load events
with open("events.json", "r") as f:
    events = json.load(f)

now = datetime.now()
summary = ["📅 Good morning! Here's your event countdown:\n"]

for ev in events:
    event_date = datetime.fromisoformat(ev["date"])
    days_left = (event_date - now).days

    if days_left > 0:
        summary.append(f"🎯 {ev['name']}: {days_left} day{'s' if days_left != 1 else ''} left")
    elif days_left == 0:
        summary.append(f"🚨 TODAY is the day for: {ev['name']} 🎉")
    else:
        summary.append(f"✅ {ev['name']} already passed")

summary.append("\n🔥 Let's stay focused!")
message = "\n".join(summary)

# Send to Telegram
url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
res = requests.post(url, json={"chat_id": CHAT_ID, "text": message})

if res.ok:
    print("✅ Message sent!")
else:
    print("❌ Failed:", res.text)
