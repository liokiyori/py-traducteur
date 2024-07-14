# py-traducteur
Cas pratique sur un traducteur

## Ticket d'incidence
Cas pratique sur un traducteur. C'est un travail individuel qui est attendu de vous. Chaque apprenant devra présenter un rapport personnel, du code personnel et un dashboard personnel.

## Les tickets d'incident
Chaque branche représente un ticket d'incident. Il y a 3 branches, donc 3 tickets.

Les tickets sont répartis de la façon suivante : 
- ticket 1 : Frédéric, Mikaël, Andy, Jérémy, Gwendal
- ticket 2 : Alexandre, Yann, Youenn, Ibrahim, Laura
- ticket 3 : Morgan, Pierre-Marie, Thibaut, Yves 

Vous trouverez toutes les informations du ticket dans le Readme.

## Installation
Merci de ne rien modifier sur ce dépôt.

1. Faire un clone de la branche qui vous intéresse sur votre dépôt GitHub. Créez une branche pour la correction.
2. Installer Git en local. Récupérer le projet en local.
3. Lancer d'abord la base de données grâce à Docker Compose.
4. Créer un environnement virtuel pour l'API, puis installez dans l'environnement virtuel les dépendances à partir du fichier `requirements.txt`. Lancez l'API en exécutant le code Python.
5. Créer un environnement virtuel pour l'application web, puis installez dans l'environnement virtuel les dépendances à partir du fichier `requirements.txt`. Lancez l'application web grâce aux commandes de Streamlit.

## Travail à réaliser
Avant de commencer la résolution du ticket, commencez par lire les attendus du rapport, pour pouvoir relever toutes les informations attendues aux bons moments. 

- Tracez le bug en utilisant les outils de debug et les points d'arrêt.
- Corrigez le bug et testez la solution.
- Mettez à jour la branche avec la correction documentée.
- Ajoutez des contrôles dans le code pour remonter des informations sur le nouveau code.
- Ajoutez un dashboard pour assurer le suivi de l'application.
- Une des métriques doit permettre le suivi du modèle.
- Ajoutez la documentation du dashboard.
- Redéployez la solution sur votre dépôt GitHub.
- Rédigez votre rapport.

## Rapport
Le rapport compte entre 2 et 5 pages.

- Présentation de l'application.
- Présentation de l'incident technique.
- Présentez le message d'erreur en console et expliquez-le.
- Expliquez les recherches faites pour résoudre l'incident technique.
- Expliquez la correction apportée et le test de validation.
- Expliquez le versionnage de la correction dans Git et le déploiement sur GitHub.
- Ajoutez la documentation sur le dashboard en expliquant le choix des métriques, le choix de la technologie, la mise à jour des indicateurs et les alertes.

## Compétences visées
C.20 : Surveiller une application d’intelligence artificielle
C.21 : Résoudre les incidents techniques

Ces deux compétences sont validées par l'épreuve E5.

## Technologies utilisées
- Le transformer d'Huggingface pour le traducteur
- FastAPI pour l'API
- Streamlit pour l'application web
