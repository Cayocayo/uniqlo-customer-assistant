from database import get_vector_store

def test_retrieval():
    vector_store = get_vector_store()
    
    # Pertanyaan uji coba (tidak harus sama persis dengan teks dokumen)
    query = "Bagaimana kebijakan kalau mau tukar barang?"
    
    print(f"Mencari dokumen untuk query: '{query}'\n")
    
    # Melakukan pencarian kemiripan (similarity search)
    results = vector_store.similarity_search(query, k=2)
    
    for i, doc in enumerate(results, 1):
        print(f"Hasil {i}:")
        print(f"Isi: {doc.page_content}")
        print(f"Metadata: {doc.metadata}")
        print("-" * 40)

if __name__ == "__main__":
    test_retrieval()