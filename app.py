import streamlit as st
from rag_pipeline import get_rag_chain

st.set_page_config(page_title="UNIQLO Customer Assistant", page_icon="🛍️")

st.title("🛍️ UNIQLO Customer Assistant")
st.write("Halo! Saya adalah asisten virtual UNIQLO siap membantu pertanyaan seputar produk, teknologi kain, dan kebijakan toko.")

# Inisialisasi RAG chain
@st.cache_resource
def load_chain():
    return get_rag_chain()

try:
    chain = load_chain()
except Exception as e:
    st.error(f"Gagal memuat RAG Chain: {e}")

# Inisialisasi riwayat chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Tampilkan pesan chat sebelumnya
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input dari pengguna
if user_query := st.chat_input("Tulis pertanyaan Anda tentang UNIQLO di sini..."):
    # Simpan dan tampilkan pesan user
    st.session_state.messages.append({"role": "user", "content": user_query})
    with st.chat_message("user"):
        st.markdown(user_query)

    # Proses jawaban dari RAG pipeline
    with st.chat_message("assistant"):
        with st.spinner("Sedang mencari informasi..."):
            try:
                response = chain.invoke(user_query)
                st.markdown(response)
                # Simpan respons asisten
                st.session_state.messages.append({"role": "assistant", "content": response})
            except Exception as e:
                error_msg = f"Terjadi kesalahan saat memproses pertanyaan: {e}"
                st.error(error_msg)