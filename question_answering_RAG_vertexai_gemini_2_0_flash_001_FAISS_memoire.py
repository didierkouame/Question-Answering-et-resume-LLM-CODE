from langchain_google_vertexai import VertexAI
from langchain_google_vertexai.embeddings import VertexAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain.chains.retrieval import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain import hub
import os

# Le code est exécuté dans un environnement virtuel déjà configuré pour vertex ai
# charger le modèle de récupération
retrieval_qa_chat_prompt = hub.pull("langchain-ai/retrieval-qa-chat")

# Ingestion des documents
def ingestion():
    # étape 1 charger les documents depuis le PDF
    loader = PyPDFLoader("Memoire_master1_didier_hernandez.pdf")
    documents = loader.load_and_split()

   # etape 2 embedding des chunks du document sans redéfinir la clé dans le modèle
    embedding_model = VertexAIEmbeddings("textembedding-gecko")
    vectorstore = FAISS.from_documents(documents=documents, embedding=embedding_model)

     # étap3 sauvegarder les vecteurs dans un vectordb local
    vectorstore.save_local("faiss_index_vectorstore")



# récupération de la réponse à la requête
def retriever(message):
    
    llm = VertexAI(model_name="gemini-2.0-flash-001", temperature=0.3)
    embedding_model = VertexAIEmbeddings("textembedding-gecko")

    # étape 2 Chargement de l'index FAISS local
    new_store = FAISS.load_local("faiss_index_vectorstore", embedding_model, allow_dangerous_deserialization=True)
    
    # étape 3 chaîne de récupération pour combiner les résultats
    combine_docs_chain = create_stuff_documents_chain(llm, retrieval_qa_chat_prompt)
    qa = create_retrieval_chain(new_store.as_retriever(), combine_docs_chain)


    #la langue de réponse

    message_en_francais = f"Réponds en français : {message}" # ligne ajoutée

    
    res = qa.invoke(input={"input": message_en_francais})
    response = res["answer"]
    #res = qa.invoke(input={"input": message})
    #response = res["answer"]

    

    
    # enregistrer la réponse dans un fichier texte
    with open("question_answering_RAG_vertexai_FAISS_gemini_2_0_flash_001.txt", "w") as f:
        f.write(response)
    
    print(response)


# exécution 
if __name__ == "__main__":
    ingestion()  # Étape d'ingestion
    input_message = "Résume ce document en détail et quelles sont les ouvertures"  # Exemple de requête
    retriever(input_message)  # Récupération et génération de la réponse
