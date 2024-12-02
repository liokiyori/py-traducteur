from fastapi import FastAPI
import uvicorn

from datetime import datetime
import statistics
from config.parametres import VERSIONS
from model.nlp import traduire
from model.prompt import Prompt
from dto.service_traducteur import Service_Traducteur as st
from model.utilisateur import Utilisateur

metrics = {
    "translation_count": 0,
    "response_times": [],
    "language_usage": {"fr >> en": 0, "en >> fr": 0},
    "errors": 0
}

tags =[
       {
         "name":"index",
         "description":"Index"     
       },
     {
          "name":"traduction",
          "description":"Traduction"
     },
     {
          "name":"authentification",
          "description":"authentification"
     },
        {
            "name":"metrique",
            "description":"metrique"
        }
]

app = FastAPI(
     title="Appli de traduction",
     description="API de traudction",
     version="1.0.0",
     openapi_tags = tags
)

@app.get("/versions", tags=["index"])
def versions():
        return VERSIONS

@app.post("/traductions", tags=["traduction"])
def traducteur(prompt: Prompt):
    start_time = datetime.now()
    try:
        traduire(prompt)
        metrics["translation_count"] += 1
        metrics["language_usage"][prompt.version] += 1
    except Exception as e:
        metrics["errors"] += 1
    finally:
        response_time = (datetime.now() - start_time).total_seconds()
        metrics["response_times"].append(response_time)
    st.sauvegarder_prompt(prompt)
    return prompt

@app.get("/traductions/auteur/{id}", tags=["traduction"])
def versions_par_auteur(id:int):
       return st.lister_prompts(id)

@app.post("/login", tags=["authentification"])
def authentifier(utilisateur:Utilisateur):
       st.verifier_login(utilisateur)
       return {"authentifié" : utilisateur.authentifie, "id":utilisateur.id}

@app.get("/metrique", tags=["metrique"])
def metrique():
    avg_response_time = statistics.mean(metrics["response_times"]) if metrics["response_times"] else 0
    return {
        "total_translations": metrics["translation_count"],
        "average_response_time": avg_response_time,
        "language_usage": metrics["language_usage"],
        "errors": metrics["errors"]
    }

if __name__ == "__main__" :
    uvicorn.run(app, host="0.0.0.0", port=8080)

