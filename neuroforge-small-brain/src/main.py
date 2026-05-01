from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI(title="NeuroForge Small Brain", version="0.1.0")

generator = pipeline("text-generation", model="gpt2", device=-1)

class IntentRequest(BaseModel):
    text: str

class IntentResponse(BaseModel):
    action: str
    params: dict

@app.post("/parse", response_model=IntentResponse)
async def parse_intent(req: IntentRequest):
    raw = req.text.lower()
    if "report" in raw or "отчёт" in raw:
        return IntentResponse(action="generate_report", params={"type": "sales"})
    elif "predict" in raw or "прогноз" in raw:
        return IntentResponse(action="predict", params={"model": "auto"})
    else:
        prompt = f"Extract structured intent from: {req.text}. Output JSON with keys action and params. Only JSON:"
        result = generator(prompt, max_length=100, num_return_sequences=1)[0]["generated_text"]
        return IntentResponse(action="unknown", params={"raw_output": result})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)