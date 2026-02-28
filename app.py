from langchain_community.document_loaders import PyPDFDirectoryLoader,PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import ChatGoogleGenerativeAI,GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
import streamlit as st

from dotenv import load_dotenv
import os
load_dotenv()

key = os.getenv('GEMINI_API_KEY')

loader = PyPDFLoader(r'your_file_path')
doc = loader.load()


splitter = RecursiveCharacterTextSplitter(chunk_size = 1000,chunk_overlap = 200)
documents = splitter.split_documents(doc)

embedding = GoogleGenerativeAIEmbeddings(api_key=key,model="gemini-embedding-001")
vector_store = Chroma(embedding_function=embedding)
vector_store.add_documents(documents)
retriever = vector_store.as_retriever()

prompt = ChatPromptTemplate.from_template("""Based on user question give the correct answer based only on context
                                 question:{question}
                                 context:{context}""")

llm = ChatGoogleGenerativeAI(api_key=key,model='gemini-2.5-flash', temperature=0.2)

rag_chain = ({'context':retriever,"question":RunnablePassthrough()} | prompt | llm | StrOutputParser() )

st.title('Retrieval Augmented Generation')

st.image(r'your_image_here')

query = st.text_input("Enter the Query")

if st.button("Predict"):
    response = rag_chain.invoke(query)
    st.write(response)