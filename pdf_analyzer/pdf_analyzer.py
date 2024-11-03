import PyPDF2
import re
import os
from transformers import pipeline

"""
Function to preprocess the text
Removes punctuation
Removes extra whitespace
it will return a text all in lower case
"""
def preprocessing_text(text):
    text = re.sub(r'[^\w\s]', '', text)  
    text = re.sub(r'\s+', ' ', text).strip()  
    return text.lower()  

# Function that reades a pfd and return a clear text
def read_pdf(file_path):
    file_text = ""
    
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            file_text += page.extract_text() + ' ' 

    return preprocessing_text(file_text)

"""
Function to read all pdf in directoy
save the content of all file in a single 
long string 
"""
def read_multiple_pdf(directory_path):
    all_texts = []
    
    for file_name in os.listdir(directory_path):
        if file_name.endswith('.pdf'):
            print(file_name)
            file_path = os.path.join(directory_path, file_name)
            clear_text = read_pdf(file_path)
            all_texts.append(clear_text)
    
    return ' '.join(all_texts)  

# load the model for question-answering
qa_model = pipeline("question-answering")

# Funzione per rispondere a una domanda sul testo
def get_an_answer(user_question, full_text):
    answer = qa_model(question=user_question, context=full_text)
    return answer['answer']

""""
simple use case 
"""
# Esempio di utilizzo
directory_path = 'pdf_only_text_test'  
whole_text = read_multiple_pdf(directory_path)

# print(whole_text)

user_question = input(" insert a new question about the context:  ")
answer = get_an_answer(whole_text, user_question)
print("answer:", answer)
