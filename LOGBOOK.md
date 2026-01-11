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

- Création :


python manage.py startapp catalogue

- Ajout dans `settings.py` :

```python



INSTALLED\\\_APPS = \\\[

\&nbsp;   ...,

\&nbsp;   'catalogue',

]

---


🔹 6. Configuration de la base de données\



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


---


🔹 7. Gestion de Git et GitHub\



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


### 🔹 11. Nettoyage final

- Suppression de l’ancien dépôt `reservationsDjango`.  
- Tout le code consolidé dans **Projet-Younes-Python-Django**. 

**\*\*🔹 12. autres oublis\*\***


- Toujours activer le venv avant pip install.
- Committer régulièrement avec des messages clairs.
\* Fermer correctement les blocs ``` dans les fichiers Markdown (README tout écrit en mode code)
- Vérifier les branches avant un push.

###🔹 13. WIKI en doublon dans mon projet \*\***

- Ajout d’une section Wiki directement sur GitHub pour centraliser toutes les commandes et notes techniques.  
- Suppression du fichier local `WIKI.md` (désormais remplacé par le Wiki en ligne).  
- Ajout d’un lien vers le Wiki dans le README principal :  
[Consulter le Wiki complet du projet](https://github.com/younesmala/Projet-Younes-Python-Django/wiki)

# 

###🔹 14. erreurs déctectées suite au mapping relationnel \*\***

la transition de Python 3.14 → Python 3.12 (compatibilité Django + mysqlclient)

la création correcte d’un environnement virtuel propre (.venv)

le remplacement du driver mysql-connector (non supporté) par mysqlclient

la correction du backend BD dans settings.py

la résolution des erreurs de connexion MySQL/MariaDB

la réparation des migrations du projet

la mise à jour du LogBook pour documenter l’ensemble des problèmes rencontrés

==> Détails des problèmes résolus:

Incompatibilité Python 3.14 avec mysqlclient → downgrade vers Python 3.12

Erreurs liées au driver MySQL non supporté

Backend de la base mal configuré dans settings.py

Migrations bloquées / base non accessible

Erreur « Can't connect to MySQL server » due à un mauvais driver

Erreur « display_name() takes 0 positional arguments » générée par le mauvais connecteur

Versions Django incompatibles → passage à Django 4.2.16 LTS

Analyse d’un projet fonctionnel pour vérifier le mapping relationnel

Documentation complète ajoutée dans le logbook

==> Résultat:

Le projet Django fonctionne désormais correctement

Les migrations sont opérationnelles

Le StarterKit est aligné avec les attentes du professeur

Le logbook est tenu à jour

==> POINTS D'ATTENTION: 

Toujours vérifier la compatibilité Python / Django / MySQL

Les drivers MySQL doivent correspondre au backend utilisé

Les erreurs de migrations sont souvent liées au driver ou aux versions

Git n’accepte pas de commit sans modification locale

Documenter systématiquement chaque erreur et solution

###🔹 15. acces admin 
Accès impossible à Django Admin

Le login vers /admin/ échouait systématiquement avec :

Please enter the correct username and password for a staff account.


Causes possibles :

mauvais mot de passe

compte non-staff

superuser non créé correctement

Solution :
Réinitialisation du compte administrateur via le shell Django :

from django.contrib.auth.models import User
u, created = User.objects.get_or_create(username="rootadmin")
u.is_staff = True
u.is_superuser = True
u.set_password("Admin123!")
u.save()


Après cela, l’accès à /admin/ fonctionnait parfaitement.
rootadmin
Admin123!

## Organisation du groupe

- Création du dépôt GitHub de groupe : PID_Groupe3
- Ajout des membres du groupe en tant que collaborateurs
- Mise en place d’une organisation de travail basée sur des branches personnelles




Dernière mise à jour : 11/01/2026