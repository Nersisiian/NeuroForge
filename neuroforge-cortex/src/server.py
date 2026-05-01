from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn

app = FastAPI(title="NeuroForge Cortex", version="0.2.0")

# ????????? ??????? ? ?????? ????????? (??? ??????????)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class IntentRequest(BaseModel):
    text: str

class IntentResponse(BaseModel):
    action: str
    params: dict
    confidence: float

@app.post("/parse", response_model=IntentResponse)
async def parse_intent(req: IntentRequest):
    text = req.text.lower()
    if "report" in text or "?????" in text:
        return IntentResponse(action="generate_report", params={"type": "sales"}, confidence=0.95)
    elif "predict" in text or "???????" in text:
        return IntentResponse(action="predict", params={"model": "auto"}, confidence=0.92)
    else:
        return IntentResponse(action="unknown", params={"raw": text}, confidence=0.5)

class UIRequest(BaseModel):
    intent_id: str
    constraints: dict = {}

@app.post("/generate_ui")
async def generate_ui(req: UIRequest):
    return {
        "component_tree": {
            "root": "Dashboard",
            "children": [
                {"component": "IntentCard", "intent_id": req.intent_id},
                {"component": "LiveGraph3D", "dataSource": f"intent://{req.intent_id}"}
            ]
        },
        "assets": []
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
