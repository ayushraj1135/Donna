# Donna: Your AI-Driven Personal Secretary

**Donna** is a professional-grade virtual assistant project designed to act as a highly organized personal secretary. Built with a dual-service architecture, Donna bridges a **Java Spring Boot** gateway with a **Python FastAPI** intelligence core powered by **Google’s Gemini 2.0 Flash**.

Unlike basic chatbots, Donna is designed to manage your schedule, log tasks, coordinate with third parties, and utilize a persistent **PostgreSQL** database for long-term memory.

---

## 🚀 Core Features

*   **Intelligent Scheduling**: Uses Gemini 2.0 Flash to categorize user intent and manage complex scheduling logic.
*   **Secretary Persona**: Donna maintains a professional, organized, and witty personality, focusing strictly on productivity and coordination.
*   **Persistent Database Memory**: Utilizes a PostgreSQL backend to store historical logs, ensuring Donna remembers past context and user preferences.
*   **Third-Party Coordination**: Capable of drafting messages and managing communications with other people on your behalf.
*   **Conflict Resolution**: (Planned) Logic to prioritize urgent tasks and automatically suggest rescheduling for lower-priority events.

---

## 🛠️ Tech Stack

### **Gateway (Java)**
*   **Framework**: Spring Boot
*   **Responsibility**: Acts as the Webhook controller for Twilio, receiving WhatsApp messages and routing them to the Python brain.

### **Brain (Python)**
*   **Framework**: FastAPI
*   **AI Model**: Google Gemini 2.0 Flash
*   **Database**: PostgreSQL (via `psycopg2`)
*   **Responsibility**: Intent analysis, context retrieval, and executing secretary-specific logic.

---

## 📂 Project Structure

```text
Donna/
├── java-backend/
│   └── WebhookController.java  # Spring Boot REST Controller
├── python-brain/
│   ├── main.py                 # FastAPI & Gemini Logic
│   └── test_db.py              # Database Connection Utility
├── schema.sql                  # PostgreSQL Table Definitions
└── README.md
```

⚙️ Setup & Installation
1. Database Setup

Ensure PostgreSQL is installed and running. Run the following to initialize Donna's memory:
SQL
````
CREATE DATABASE donna_db;

CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    intent VARCHAR(50),
    details TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
````

2. Python Brain Configuration

   1. Install necessary libraries:
````
pip install fastapi uvicorn psycopg2-binary google-generativeai
````
    ii. Set your Gemini API Key and PostgreSQL credentials in `main.py`.

    iii. Start the server:
    uvicorn main:app --reload --port 8000

3. Java Gateway Configuration

Ensure the pythonUrl in WebhookController.java points to your running FastAPI instance.

Run the Spring Boot application.
