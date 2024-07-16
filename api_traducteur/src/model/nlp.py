from transformers import pipeline
from config.parametres import VERSIONS
from model.prompt import Prompt

def traduire(prompt:Prompt) :
    try :
        if prompt.version == VERSIONS[0] :
            translator = pipeline("translation", model="Helsinki-NLP/opus-mt-fr-en")
        if prompt.version == VERSIONS[1] :
            translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-fr")
        prompt.traduction = translator(prompt.atraduire)[0]['translation_text']
    except Exception as exc:
        raise ValueError(f'Traduction non disponible pour la version {prompt.version}') from exc
    return(prompt)