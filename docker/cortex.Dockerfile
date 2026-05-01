FROM python:3.11-slim
WORKDIR /app
RUN pip install --upgrade pip
COPY pyproject.toml .
RUN pip install --no-cache-dir fastapi uvicorn[standard] pydantic transformers torch accelerate sentencepiece
COPY src/ src/
CMD ["uvicorn", "src.server:app", "--host", "0.0.0.0", "--port", "8000"]
