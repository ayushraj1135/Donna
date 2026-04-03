# Donna 🤖

Donna is a **WhatsApp-based AI personal task scheduler** inspired by *Donna Paulsen* from the TV show *Suits*.

Instead of using an app, users can simply **message Donna on WhatsApp**, and she will understand, organize, and schedule their tasks intelligently.

---

## 🚀 Features (Current)

* 📩 WhatsApp chatbot integration
* 🔗 Webhook-based backend using Spring Boot
* 🧠 Basic AI intent detection (FastAPI)
* 🌐 Public endpoint using ngrok
* 💬 Real-time message handling

---

## 🛠️ Tech Stack

### Backend

* Java (Spring Boot)

### AI Service

* Python (FastAPI)

### Messaging

* Twilio WhatsApp Sandbox

### Development Tools

* ngrok (for public URL tunneling)

---

## 🧠 How It Works

1. User sends a message on WhatsApp
2. Twilio forwards the message to the backend
3. Spring Boot processes the request
4. Message is sent to FastAPI for parsing
5. AI extracts intent (e.g., create/delete task)
6. Donna responds back on WhatsApp

---

## 📦 Project Structure

```
donna/
│
├── backend/        # Spring Boot application
├── donna-ai/       # FastAPI AI service
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```
git clone https://github.com/YOUR_USERNAME/donna-ai.git
cd donna-ai
```

---

### 2. Run Backend (Spring Boot)

* Open in IntelliJ
* Run `DonnaBackendApplication.java`
* Runs on:

```
http://localhost:8080
```

---

### 3. Run AI Service (FastAPI)

```
cd donna-ai
python -m uvicorn main:app --reload
```

* Runs on:

```
http://localhost:8000
```

---

### 4. Expose Backend (ngrok)

```
ngrok http 8080
```

* Copy HTTPS URL and add `/webhook`

---

### 5. Configure Twilio Sandbox

* Paste ngrok URL in:

    * **WHEN A MESSAGE COMES IN**
* Method: POST

---

### 6. Test

Send a WhatsApp message:

```
Hello Donna
```

---

## 🔥 Future Plans

* 📅 Smart task scheduling algorithm
* 🗄️ Database integration (PostgreSQL)
* ⏱️ Priority-based scheduling
* 🔄 Dynamic rescheduling ("do this now")
* 📆 Google Calendar integration
* 🧠 Advanced NLP (spaCy / transformers)

---

## 💡 Vision

Donna is not just a chatbot.

The goal is to build a **proactive personal assistant** that:

* Understands your tasks
* Plans your time intelligently
* Feels like a real human assistant

---

## 👨‍💻 Author

**Ayush Raj**
Computer Science Student | Music Producer | Builder

---

## ⭐ Contribute

This is an evolving project. Contributions, ideas, and feedback are welcome!

---

## ⚠️ Note

This project is currently in development and uses **Twilio WhatsApp Sandbox** for testing purposes.

---

## 🔥 Inspired By

* *Suits* — Donna Paulsen
* AI productivity tools like Motion & Reclaim

---
