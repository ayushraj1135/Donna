import os
import json
import logging
from datetime import datetime
import google.generativeai as genai
from fastapi import FastAPI
from pydantic import BaseModel

# Setup Logging
logging.basicConfig(level=logging.INFO)

# 1. Setup the AI
genai.configure(api_key="AIzaSyBAYXmsKMFO3DmZhvnjHKTznrIHeag2eNE")

# Use 2.0-flash for the best 2026 performance
MODEL_NAME = 'gemini-2.5-flash'
model = genai.GenerativeModel(MODEL_NAME)

app = FastAPI()

class Message(BaseModel):
    text: str

# --- THE NOTEBOOK (Memory Functions) ---
MEMORY_FILE = "donna_memory.json"

def save_to_notebook(intent, details):
    """Saves a task or important note to a local JSON file."""
    entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "intent": intent,
        "details": details
    }
    # Append mode for the memory file
    with open(MEMORY_FILE, "a") as f:
        f.write(json.dumps(entry) + "\n")

def read_notebook():
    """Reads the last few entries to give Donna context."""
    if not os.path.exists(MEMORY_FILE):
        return "Your notebook is currently empty."

    with open(MEMORY_FILE, "r") as f:
        lines = f.readlines()
        # Get the last 5 things logged
        last_entries = [json.loads(line) for line in lines[-5:]]
        return json.dumps(last_entries)

@app.post("/analyze")
async def analyze(message: Message):
    current_time = datetime.now().strftime("%I:%M %p, %A, %B %d, %Y")

    # Donna looks at her notebook before answering
    past_context = read_notebook()

    prompt = f"""
    You are Donna, a loyal secretary and a close friend. 
    Current Time: {current_time}
    
    Your Notebook (Last 5 logs): {past_context}
    
    User Message: "{message.text}"
    
    PERSONALITY: Witty, helpful, organized. Talk like a friend.
    
    TASK:
    1. CATEGORIZE: CHAT, LOG_TASK, or CONTACT_THIRD_PARTY.
    2. RESPOND: If it's a LOG_TASK, confirm you've written it down. 
       If the user asks "What's on my list?", use the Notebook context above to answer.

    Return ONLY JSON:
    {{
      "intent": "THE_INTENT",
      "recipient": "Name or null",
      "details": "Summary of action",
      "response_to_user": "Your witty response"
    }}
    """

    try:
        response = model.generate_content(prompt)
        raw_text = response.text.strip().replace("```json", "").replace("```", "").strip()
        result = json.loads(raw_text)

        # --- EXECUTE THE NOTEBOOK LOGGING ---
        if result.get("intent") == "LOG_TASK":
            save_to_notebook("LOG_TASK", result.get("details"))
            # Add a small visual cue to the response
            result["response_to_user"] += " ✅ Logged in my notebook!"

        print(f"Success! Intent: {result.get('intent')}")
        return result

    except Exception as e:
        print(f"CRITICAL ERROR: {str(e)}")
        return {
            "intent": "CHAT",
            "response_to_user": f"Donna's brain is buffering. (Error: {str(e)[:40]})"
        }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)