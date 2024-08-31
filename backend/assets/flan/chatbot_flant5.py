import faiss
from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import os
import deepl
from dotenv import load_dotenv

load_dotenv()

class ChatbotFlan:
    deepl_api_key = os.getenv("DEEPL_API_KEY")
    translator = deepl.Translator(deepl_api_key)
    sentence_transformers_name = 'paraphrase-MiniLM-L6-v2'

    def __init__(self, dataset, model_path, faiss_index_path) -> None:
        self.df = dataset
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_path)
        self.index = faiss.read_index(faiss_index_path)
        self.model_embeddings = SentenceTransformer(self.sentence_transformers_name)

    def get_answer(self, question: str):
        question = question.lower()
        
        # Convertir la pregunta del usuario en un embedding
        embedding_question = self.model_embeddings.encode([question])
        
        # Buscar el índice de la pregunta más cercana en el espacio de embeddings
        _, index_question = self.index.search(embedding_question, 1)
        
        # Obtener la respuesta correspondiente a la pregunta más similar
        base_answer = self.df['respuesta'].iloc[index_question[0][0]]
        
        # Generar una respuesta con el modelo fine-tuneado usando el contexto en español
        input_text = f"Pregunta: {question}\nRespuesta: {base_answer}"
        input_ids = self.tokenizer(input_text, return_tensors='pt').input_ids
        
        # Generar la respuesta final
        output = self.model.generate(input_ids, max_new_tokens=128)
        answer = self.tokenizer.decode(output[0], skip_special_tokens=True)
        
        return self.translator.translate_text(answer, target_lang='ES').text