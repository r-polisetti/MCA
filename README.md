# ⏳ Countdown Events App

A minimal, and customizable countdown timer web app — perfect for tracking important events, milestones, or launches.

> Live Demo: [Click here to try it out 🚀](https://r-polisetti.github.io/MCA/)

---

## ✨ Features

- ✅ **Multiple countdowns** with titles and descriptions
- 🌗 **Dark mode toggle** (remembers your preference)
- 📊 **Live countdown** showing days, hours, minutes, and seconds
- 📈 **Progress bar** showing how far along each event is
- 🎨 **Color-coded event tiles**:
  - 🟢 Green: Plenty of time left
  - 🟡 Yellow: Halfway
  - 🔴 Red: Almost there!
- 💡 **Rotating motivational quotes**
- 🎉 Auto-updates every second
- 💾 Lightweight and **deployed using GitHub Pages**

---

## 📁 Project Structure

```plaintext
modc.github.io/
├── index.html          # Main app UI and logic
├── events.json         # Editable list of your events
├── preview.png         # (Optional) Social share image
└── README.md           # You're reading it!
```
---

## 📅 How to Add or Update Events
Open events.json

Add events in this format:

```json
[
  {
    "name": "Project Launch",
    "description": "Final release of the platform",
    "date": "2025-06-20T00:00:00",
    "startDate": "2025-06-01T00:00:00"
  }
]
```
date must be in full ISO format (e.g. YYYY-MM-DDTHH:mm:ss)
startDate is optional — if not given, current time is used.

---

## 🛠️ How to Run Locally
You can test the app on your own machine before pushing it:

```bash
# Start a local web server (Python 3)
python -m http.server
```
Then open: http://localhost:8000 in your browser
Or use Live Server in VS Code.

---

## 🌐 Deploying on GitHub Pages
Push your files to a GitHub repo (e.g. modc.github.io)

Go to Repo Settings > Pages

Set source as / (root) or main branch, and folder as /root

Done! Your site will be live at:

```php-template
https://<your-username>.github.io/<repo-name>
```
---

## 🧠 Credits & Inspiration
Built with 💙 using vanilla HTML, CSS, and JavaScript

Motivated by the need to track deadlines & goals in a beautiful way

UI inspired by minimalist productivity apps

---

## 📃 License
This project is open-source under the MIT License.

---

## Made with ❤️ by r-polisetti
