import os
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec

def initialize_pinecone():
    load_dotenv()
    api_key = os.getenv("PINECONE_API_KEY")
    environment = os.getenv("PINECONE_ENV")
    index_name = os.getenv("PINECONE_INDEX_NAME")

    pc = Pinecone(api_key=api_key)
    if index_name not in [index['name'] for index in pc.list_indexes()]:
        pc.create_index(
            name=index_name,
            dimension=384,  # Update this if your embedding model's output dimension is different
            metric='cosine',
            spec=ServerlessSpec(
                cloud='aws',
                region=environment
            )
        )
    
    index = pc.Index(index_name)
    return index




