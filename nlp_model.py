from transformers import pipeline

pipe = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base",top_k=None,device=-1)

def bot_mood(text):
    result=pipe(text)
    return result[0][0]
