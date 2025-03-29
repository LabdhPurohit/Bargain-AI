from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from negotiation_bot import get_bot_response
import uvicorn

app = FastAPI()

class UserMessage(BaseModel):
    message: str

@app.post("/chat/")
async def chat(user_message: UserMessage):
    try:
        response = get_bot_response(user_message.message)
        return {"shopkeeper": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Directly run FastAPI using Python command
def start():
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)

if __name__ == "__main__":
    start()
