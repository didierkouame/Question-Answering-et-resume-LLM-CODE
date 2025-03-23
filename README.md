# Question Answering et Résumé avec Vertex AI et LangChain

Ce dépôt contient plusieurs expérimentations autour du **question answering (QA)** et du **résumé automatique** avec LLM, en utilisant **Vertex AI**, **LangChain** et **FAISS**.
Les codes ont été exécutés dans un environnement Python configuré pour Vertex AI sur Google Cloud. 

## Contenu du dépôt

### 📌 Question Answering avec et sans RAG
- **question_answering_RAG_vertexai_FAISS_gemini_1_5_flash_001.txt** : Réponse générée par le modèle **Gemini 1.5 Flash** avec **RAG**.
- **question_answering_RAG_vertexai_FAISS_gemini_2_0_flash_001.txt** : Réponse générée par le modèle **Gemini 2.0 Flash** avec **RAG**.
- **question_answering_RAG_vertexai_gemini_1_5_flash_FAISS_001_memoire.py** : Code Python pour effectuer du **QA avec RAG** sur un mémoire en PDF avec **Gemini 1.5 Flash**.
- **question_answering_RAG_vertexai_gemini_2_0_flash_001_FAISS_memoire.py** : Code Python pour du **QA avec RAG** sur un mémoire en PDF avec **Gemini 2.0 Flash**.
- **question_answering_vertex_ai.py** : Code Python pour du **QA sans RAG** avec Vertex AI.
- **question_answering_article_vertexai_sans_rag.txt** : Résultat de QA sur un article sans RAG.
- **Question-Answering_Extractive.ipynb** : Notebook d'extraction pour le **QA extractif**.

### 📌 Résumé automatique
- **resume_long_texte_gemini1_5_pro.py** : Code Python pour résumer un long texte avec **Gemini 1.5 Pro**.
- **resume_article.txt** : Résumé généré d'un article de presse de *L'Est Républicain*.
- **Évaluation_résumé_automatique.ipynb** : Notebook contenant l'évaluation du résumé avec **BERTScore** (**score : 69%**).

### 📌 Fichiers supplémentaires
- **taln-2008-long-001.pdf.tei.xml** : Document utilisé pour tester le QA dans Question-Answering_Extractive.ipynb.
- **capture_python_vertex_ai_terminal.png** : Capture d'écran des tests réalisés dans le terminal.

## 🛠 Technologies utilisées
- **Vertex AI** (Gemini 1.5 Flash, Gemini 2.0 Flash, Gemini 1.5 Pro)
- **LangChain** (gestion des chaînes de récupération et traitement des documents)
- **FAISS** (stockage et recherche vectorielle pour RAG)
- **BERTScore** (évaluation du résumé)
- **Python**
