# CampusConnect AAT-2 AI Chatbot Integration

This is the AAT-1 CampusConnect event portal with its original event browsing, filtering, registration, cancellation and localStorage functionality retained, plus a Flask/Gemini chatbot.

## Run on Windows
1. Install Python 3.10+.
2. Open this folder in VS Code and run:
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
```
3. Put your own Gemini API key in `.env`. Never upload `.env` to GitHub.
4. Run `python app.py` and open `http://127.0.0.1:5000`.

The browser sends questions to Flask `/api/chat`; Flask adds the sample event context and calls Gemini. If no key is configured or the API fails, built-in FAQ responses are shown.

## Limitations
The event data is sample data and is duplicated in `app.py` and the JavaScript `EVENTS` array; keep both synchronized. Registrations remain in browser localStorage and are not sent to a shared database. The chatbot explains registration but cannot register or cancel for a student. GitHub Pages cannot run Flask; deploy the backend separately for a public live chatbot.
