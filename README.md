# 🛍️ UNIQLO Customer Assistant (RAG Prototype)

Proyek ini adalah prototipe aplikasi Customer Assistant berbasis Retrieval-Augmented Generation (RAG) yang dirancang khusus untuk menjawab pertanyaan pelanggan seputar produk, teknologi kain (seperti AIRism), dan kebijakan toko dari **UNIQLO**. 

Aplikasi ini dibangun menggunakan kerangka kerja LangChain, basis data vektor PostgreSQL (PgVector), model bahasa besar (LLM) dari **Groq**, serta antarmuka web interaktif menggunakan **Streamlit**.

---

## 🚀 Fitur Utama
* **Semantic Search & Retrieval**: Mengambil informasi relevan dari basis pengetahuan dokumen teks secara akurat menggunakan *embeddings*.
* **LLM Integration**: Memanfaatkan model berkecepatan tinggi dari Groq untuk menghasilkan respons asisten layanan pelanggan yang ramah dan kontekstual.
* **Interactive UI**: Antarmuka obrolan (*chat interface*) berbasis web yang bersih dan responsif menggunakan Streamlit.

---

## 🛠️ Tech Stack
* **Python 3.11+**
* **LangChain** (RAG Orchestration)
* **Groq API** (LLM Provider)
* **PostgreSQL + PgVector** (Vector Database via Docker)
* **Streamlit** (Web UI)

---

## ⚙️ Cara Menjalankan Proyek Secara Lokal

Ikuti langkah-langkah berikut untuk menjalankan proyek ini di komputer Anda:

### 1. Klon Repository
```bash
git clone [https://github.com/Cayocayo/uniqlo-customer-assistant.git](https://github.com/Cayocayo/uniqlo-customer-assistant.git)
cd uniqlo-customer-assistant

2. Buat dan Aktifkan Virtual Environment
Bash
python -m venv .venv
# Untuk macOS/Linux:
source .venv/bin/activate
# Untuk Windows:
# .venv\Scripts\activate

3. Install Pustaka yang Dibutuhkan
Bash
pip install -r requirements.txt

4. Konfigurasi Environment Variables
Buat file bernama .env di root folder proyek, lalu isi dengan konfigurasi berikut:

Code snippet
GROQ_API_KEY=your_groq_api_key_here
DATABASE_URL=

5. Jalankan Basis Data PostgreSQL (Docker)
Pastikan Docker Desktop aktif di komputer Anda, lalu jalankan kontainer PostgreSQL dengan ekstensi PgVector:

Bash
docker run --name pgvector-container -e POSTGRES_PASSWORD=postgres -p 5432:5432 -d pgvector/pgvector:pg16

6. Jalankan Aplikasi Streamlit
Bash
streamlit run app.py

uniqlo-customer-assistant/
│
├── .venv/                 # Virtual Environment
├── app.py                 # Antarmuka web Streamlit
├── rag_pipeline.py        # Logika utama RAG & rantai LLM
├── database.py            # Koneksi database & vector store
├── embeddings.py          # Modul embedding dokumen
├── requirements.txt       # Daftar pustaka dependensi
├── .env                   # Konfigurasi kunci API & database (rahasia)
└── README.md              # Dokumentasi proyekgit