from flask import Flask, render_template, jsonify, request
from src.helper import download_hugging_face_embeddings
from langchain_community.vectorstores import Pinecone
from langchain_groq import ChatGroq
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from src.prompt import *
import os
from dotenv import load_dotenv


app = Flask(__name__)

load_dotenv()


PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

embeddings = download_hugging_face_embeddings()

index_name = "medicalbot"

from langchain_community.vectorstores import Pinecone

docsearch = Pinecone.from_existing_index(
    index_name=index_name,
    embedding = embeddings
)

retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k":3})

system_prompt = (
    "You are an assistant for question-answering tasks."
    "Use the following pieces of retrieved context to answer "
    "the question. If you dont know the answer, say that you "
    "don't know. Use three sentences maximum and keep the "
    "answer concise"
    "\n\n"
    "{context}"
)

llm = ChatGroq(temperature=0.4, max_tokens=500)
prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "{input}"),
])

question_answer_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)

@app.route("/")
def index():
    return render_template('chat.html')
 
@app.route("/get", methods = ["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    print(input)
    response = rag_chain.invoke({"input": msg})
    print("Response : ", response["answer"])
    return str(response["answer"])

if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = 8080, debug = True)

