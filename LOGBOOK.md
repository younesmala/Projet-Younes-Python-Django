\# 🧾 LOGBOOK – Projet Younes Python Django



\## Auteur

\*\*Younes El Mallahi\*\*

Bachelier Informatique – Développement d’Applications

Institut des Carrières Commerciales (ICC), Bruxelles



---



\## Journal de bord du projet



**### 🔹 1. Installation de Python et pip**



\- \*\*Problème :\*\* Python installé mais non reconnu dans le terminal.

\- \*\*Cause :\*\* Chemin d’accès non ajouté dans les variables d’environnement.

\- \*\*Solution :\*\* Ajout du dossier `C:\\\\Program Files\\\\Python314\\\\` dans le PATH.

 

Vérification avec :



python --version

pip --version





---



**### 🔹 2. Création de l’environnement virtuel**



\- \*\*Problème :\*\* Erreur “No module named venv”.

\- \*\*Solution :\*\* Installation du module manquant puis création :





python -m pip install virtualenv

py -m venv .venv

.venv\\Scripts\\activate





---



**### 🔹 3. Installation de Django**



\- \*\*Problème :\*\* Commande `django-admin` non reconnue.

\- \*\*Solution :\*\*





pip install django

python -m django --version





---



**### 🔹 4. Création du projet Django**

\- Création du projet :





django-admin startproject reservations



\- Test du serveur :



python manage.py runserver



\- Vérification : page Django par défaut visible sur `http://127.0.0.1:8000/`



---



**### 🔹 5. Ajout de l’application `catalogue`**

\- Création :





python manage.py startapp catalogue



\- Ajout dans `settings.py` :

```python



INSTALLED\\\_APPS = \\\[

\&nbsp;   ...,

\&nbsp;   'catalogue',

]



**\*\*🔹 6. Configuration de la base de données\*\***



Problème : Erreur à l’installation de mysqlclient.



Solution :



Installation de Microsoft Visual C++ Build Tools ou alternative :



pip install mysql-connector-python





Test OK avec :



DATABASES = {

\&nbsp;   'default': {

\&nbsp;       'ENGINE': 'mysql.connector.django',

\&nbsp;       'NAME': 'reservations',

\&nbsp;       'USER': 'root',

\&nbsp;       'PASSWORD': '',

\&nbsp;       'HOST': '127.0.0.1',

\&nbsp;       'PORT': '3306',

\&nbsp;   }

}



**\*\*🔹 7. Gestion de Git et GitHub\*\***



Initialisation du dépôt :



git init

git add .

git commit -m "Initial commit - Django setup"





Lien avec GitHub :



git remote add origin https://github.com/younesmala/Projet-Younes-Python-Django.git

git push -u origin main





Ajout d’un .gitignore pour éviter d’envoyer .venv/ et db.sqlite3.



**\*\*🔹 8. Problèmes de fusion (merge)\*\***



Erreur : “There isn’t anything to compare” sur GitHub.



Cause : Historique Git différent entre branches.



Solution :



git merge integrate-reservations --allow-unrelated-histories





Résolution manuelle des conflits puis :



git add .

git commit -m "Merge corrigé"

git push



**\*\*🔹 9. Nettoyage GitHub\*\***



Suppression de l’ancien dépôt reservationsDjango.



Tout le code consolidé dans Projet-Younes-Python-Django.



**\*\*🔹 10. Documentation finale\*\***



Création du README.md clair et propre.



Ajout du LOGBOOK.md et WIKI.md pour suivi du projet.


**\*\*🔹 11. autres oublis\*\***


- Toujours activer le venv avant pip install.
- Committer régulièrement avec des messages clairs.
\* Fermer correctement les blocs ``` dans les fichiers Markdown (README tout écrit en mode code)
- Vérifier les branches avant un push.


# 
