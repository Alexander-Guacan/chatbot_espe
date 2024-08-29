import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'
import torch
import faiss
from transformers import BertTokenizer, BertModel

class ChatbotBert:
    model_name = 'bert-base-multilingual-cased'
    
    def __init__(self, dataset, faiss_index_path) -> None:
        self.df = dataset
        self.tokenizer = BertTokenizer.from_pretrained(self.model_name)
        self.model = BertModel.from_pretrained(self.model_name)
        self.index = faiss.read_index(faiss_index_path)
    
    def get_answer(self, question: str):
        question = question.lower()
        # Tokenizar la pregunta
        inputs = self.tokenizer([question], padding=True, truncation=True, max_length=512, return_tensors="pt")
        # Generar el embedding de la pregunta
        with torch.no_grad():
            outputs = self.model(**inputs)
            embedding_question = outputs.last_hidden_state.mean(dim=1).numpy()

        # Buscar en el índice FAISS la pregunta más cercana
        _, index_question = self.index.search(embedding_question, 1)
        
        # Obtener la respuesta correspondiente
        answer = self.df['respuesta'].iloc[index_question[0][0]]
        
        return answer