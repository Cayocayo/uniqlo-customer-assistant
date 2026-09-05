from database import get_vector_store
from langchain_core.documents import Document

def load_knowledge_base():
    raw_documents = [
        Document(
            page_content="Jaket Fleece UNIQLO terbuat dari bahan bulu domba daur ulang yang sangat lembut, ringan, dan memberikan kehangatan ekstra di cuaca dingin.",
            metadata={"category": "Jaket", "product": "Fleece"}
        ),
        Document(
            page_content="AIRism adalah teknologi kain inovatif dari UNIQLO yang dirancang agar cepat kering, sejuk, lembut di kulit, dan menyerap keringat dengan sangat baik untuk kenyamanan sepanjang hari.",
            metadata={"category": "Teknologi Kain", "product": "AIRism"}
        ),
        Document(
            page_content="HEATTECH adalah kain fungsional berteknologi tinggi yang menyerap kelembapan tubuh dan mengubahnya menjadi panas, menjaga tubuh tetap hangat di suhu dingin.",
            metadata={"category": "Teknologi Kain", "product": "HEATTECH"}
        ),
        Document(
            page_content="Kebijakan pengembalian dan penukaran barang di toko UNIQLO dapat dilakukan dalam waktu 30 hari sejak tanggal pembelian dengan syarat membawa struk belanja asli dan label harga masih terpasang utuh.",
            metadata={"category": "Layanan Pelanggan", "topic": "Pengembalian"}
        ),
        Document(
            page_content="Jam operasional standar gerai UNIQLO di mal wilayah Jakarta dan sekitarnya umumnya buka setiap hari mulai pukul 10.00 pagi hingga 22.00 malam WIB.",
            metadata={"category": "Informasi Toko", "topic": "Jam Operasional"}
        )
    ]

    print("Memuat dokumen ke dalam vector store (PgVector)...")
    vector_store = get_vector_store()
    
    vector_store.add_documents(raw_documents)
    print("Knowledge base berhasil dimasukkan ke PgVector!")

if __name__ == "__main__":
    load_knowledge_base()