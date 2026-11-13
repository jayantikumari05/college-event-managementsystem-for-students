import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import requests
load_dotenv()
app=Flask(__name__)
API_KEY=os.getenv("GEMINI_API_KEY","").strip()
MODEL=os.getenv("GEMINI_MODEL","gemini-2.5-flash")
EVENTS=[
{"title":"Web Development Workshop","category":"Technical","date":"5 November 2026","time":"10:00 AM","venue":"Computer Lab 2","description":"Responsive web page and front-end development."},
{"title":"Inter-College Coding Challenge","category":"Technical","date":"12 November 2026","time":"9:30 AM","venue":"Seminar Hall","description":"Programming problems and collaboration."},
{"title":"Campus Cultural Fest","category":"Cultural","date":"18 November 2026","time":"4:00 PM","venue":"Main Auditorium","description":"Music, dance and student performances."},
{"title":"Sports Meet","category":"Sports","date":"22 November 2026","time":"8:00 AM","venue":"College Grounds","description":"Friendly sports competitions."},
{"title":"Career Readiness Talk","category":"Career","date":"28 November 2026","time":"11:00 AM","venue":"Lecture Hall 1","description":"Interview preparation and resume building."}]
def fallback(q):
 q=q.lower()
 if any(x in q for x in ["event","upcoming","available","list"]): return "Demo events:\n"+"\n".join(f"• {e['title']} — {e['date']} at {e['time']}, {e['venue']} ({e['category']})" for e in EVENTS)
 if any(x in q for x in ["register","registration","sign up"]): return "Use the Register for an Event form on this page. Enter your name, student ID, email, choose an event and submit. I cannot submit it for you."
 if any(x in q for x in ["venue","where","location"]): return "Event venues:\n"+"\n".join(f"• {e['title']}: {e['venue']}" for e in EVENTS)
 if any(x in q for x in ["date","when","time"]): return "Event schedules:\n"+"\n".join(f"• {e['title']}: {e['date']} at {e['time']}" for e in EVENTS)
 return "I can help with sample events and registration steps. Ask: What events are available?"
def ask_gemini(q,history):
 context="\n".join(f"{e['title']} | {e['category']} | {e['date']} | {e['time']} | {e['venue']} | {e['description']}" for e in EVENTS)
 contents=[]
 for item in history[-8:]:
  if isinstance(item,dict) and item.get("text"):
   contents.append({"role":"user" if item.get("role")=="user" else "model","parts":[{"text":str(item["text"])[:1200]}]})
 prompt=("You are CampusConnect Assistant. Answer only from this demo event data: "+context+". Explain how to use the registration form, but never claim you registered anyone, sent email, checked a live database, or verified seats. Say when information is unavailable.\nStudent question: "+q[:1200])
 contents.append({"role":"user","parts":[{"text":prompt}]})
 url=f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent"
 r=requests.post(url,params={"key":API_KEY},json={"contents":contents,"generationConfig":{"temperature":0.3,"maxOutputTokens":450}},timeout=30)
 r.raise_for_status()
 return r.json()["candidates"][0]["content"]["parts"][0]["text"].strip()
@app.get("/")
def home(): return render_template("index.html")
@app.post("/api/chat")
def chat():
 data=request.get_json(silent=True) or {};q=str(data.get("message","")).strip();history=data.get("history",[])
 if not q:return jsonify(error="Please enter a question."),400
 if len(q)>1200:return jsonify(error="Keep your question under 1,200 characters."),400
 if API_KEY:
  try:return jsonify(reply=ask_gemini(q,history),mode="gemini")
  except (requests.RequestException,KeyError,IndexError,TypeError,ValueError):return jsonify(reply=fallback(q)+"\n\n(Live AI unavailable; built-in help shown.)",mode="fallback")
 return jsonify(reply=fallback(q)+"\n\n(Add your Gemini API key to .env to enable live AI.)",mode="fallback")
if __name__=="__main__":app.run(debug=True)
