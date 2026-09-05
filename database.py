import os
from dotenv import load_dotenv
from langchain_community.vectorstores import PGVector
from embeddings import get_embeddings

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
TABLE_NAME = "uniqlo_knowledge"

if not DATABASE_URL:
    raise ValueError("DATABASE_URL tidak ditemukan di .env")

def get_vector_store():
    return PGVector(
        connection_string=DATABASE_URL,
        collection_name=TABLE_NAME,
        embedding_function=get_embeddings(),
    )
