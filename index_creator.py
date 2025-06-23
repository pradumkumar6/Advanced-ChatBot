from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv
import os

# Load env variables from .env
load_dotenv()

# Get values
api_key = os.getenv("PINECONE_API_KEY")

# Initialize Pinecone client
pc = Pinecone(api_key=api_key)

# Create index if not exists
if "euriai-chat-memory-1536" not in pc.list_indexes().names():
    pc.create_index(
        name="euriai-chat-memory-1536",
        dimension=1536,
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        )
    )
    print("✅ Index created: euriai-chat-memory-1536")
else:
    print("ℹ️ Index already exists: euriai-chat-memory-1536")
