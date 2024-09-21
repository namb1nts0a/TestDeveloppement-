# Mon Application Django de Connexion

Cette application est un projet de connexion utilisateur utilisant Django. Elle permet aux utilisateurs de s'inscrire, se connecter et de se déconnecter.

## Prérequis

Assurez-vous d'avoir installé les éléments suivants sur votre machine :

- Python 3.10
- pip (gestionnaire de paquets Python)
- virtualenv (facultatif, mais recommandé)

## Installation

1. Clonez le dépôt depuis GitHub :

   ```bash
   git clone https://github.com/namb1nts0a/TestDeveloppement-

2. Accédez au répertoire du projet :
    ```bash
    cd mon-projet

3. Créez un environnement virtuel et activez-le :
    ```bash
    python -m venv env
    source env/bin/activate  

4. Installez les dépendances du projet :
    ```bash
    pip install -r requirements.txt


## Migration sur la base de donnees
    python manage.py migrate

## Lancement du server dev
    python manage.py runserver

## Lancement du test 
    python manage.py test
