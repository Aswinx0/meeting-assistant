# Talkwise AI

An AI-powered meeting assistant (proof of concept). It turns a meeting recording into a searchable knowledge base, so you can ask "what did we decide about the budget?" and get an answer grounded in the transcript.

## Architecture

```
Meeting audio -> Whisper (STT) -> Chunking -> Cohere embeddings -> Pinecone
Question -> Embed -> Pinecone search -> Cohere rerank -> LLM -> Answer
```

Served through a FastAPI backend with an ingest endpoint and a query endpoint.

## Tech stack

- **Speech-to-text:** faster-whisper (Whisper)
- **Embeddings, reranking, LLM:** Cohere (`embed-english-v3.0`, `rerank-english-v3.0`, `command-r-plus`)
- **Vector database:** Pinecone
- **Backend:** Python, FastAPI

## Status

Core pipeline in active development. The transcription service is written; chunking, retrieval and the API endpoints are next. Multimodal (vision-language model) and agent tooling are planned extensions.

## Setup

Requires Python 3.11+ and ffmpeg.

```bash
python -m venv venv
venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Create a `.env` file:

```
COHERE_API_KEY=your_cohere_key
PINECONE_API_KEY=your_pinecone_key
PINECONE_INDEX_NAME=talkwise-mvp
WHISPER_MODEL_SIZE=base
```