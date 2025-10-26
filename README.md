# README



\# Projet Younes Python Django



\*\*Projet académique réalisé dans le cadre du module PID (Projet d’Intégration en Développement).\*\*  

Ce projet utilise le framework \*\*Django 5\*\* pour concevoir une application web de \*\*gestion de réservations\*\* avec un module interne \*\*catalogue\*\*.



---



\## Fonctionnalités principales



\- Système de \*\*gestion des réservations\*\*

\- Module interne \*\*catalogue\*\* (application Django)

\- Interface \*\*administrateur Django\*\* intégrée

\- Base de données \*\*MySQL\*\* (ou SQLite en local)

\- Architecture \*\*MVC (Modèles / Vues / Templates)\*\*

\- Compatible avec \*\*Windows, Linux et Mac\*\*



---


\## Installation locale


\### 1. Cloner le projet

```bash

git clone https://github.com/younesmala/Projet-Younes-Python-Django.git

cd Projet-Younes-Python-Django


\### 2. Créer et activer un environnement virtuel


python -m venv .venv

.venv\\Scripts\\activate      # sur Windows

\# ou

source .venv/bin/activate   # sur Linux / Mac


\### 3. Installer les dépendances


pip install -r requirements.txt


\### 4. Configurer la base de données


Dans le fichier reservations/settings.py, ajustez les paramètres du bloc DATABASES selon votre environnement :


Exemples: 

MySQL: 							


DATABASES = {

&nbsp;   'default': {

&nbsp;       'ENGINE': 'django.db.backends.mysql',

&nbsp;       'NAME': 'reservations',

&nbsp;       'USER': 'root',

&nbsp;       'PASSWORD': '',

&nbsp;       'HOST': '127.0.0.1',

&nbsp;       'PORT': '3306',

&nbsp;   }

}


SQLite: 

DATABASES = {

&nbsp;   'default': {

&nbsp;       'ENGINE': 'django.db.backends.sqlite3',

&nbsp;       'NAME': BASE\_DIR / 'db.sqlite3',

&nbsp;   }

}


\### 5: Appliquer les migrations


python manage.py migrate


\### 6: Lancer le serveur


python manage.py runserver

```


L’application est accessible à l’adresse :  
http://127.0.0.1:8000/

## Structure du projet

Projet-Younes-Python-Django/

├── catalogue/ # Application interne Django

├── reservations/ # Projet principal (settings, urls, etc.)

├── manage.py # Point d’entrée du projet

├── db.sqlite3 # Base de données locale

├── requirements.txt # Dépendances Python

├── .gitignore # Fichiers ignorés par Git

└── .venv/ # Environnement virtuel (local)

Auteur: 

Younes El Mallahi

Étudiant en Bachelier Informatique – Développement d’Applications

📍 Institut des Carrières Commerciales (ICC), Bruxelles

📧 Contact GitHub


Licence : 


Projet académique à usage pédagogique — non destiné à un usage commercial.








