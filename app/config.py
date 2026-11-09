import os
from dotenv import load_dotenv

load_dotenv()

COHERE_API_KEY = os.getenv("COHERE_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX_NAME", "talkwise-mvp")
WHISPER_MODEL_SIZE = os.getenv("WHISPER_MODEL_SIZE", "base")

# embed-english-v3.0 (Cohere's embedding model) outputs 1024-dim vectors.
# This has to match the dimension your Pinecone index is created with,
# or upserting vectors later will fail with a dimension mismatch error.
EMBEDDING_DIMENSION = 1024