import requests
from pathlib import Path

# Liste des URLs CSV
url_template = "https://data.toulouse-metropole.fr/api/explore/v2.1/catalog/datasets/{}/exports/csv?lang=fr&timezone=Europe%2FBerlin&use_labels=true&delimiter=%3B"
datasets = [
    "38-station-meteo-toulouse-parc-jardin-des-plantes",
    "63-station-meteo-toulouse-life-marechal-juin",
    "58-station-meteo-toulouse-fondeyre",
    '13-station-meteo-toulouse-pech-david',
    '33-station-meteo-saint-jory-chapelle-beldou',
    '02-station-meteo-toulouse-marengo',
    '62-station-meteo-toulouse-parc-maourine',
    '42-station-meteo-toulouse-parc-compans-cafarelli',
    '08-station-meteo-toulouse-basso-cambo',
    '48-station-meteo-toulouse-la-machine-af',
    '19-station-meteo-mondouzil-mairie',
    '31-station-meteo-mons-station-epuration',
    '20-station-meteo-mondonville-ecole',
    '34-station-meteo-toulouse-teso',
    '40-station-meteo-toulouse-zi-thibaud',
    '03-station-meteo-toulouse-busca',
    '23-station-meteo-pibrac-bouconne-centre-equestre',
    '05-station-meteo-toulouse-life-hall-1',
    '37-station-meteo-toulouse-universite-paul-sabatier',
    '05-station-meteo-toulouse-nakache',
    '41-station-meteo-toulouse-avenue-de-casselardit',
    '45-station-meteo-toulouse-st-exupery',
    '53-station-meteo-toulouse-ponsan',
    '47-station-meteo-toulouse-la-machine-tm',
    '39-station-meteo-tournefeuille-ecole',
    '30-station-meteo-toulouse-george-sand',
    '17-station-meteo-fenouillet-foyer',
    '28-station-meteo-toulouse-carmes',
    '22-station-meteo-colomiers-za-perget',
    '26-station-meteo-toulouse-reynerie',
    '04-station-meteo-toulouse-ile-empalot',
    '14-station-meteo-toulouse-centre-pierre-potier',
    '27-station-meteo-toulouse-saint-cyprien',
    '09-station-meteo-toulouse-la-salade',
    '51-station-meteo-toulouse-lardenne',
    '18-station-meteo-brax-ecole',
    '36-station-meteo-toulouse-purpan',
    '66-station-meteo-toulouse-life-coubertin',
    '49-station-meteo-toulouse-cote-pavee',
    '07-station-meteo-toulouse-avenue-de-grande-bretagne',
    '00-station-meteo-toulouse-valade',
    '23-station-meteo-pibrac-bouconne-centre-equestr-archive-2019',
    '22-station-meteo-colomiers-za-perget-archive-2022',
    '22-station-meteo-colomiers-za-perget-archive-2021',
    '22-station-meteo-colomiers-za-perget-archive-2020',
    '22-station-meteo-colomiers-za-perget-archive-2019',
    '19-station-meteo-mondouzil-mairie-archive-2022',
    '19-station-meteo-mondouzil-mairie-archive-2020',
    '19-station-meteo-mondouzil-mairie-archive-2021',
    '19-station-meteo-mondouzil-mairie-archive-2019',
    '18-station-meteo-brax-ecole-archive-2022',
    '18-station-meteo-brax-ecole-archive-2021',
    '18-station-meteo-brax-ecole-archive-2020',
    '18-station-meteo-brax-ecole-archive-2019',
    '17-station-meteo-fenouillet-foyer-archive-2020',
    '17-station-meteo-fenouillet-foyer-archive-2019',
    '15-station-meteo-l-union-ecole',
    '13-station-meteo-toulouse-pech-david-archive-2020',
    '13-station-meteo-toulouse-pech-david-archive-2019',
    '11-station-meteo-toulouse-soupetard-archive-2020',
    '12-station-meteo-toulouse-montaudran-archive-2020',
    '12-station-meteo-toulouse-montaudran-archive-2019',
    '11-station-meteo-toulouse-soupetard-archive-2019',
    '11-station-meteo-toulouse-soupetard-archive-2021',
    '10-station-meteo-castelginest-ecole-archive-2020',
    '10-station-meteo-castelginest-ecole-archive-2019',
    '09-station-meteo-toulouse-la-salade-archive-2021',
    '09-station-meteo-toulouse-la-salade-archive-2020',
    '09-station-meteo-toulouse-la-salade-archive-2019',
    '08-station-meteo-toulouse-basso-cambo-archive-2021',
    '08-station-meteo-toulouse-basso-cambo-archive-2020',
    '08-station-meteo-toulouse-basso-cambo-archive-2019',
    '07-station-meteo-toulouse-avenue-de-grande-bretagne-archive-2021',
    '07-station-meteo-toulouse-avenue-de-grande-bretagne-archive-2020',
    '07-station-meteo-toulouse-avenue-de-grande-bretagne-archive-2019',
    '03-station-meteo-toulouse-busca-archive2020',
    '03-station-meteo-toulouse-busca-archive2019',
    '02-station-meteo-toulouse-marengo-archive2020',
    '02-station-meteo-toulouse-marengo-archive2019',
    '01-station-meteo-toulouse-meteopole-archive2020',
    '01-station-meteo-toulouse-meteopole-archive-2019',
    '05-station-meteo-toulouse-nakache-archive2019',
    '32-station-meteo-mons-ecole',
    '65-station-meteo-toulouse-life-gastou',
    '61-station-meteo-blagnac-mairie',
    '10-station-meteo-castelginest-ecole',
    '21-station-meteo-cugnaux-general-de-gaulle',
    '25-station-meteo-tournefeuille-residentiel',
    '50-station-meteo-blagnac-quinze-sols',
    '24-station-meteo-colomiers-zi-enjacca',
    '11-station-meteo-toulouse-soupetard',
    '01-station-meteo-toulouse-meteopole',
    '12-station-meteo-toulouse-montaudran',
]

# Dossier où enregistrer les fichiers
output_dir = Path("data/meteo")
output_dir.mkdir(exist_ok=True)

for dataset in datasets:
    filename = f'{dataset}.csv'
    filepath = output_dir / filename
    if filepath.exists():
        print(f'Skip dataset existant: {dataset}')
        continue
    url = url_template.format(dataset)

    print(f"Download: {url}")
    response = requests.get(url)
    response.raise_for_status()  # lève une exception si erreur HTTP

    # Écrire le contenu dans un fichier
    with open(filepath, "wb") as f:
        f.write(response.content)
    print(f"Enregistré dans: {filepath}")

print("Téléchargements terminés !")
