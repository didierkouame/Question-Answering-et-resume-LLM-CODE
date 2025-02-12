# Le code est exécuté dans un environnement virtuel déjà configuré pour vertex ai 

# nécessite les librairies suivantes : 
# importer la classe request qui permet d'envoyer des requêtes HTTP
from google.auth.transport.requests import Request

# importer la classe credentials qui permet de créer des objets de type service account 
# à partir d'un fichier JSON qu'on utilise pour authentifier un service de API Google Cloud
from google.oauth2.service_account import Credentials

# chemin vers la clé d'authentification
# cette clé est générée sur google cloud en un fichier json qu'on télécharge
# qui permettra de se connecter au compte de service Google Cloud
chemin_cle = '' # n'est pas affiché ici 

#créé un objet credentials à partir du fichier de service
# scope indique les permissions accordées pour accéder aux ressources google cloud (accès global)
credentials = Credentials.from_service_account_file(chemin_cle, scopes=['https://www.googleapis.com/auth/cloud-platform'])

if credentials.expired:
	credentials.refresh(Request()) # si les informations d'authentification ont expiré , les rafraîchir

PROJECT_ID = '' # ID du projet google cloud qui interagit avec les API # n'est pas affiché ici
REGION = 'europe-west1' # région geographique ou les ressources sont déployées, si usa la latence sera élevée


import vertexai # importer le module vertexai qui interagit avec google cloud pour l'IA comme le résumé de texte

vertexai.init(project=PROJECT_ID, location=REGION)


# importer les classes pour configurer et utiliser un modèle génératif 
from vertexai.generative_models import GenerationConfig, GenerativeModel

generation_model = GenerativeModel("gemini-1.5-pro") # paramètre de génération

generation_config = GenerationConfig(temperature=0.1, max_output_tokens=1024) #paramètres de configuration



prompt = """
Source de l'article : L'Est Républicain (Source ajoutée volontairement)
Droit du sang, du sol, naturalisation : quelles sont les règles pour devenir Français ?
Le gouvernement a rouvert ces derniers jours le débat sur les conditions d'acquisition de la nationalité française. Actuellement, la nationalité française repose sur le droit du sang et le droit du sol.
C.T - Aujourd'hui à 19:01 - Temps de lecture : 6 min  
En 2023, 97 288 personnes ont acquis la nationalité française. Photo d'illustration Sipa / Patrick Siccoli
En 2023, 97 288 personnes ont acquis la nationalité française. Photo d'illustration Sipa / Patrick Siccoli
Depuis quelques jours, la classe politique s'enflamme autour de l'acquisition de la nationalité française. Le Premier ministre François Bayrou souhaite ouvrir un débat sur « qu'est ce que c'est d'être Français ». Son ministre de la Justice, Gérald Darmanin, estime que « le débat public doit s'ouvrir sur le droit du sol dans notre pays ».
Éric Lombard, ministre de l'Économie juge, lui, « le dispositif législatif actuel tout à fait satisfaisant », tout comme François Hollande, qui estime le débat « inutile ». Enfin, la cheffe de file du Rassemblement national, Marine Le Pen, réclame un référendum pour changer la loi. 
En France, la nationalité repose sur une combinaison du droit du sang et du droit du sol, des principes qui remontent au Moyen Âge. Mais il est aussi possible d'obtenir la nationalité française par d'autres moyens. On fait le point sur les règles en vigueur qui permettent actuellement de devenir Français.
Le droit du sang 
La nationalité française est attribuée de manière automatique à toute personne dont au moins un des parents est Français, et ce peu importe son lieu de naissance. C'est le droit du sang.
L'enfant né en France qui a un de ses parents qui y est lui-même né obtient également la nationalité française dès sa naissance. La nationalité française est également accordée de manière automatique à l'enfant né en France de deux parents apatrides.
Le droit du sol
Lorsque les deux parents sont étrangers, l'enfant né en France peut obtenir la nationalité française à sa majorité. C'est ce qu'on appelle le droit du sol. Mais certaines conditions sont nécessaires: il doit résider en France à l'âge de ses 18 ans et y avoir résidé pendant au moins cinq ans, de manière continue ou discontinue, depuis ses 11 ans. Si l'enfant remplit ces conditions, l'acquisition est automatique à la majorité.
Cette obtention de la nationalité française à la majorité en vertu du droit du sol peut être anticipée dès l'âge de 13 ans, en faisant une demande de naturalisation en préfecture. Il faut alors que les représentants légaux de l'enfant justifient une résidence en France de cinq années depuis l'âge de 8 ans.
L'exception Mayotte
Les règles ne sont pas les mêmes à Mayotte, où le droit du sol a été durci en 2018 par la loi Asile et immigration. Pour qu'un enfant né à Mayotte devienne Français, il faut que l'un de ses parents ait, au jour de sa naissance, été présent de manière régulière en France depuis au moins trois mois.
Jeudi dernier, l'Assemblée nationale a également adopté une proposition de loi visant à restreindre davantage le droit du sol à Mayotte. Si elle était définitivement adoptée, elle conditionnerait l'obtention de la nationalité française pour les enfants nés à Mayotte au fait que les « deux parents » (et non plus d'un seul) aient été présents régulièrement sur le sol français depuis au moins trois ans (et non plus trois mois).
Le mariage
Il est également possible d'obtenir la nationalité française en justifiant de certains liens affectifs et parentaux. L'étranger marié à une personne de nationalité française peut ainsi devenir français par déclaration, quatre ans après le mariage. Il faut toutefois pouvoir justifier d'une communauté de vie affective et matérielle et d'une connaissance suffisante de la langue française. Pour pouvoir obtenir la nationalité française, la personne ne doit pas avoir été condamné à une peine d'au moins 6 mois de prison avec sursis, ni avoir été condamné pour un crime ou un délit constituant une atteinte aux intérêts fondamentaux de la Nation, ou avoir été condamné pour un acte de terrorisme. 
Le délai d'obtention de la nationalité est porté à cinq ans de mariage lorsque le demandeur ne justifie pas d'avoir résidé au moins trois ans en France à compter du mariage ou pendant la résidence à l'étranger du couple, si le conjoint français n'a pas été inscrit au registre des Français établis hors de France. Dans tous les cas, une fois le dossier de demande de naturalisation déposé, les époux sont convoqués à un entretien au cours duquel la réalité de la communauté de vie et de l'assimilation à la société française seront vérifiés. Les acquisitions par mariage représentaient en 2023 20% des acquisitions de la nationalité française, selon les données de l'Insee.
A lire aussi
Après les budgets, le gouvernement de François Bayrou menacé par le dossier de l'immigration
Débat sur l'immigration : le patron du PS ne veut pas laisser la place à la droite
Des liens familiaux
D'autres liens affectifs peuvent aussi permettre d'obtenir la nationalité française. Ainsi, si vous êtes un étranger de 65 ans au moins et avez un enfant, petit-enfant ou arrière petit-enfant de nationalité française, vous pouvez réclamer la nationalité française, à condition de résider régulièrement et habituellement en France depuis au moins 25 ans.
De la même manière, si votre frère ou soeur a obtenu la nationalité française en vertu du droit du sol, vous pouvez également l'obtenir. Il faut pour cela respecter certaines conditions : résider en France depuis l'âge de 6 ans de manière habituelle et régulière, avoir suivi la scolarité obligatoire en France dans un établissement soumis au contrôle de l'Etat, ne pas avoir eu de condamnation pénale et ne pas avoir fait l'objet d'un arrêté d'expulsion ou d'une interdiction du territoire français toujours en vigueur.
Vous pouvez également devenir Français si vous avez été adopté ou recueilli par une personne française. Les acquisitions par ascendants et fratrie représentaient en 2023 2,2% des acquisitions de la nationalité française, selon les données de l'Insee.
La naturalisation
D'autres conditions permettent de demander l'acquisition de la nationalité française à partir de 18 ans : avoir le statut de réfugié, venir d'un pays francophone et parler le français, venir d'un pays francophone et avoir été scolarisé cinq ans ou plus dans un établissement enseignant en langue français, avoir fait son service militaire dans l'armée française, s'être engagé dans l'armée française ou une armée alliée en temps de guerre, avoir rendu des services exceptionnels à la France, avoir obtenir un diplôme d'enseignement supérieur français après deux ans d'études, avoir accompli un parcours exceptionnel d'intégration. 
Une durée minimale de cinq ans de résidence est exigée, et peut être abaissée à deux ans si le demandeur a accompli avec succès deux ans d'étude dans un établissement d'enseignement supérieur français ou s'il a rendu des services importants à la France. Il faut aussi avoir en France le centre de ses intérêts matériels et de ses liens familiaux. Il faut aussi prouver son assimilation à la communauté française, notamment en étant en accord avec les principes et valeurs essentiels de la République et en ayant des connaissances sur l'histoire, la culture et la société françaises. Il faut aussi pouvoir justifier d'une insertion professionnelle et d'une connaissance suffisante de la langue française.
La demande de naturalisation est discrétionnaire et l'administration peut refuser la demande même si toutes les conditions d'accès sont remplies. En 2023, les acquisitions par naturalisation représentaient 40,8% des acquisitions de la nationalité française.
Des cas exceptionnels
Enfin, la nationalité française peut vous être accordée de manière exceptionnelle sur proposition du ministre de la Défense si vous avez été blessé lors de votre engagement dans l'armée française ou sur proposition du ministre des Affaires étrangères si vous êtes francophone et que vous contribuez par votre activité au rayonnement de la France.

Summary:

"""

response = generation_model.generate_content(
    contents=prompt, generation_config=generation_config
).text
print(response)


#on pourrait générer des résumés avec les modèles disponibles sur hugging face
# mais ceux ci ont des limites de longueur de texte en input qu'ils peuvent traiter en une seule fois 512 ou 1024
# mais si on décide de limiter les tokens du texte aux modèles en faisant des "chunks"(morcellement)
# on peut perdre de l'information
# LongFormer créé pour gérer des séquences de textes longues fait mieux jusqu'à 4096 tokens
#

#nom fichier
fichier_nom = "resume_article.txt"
with open(fichier_nom, 'w') as fichier:
  fichier.write(response)
print("Résumé sauvegardé.")