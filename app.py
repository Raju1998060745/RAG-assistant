import logging
from flask import Flask, request, jsonify
from flask_cors import CORS
from langchain_community.vectorstores import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms.ollama import Ollama
from get_embedding_function import get_embedding_function

CHROMA_PATH = "chroma"

PROMPT_TEMPLATE = """
your are my assistant so Answer the recruiter question positively based on the following context:

{context}

---

Answer the question based on the above context: {question}
"""

app = Flask(__name__)
CORS(app)

# Configure logging
logging.basicConfig(level=logging.DEBUG)

@app.route('/answer', methods=['POST'])
def answer():
    data = request.get_json()
    query_text = data.get("question", "")
    
    if not query_text:
        return jsonify({"error": "No question provided"}), 400

    try:
        response_text = query_rag(query_text)
        return jsonify({"response": response_text})
    except Exception as e:
        app.logger.error("Error occurred: %s", str(e))
        return jsonify({"error": str(e)}), 500

def query_rag(query_text: str):
    # Prepare the DB.
    embedding_function = get_embedding_function()
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

    # Search the DB.
    results = db.similarity_search_with_score(query_text, k=5)

    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)

    model = Ollama(model="llama3")
    response_text = model.invoke(prompt)

    return response_text

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
