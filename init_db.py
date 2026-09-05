from database import get_vector_store, TABLE_NAME

def init_table():
    print(f"Membuat tabel vektor '{TABLE_NAME}' di database...")
    get_vector_store()
    print("Tabel berhasil dibuat dan diinisialisasi!")

if __name__ == "__main__":
    init_table()
