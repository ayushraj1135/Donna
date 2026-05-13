import os
import json
import logging
from datetime import datetime
import google.generativeai as genai
from fastapi import FastAPI, Request
from pydantic import BaseModel

# Setup Logging
logging.basicConfig(level=logging.INFO)

# 1. Setup the AI
genai.configure(api_key="AIzaSyALWH-UWHpv1xv-NrRQgOEsTGK1RiADTTs")

# Use gemini-2.0-flash (2.5 does not exist yet)
MODEL_NAME = 'gemini-2.0-flash'
model = genai.GenerativeModel(MODEL_NAME)

app = FastAPI()

# --- THE NOTEBOOK (Memory Functions) ---
MEMORY_FILE = "donna_memory.json"

def save_to_notebook(intent, details):
    """Saves a task or important note to a local JSON file."""
    entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "intent": intent,
        "details": details
    }
    with open(MEMORY_FILE, "a") as f:
        f.write(json.dumps(entry) + "\n")

def read_notebook():
    """Reads the last few entries to give Donna context."""
    if not os.path.exists(MEMORY_FILE):
        return "The notebook is currently empty. No tasks scheduled."

    with open(MEMORY_FILE, "r") as f:
        lines = f.readlines()
        last_entries = [json.loads(line) for line in lines[-5:]]
        return json.dumps(last_entries)

@app.post("/bot/receive")
async def analyze(request: Request):
    # Flexible JSON handling to prevent 422 errors
    try:
        data = await request.json()
        logging.info(f"Incoming Request Body: {data}")
    except Exception:
        return {"error": "Invalid JSON format"}

    # Extract text from common keys (text, body, or message)
    user_text = data.get("text") or data.get("body") or data.get("message")

    if not user_text:
        logging.error("No text field found in incoming JSON")
        return {"intent": "CHAT", "response_to_user": "I received your message, but I couldn't read the text!"}

    current_time = datetime.now().strftime("%I:%M %p, %A, %B %d, %Y")
    past_context = read_notebook()

    # STRICT SECRETARY PERSONA PROMPT
    prompt = f"""
    ROLE: You are Donna, a professional, highly organized Personal Secretary.
    Your SOLE responsibility is managing the user's schedule, logging tasks, and coordinating with third parties.
    
    Current Time: {current_time}
    Your Notebook (Last 5 logs): {past_context}
    User Message: "{user_text}"
    
    STRICT BOUNDARIES:
    - You are a loyal secretary. If the user asks for trivia, jokes, or non-scheduling advice, politely redirect them to their tasks.
    - If a task involves someone else (e.g., "Tell Mom...", "Email the boss..."), use intent: CONTACT_THIRD_PARTY.
    - If user asks to clear everything, use intent: CLEAR_MEMORY.
    - You are witty and friendly, but always professional.

    TASK:
    1. CATEGORIZE: CHAT (only if schedule-related), LOG_TASK, CONTACT_THIRD_PARTY, or CLEAR_MEMORY.
    2. RESPOND: Confirm actions clearly. If retrieving from the Notebook, be precise.

    Return ONLY JSON:
    {{
      "intent": "THE_INTENT",
      "recipient": "Name or null",
      "details": "Summary of action",
      "response_to_user": "Your witty, professional response"
    }}
    """

    try:
        response = model.generate_content(prompt)
        raw_text = response.text.strip().replace("```json", "").replace("```", "").strip()
        result = json.loads(raw_text)

        # --- EXECUTE SECRETARY LOGIC ---
        if result.get("intent") == "CLEAR_MEMORY":
            if os.path.exists(MEMORY_FILE):
                os.remove(MEMORY_FILE)
            result["response_to_user"] = "Notebook cleared, boss. I'm ready for a fresh start! 🧹"

        elif result.get("intent") == "LOG_TASK":
            save_to_notebook("LOG_TASK", result.get("details"))
            result["response_to_user"] += " ✅ Logged."

        elif result.get("intent") == "CONTACT_THIRD_PARTY":
            result["response_to_user"] += " 📤 I'll get that message sent out immediately."

        print(f"Success! Intent: {result.get('intent')}")
        return result

    except Exception as e:
        logging.error(f"AI/JSON ERROR: {str(e)}")
        return {
            "intent": "CHAT",
            "response_to_user": "My systems are a bit crossed. Could you say that again?"
        }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)