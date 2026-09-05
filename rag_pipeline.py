import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from database import get_vector_store

load_dotenv()

def get_rag_chain():
    vector_store = get_vector_store()
    retriever = vector_store.as_retriever(
        search_kwargs={"k": 2}
    )

    # Inisialisasi LLM menggunakan Groq dengan model yang valid dan aktif
    llm = ChatGroq(
        model="openai/gpt-oss-120b",
        temperature=0
    )

    template = """Anda adalah asisten layanan pelanggan (customer service) resmi untuk UNIQLO.
Jawab pertanyaan pelanggan dengan ramah, profesional, dan akurat berdasarkan konteks informasi yang diberikan di bawah ini.
Jika Anda tidak mengetahui jawabannya atau informasi tidak ada dalam konteks, katakan dengan sopan bahwa Anda tidak memiliki informasi tersebut dan arahkan mereka untuk bertanya langsung ke staf toko.

Konteks:
{context}

Pertanyaan Pelanggan:
{question}

Jawaban:"""

    prompt = ChatPromptTemplate.from_template(template)

    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    rag_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    return rag_chain

if __name__ == "__main__":
    chain = get_rag_chain()
    query = "Berapa lama batas waktu penukaran barang di UNIQLO?"
    print(f"Pertanyaan: {query}\n")
    
    response = chain.invoke(query)
    print("Jawaban AI:")
    print(response)