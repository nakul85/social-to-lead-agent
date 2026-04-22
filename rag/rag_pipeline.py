from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.documents import Document
import json


def load_knowledge():
    with open("rag/knowledge.json") as f:
        data = json.load(f)

    docs = []

    for plan in data["plans"]:
        text = f"{plan['name']} costs {plan['price']} and includes {', '.join(plan['features'])}"
        docs.append(Document(page_content=text))

    for policy in data["policies"]:
        docs.append(Document(page_content=policy))

    return docs


def create_vectorstore():
    docs = load_knowledge()
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(docs, embeddings)
    return vectorstore
