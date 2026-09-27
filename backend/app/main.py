from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="AI Customer Support API",
    description="REST API for an AI-powered customer support application",
    version="1.0.0"
)


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    response: str


@app.get("/")
def root():
    return {
        "message": "AI Customer Support API is running"
    }


@app.post("/api/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    message = request.message

    response = (
        f"Thank you for contacting customer support. "
        f"We received your message: '{message}'"
    )

    return ChatResponse(response=response)
