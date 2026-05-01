from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

app = FastAPI(title="NeuroForge Cortex", version="0.3.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Загружаем TinyLlama – лёгкая, но реальная LLM
model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float16,
    device_map="auto",
    low_cpu_mem_usage=True
)
generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

class IntentRequest(BaseModel):
    text: str

class IntentResponse(BaseModel):
    action: str
    params: dict
    confidence: float

@app.post("/parse", response_model=IntentResponse)
async def parse_intent(req: IntentRequest):
    prompt = f"<|system|>Extract user intent as JSON with 'action' and 'params'. Only JSON.<|user|>{req.text}<|assistant|>"
    output = generator(prompt, max_new_tokens=100, temperature=0.1, do_sample=True)[0]['generated_text']
    # Простейший парсер JSON из вывода (можно доработать)
    try:
        import json
        data = json.loads(output.split("{")[1].split("}")[0] + "}")
        return IntentResponse(action=data.get("action", "unknown"), params=data.get("params", {}), confidence=0.9)
    except:
        return IntentResponse(action="unknown", params={"raw": output}, confidence=0.5)

class UIRequest(BaseModel):
    intent_id: str
    constraints: dict = {}

@app.post("/generate_ui")
async def generate_ui(req: UIRequest):
    # Заглушка для UI
    return {
        "component_tree": {"root": "Dashboard", "children": [{"component": "IntentCard", "intent_id": req.intent_id}]},
        "assets": []
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
