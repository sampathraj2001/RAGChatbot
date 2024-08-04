import streamlit as st
from embedding_model import EmbeddingModel
from pinecone_setup import initialize_pinecone
from pdf_processing import extract_text

# Initialize Pinecone and model
index = initialize_pinecone()
embedding_model = EmbeddingModel()

# Dictionary to map IDs to text chunks
id_to_chunk = {}


def add_chunks_to_pinecone(chunks):
    global id_to_chunk
    for i, chunk in enumerate(chunks):
        embedding = embedding_model.get_embeddings(chunk)
        id_to_chunk[str(i)] = chunk  # Store chunk with ID
        index.upsert([(str(i), embedding)])

def query_pinecone(query_text):
    query_embedding = embedding_model.get_embeddings(query_text)
    results = index.query(vector=query_embedding, top_k=5)
    return results


# Streamlit app
st.title('RAG Chatbot🤖')
st.markdown("""
    This app works by uploading PDF files. Based on the PDFs you upload, you can ask questions from the content.
    *(You can find sample PDFs regarding data science in the docs folder of this project.)*
""")

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'question_counter' not in st.session_state:
    st.session_state.question_counter = 1
if 'current_answer' not in st.session_state:
    st.session_state.current_answer = ""
if 'chunks_uploaded' not in st.session_state:
    st.session_state.chunks_uploaded = False

# File uploader
uploaded_files = st.file_uploader("Upload PDF files", type="pdf", accept_multiple_files=True)
if uploaded_files:
    for uploaded_file in uploaded_files:
        text, chunks = extract_text(uploaded_file)
        add_chunks_to_pinecone(chunks)
    st.session_state.chunks_uploaded = True
    st.write("Chunks added to Pinecone.")

# Conditionally display the question input only after chunks are uploaded
if st.session_state.chunks_uploaded:
    query_text = st.text_input("Ask a question:")
    if query_text:
        results = query_pinecone(query_text)

        # Get the most appropriate match
        if results['matches']:
            best_match = max(results['matches'], key=lambda x: x['score'])
            chunk_id = best_match['id']
            chunk_text = id_to_chunk.get(chunk_id, "Text not found")

            # Update current answer and chat history
            st.session_state.current_answer = chunk_text
            st.session_state.chat_history.append({
                'question': f"{st.session_state.question_counter}) {query_text}",
                'answer': chunk_text
            })
            st.session_state.question_counter += 1

        # Display current answer below the input box
        if st.session_state.current_answer:
            st.write(f"**Ans:** {st.session_state.current_answer}")

    # Display chat history
    st.write("Chat History:")
    for entry in st.session_state.chat_history:
        st.write(f"Q: {entry['question']}")
        st.write(f"A: {entry['answer']}")
