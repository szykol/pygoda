from google.cloud import translate

translate_client = translate.Client()

def translate_text(text):
    return translate_client.translate(text,target_language='en')['translatedText']
