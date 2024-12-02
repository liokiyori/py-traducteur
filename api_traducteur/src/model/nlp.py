from transformers import pipeline
from config.parametres import VERSIONS
from model.prompt import Prompt

def traduire(prompt:Prompt) :
    try :
        if prompt.version == VERSIONS[0] :
            translator = pipeline("translation", model="Helsinki-NLP/opus-mt-fr-en")
        elif prompt.version == VERSIONS[1] :
            translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-fr")
        else :
            translator = None
        prompt.traduction = translator(prompt.atraduire)[0]['translation_text']
    except Exception as e:
        print(f"Une erreur est survenue lors de la traduction: {e}")
        prompt.traduction = None

    return(prompt)