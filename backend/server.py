from flask import Flask, jsonify, request
from assets.bert.chatbot_bert import ChatbotBert
from assets.flan.chatbot_flant5 import ChatbotFlan
from flask_cors import CORS, cross_origin
import pandas as pd
import spacy

PORT = 8000
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

nlp = spacy.load("es_core_news_sm")
dataset = pd.read_csv('./assets/preguntas_respuestas.csv', encoding='utf8')

chatbotBert = ChatbotBert(
    dataset=dataset, faiss_index_path='./assets/bert/faiss_index_bert.bin')

chatbotFlan = ChatbotFlan(dataset=dataset, model_path='./assets/flan/flan-t5-finetuned',
                          faiss_index_path='./assets/flan/faiss_index_flan.bin')

def is_complex_question(question):
    is_too_long = len(question.split()) > 10
    doc = nlp(question)
    has_clauses = any(token.dep_ in {'advcl', 'ccomp', 'xcomp'} for token in doc)
    
    return is_too_long or has_clauses

def askToChatbot(question: str):
    return chatbotBert.get_answer(question) if is_complex_question(question) else chatbotFlan.get_answer(question)

@app.route('/')
@cross_origin()
def home():
    return "¡Hola, Flask!"


@app.route('/chatbot', methods=['POST'])
@cross_origin()
def chatbot():
    data = request.get_json()
    question = data.get('question', 'sin pregunta')
    answer = askToChatbot(question)
    return jsonify({"answer": f"{answer}"})


@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(405)
def endpoint_not_found_error(error):
    return jsonify({"error": "endpoint not found"}), 405


if __name__ == '__main__':
    print('Iniciando servidor...')
    app.run(debug=True, port=PORT, host="0.0.0.0")
    print('Servidor finalizado correctamente')
