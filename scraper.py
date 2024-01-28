# Importez les modules Django et configurez les paramètres
import os
import django
import json
from django.db.utils import IntegrityError
import uuid

# Configurez Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "projet_GL.settings")
django.setup()

# Importez les modules Django et autres modules nécessaires après la configuration
from django.contrib.auth import get_user_model
from authentification.models import Avocat

# Obtenez le répertoire du script
script_dir = os.path.dirname(__file__)

def scrape_and_initialize_data():
    print("Début du scraping...")

    # Chargez les données depuis le fichier index.json
    json_data = load_data_from_json(script_dir)

    if json_data:
        for avocat_info in json_data:
            nom_avocat = avocat_info.get("name")
            print(f"Nom de l'avocat : {nom_avocat}")

            # Ajoutez d'autres champs spécifiques à votre modèle Avocat
            specialite = ", ".join(avocat_info.get("categories", []))
            coordinates = f"Latitude: {avocat_info.get('latitude')}, Longitude: {avocat_info.get('longitude')}"
            experiences = avocat_info.get("description", "")

            # Créez l'utilisateur associé à l'avocat
            user = None
            username_attempt = nom_avocat

            while not user:
                try:
                    user = get_user_model().objects.create(username=username_attempt)
                except IntegrityError:
                    # Le nom d'utilisateur existe déjà, essayez avec un suffixe différent
                    username_attempt = f"{nom_avocat}_{uuid.uuid4().hex[:6]}"

            try:
                # Enregistrez les données dans la base de données Django
                Avocat.objects.create(
                    user=user,
                    nom=nom_avocat,
                    specialite=specialite,
                    coordinates=coordinates,
                    experiences=experiences,
                    # Ajoutez d'autres champs spécifiques à votre modèle Avocat
                )
                print(f"Avocat {nom_avocat} ajouté à la base de données.")
            except Exception as e:
                print(f"Erreur lors de l'ajout de l'avocat {nom_avocat} : {e}")

        print("Scraping terminé avec succès.")
    else:
        print("Aucune donnée à scraper.")

def load_data_from_json(script_dir):
    json_file_path = os.path.join(script_dir, 'index.json')

    try:
        with open(json_file_path, 'r', encoding='utf-8') as json_file:
            data = json_file.read()
            json_data = json.loads(data)
            print("Importation réussie depuis index.json.")
            return json_data
    except FileNotFoundError:
        print(f"Fichier {json_file_path} introuvable.")
        return None
    except json.JSONDecodeError as e:
        print(f"Erreur lors de la lecture du fichier JSON {json_file_path} : {e}")
        return None
    except Exception as e:
        print(f"Erreur inattendue lors de l'importation des données depuis {json_file_path} : {e}")
        return None

if __name__ == "__main__":
    scrape_and_initialize_data()
