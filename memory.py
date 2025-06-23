# memory.py (updated for latest Pinecone SDK)
import os
from dotenv import load_dotenv
from pinecone import Pinecone
from euriai.langchain_embed import EuriaiEmbeddings

# Load environment variables
load_dotenv()

# Get Pinecone config
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_INDEX = os.getenv("PINECONE_INDEX")

# Init Pinecone and connect to index
pc = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index(PINECONE_INDEX)

# Init Euriai Embeddings
embedding_client = EuriaiEmbeddings(api_key=os.getenv("EURIAI_API_KEY"))

def store_message(session_id, message, reply):
    vec = embedding_client.embed_query(message)
    index.upsert(vectors=[
        {
            "id": f"{session_id}-{hash(message)}",
            "values": vec,
            "metadata": {
                "session_id": session_id,
                "message": message,
                "reply": reply
            }
        }
    ])

def fetch_session_history(session_id):
    query_vec = embedding_client.embed_query("memory")
    result = index.query(
        vector=query_vec,
        top_k=100,
        include_metadata=True,
        filter={"session_id": session_id}
    )
    return [
        (match["metadata"]["message"], match["metadata"]["reply"])
        for match in result.get("matches", [])
        if "metadata" in match
    ]
