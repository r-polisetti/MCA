import os
import requests, json
from datetime import datetime

# Load secrets from env
BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

# Load goals
with open("goals.json", "r") as f:
    goals = json.load(f)

now = datetime.now()
summary = ["🎯 Good morning! Here's your goal countdown:\n"]

for goal in goals:
    goal_date = datetime.fromisoformat(goal["date"])
    days_left = (goal_date - now).days

    # Show countdown even if it's in the past
    if days_left > 0:
        summary.append(f"🚀 {goal['name']}: {days_left} day{'s' if days_left != 1 else ''} left")
    elif days_left == 0:
        summary.append(f"🔥 TODAY is the deadline for: {goal['name']}! Stay focused!")
    else:
        summary.append(f"⏳ {goal['name']}: {-days_left} day{'s' if days_left != -1 else ''} **past** deadline")

summary.append("\n💪 Keep pushing toward your goals!")
message = "\n".join(summary)

# Send to Telegram
url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
res = requests.post(url, json={"chat_id": CHAT_ID, "text": message})

if res.ok:
    print("✅ Message sent!")
else:
    print("❌ Failed:", res.text)
