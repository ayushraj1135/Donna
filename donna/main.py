from fastapi import FastAPI

app = FastAPI()

@app.post("/parse")
def parse(data: dict):
    message = data["message"].lower()

    if "delete" in message:
        intent = "DELETE_TASK"
    elif "now" in message:
        intent = "RESCHEDULE_NOW"
    else:
        intent = "CREATE_TASK"

    return {
        "intent": intent,
        "original": message
    }