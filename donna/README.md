# 👩‍💼 Donna: Persona-Driven AI Secretary

**Donna** is a sophisticated personal assistant backend built with **FastAPI** and **Google Gemini 2.0 Flash**. Unlike standard chatbots, Donna is designed with a specific personality—a loyal secretary and a close friend—capable of managing tasks, recognizing user intent, and maintaining a persistent "Notebook" of your activities.

---

## 🌟 Core Capabilities

* **Intent Classification**: Dynamically categorizes incoming text into `CHAT`, `LOG_TASK`, `CONTACT_THIRD_PARTY`, or `CLEAR_MEMORY`.
* **Persistent Notebook**: Features a local JSON-based memory system (`donna_memory.json`) that allows Donna to remember and recall your tasks across sessions.
* **Temporal Intelligence**: Injects real-time date and time metadata so Donna is always aware of the current context (e.g., race results, deadlines, and current year events).
* **Witty Persona**: Optimized system prompting ensures Donna communicates with a helpful, organized, and friendly tone.

---

## 🛠️ Technical Architecture

* **Runtime**: Python 3.10+
* **API Framework**: FastAPI (Asynchronous)
* **AI Engine**: Google Generative AI (Gemini 2.0 Flash)
* **Web Server**: Uvicorn
* **Data Persistence**: Flat-file JSON Storage

---

## 🚀 Getting Started

### 1. Installation
Clone the repository and install the required Python packages:
```bash
git clone [https://github.com/your-username/donna-ai-secretary.git](https://github.com/your-username/donna-ai-secretary.git)
cd donna-ai-secretary
pip install fastapi uvicorn google-generativeai pydantic
```
### 2. Configuration
Ensure you have a valid Google AI Studio API Key. Replace the placeholder in main.py:
Python
````
genai.configure(api_key="YOUR_GEMINI_API_KEY")
````

### 3. Launching the Backend

Run the server using Uvicorn:
````
python main.py
````
The API will be available at `http://127.0.0.1:8000`.

## 📡 API Usage
`POST /analyze`

Processes user messages and returns structured JSON instructions.

### Request Body (JSON):
````
{
"text": "Donna, remind me to check the Japanese GP standings tonight."
}
````
### Successful Response:

````
{
"intent": "LOG_TASK",
"recipient": null,
"details": "Check Japanese GP standings tonight",
"response_to_user": "I've got you! I've added that to your list. ✅ Logged in my notebook!"
}
````

## 🧠 Memory Logic

Donna maintains a sliding window of memory. Every request includes the last 5 entries from donna_memory.json, enabling her to answer questions like:

    "Donna, what did I tell you to remind me about earlier?"

