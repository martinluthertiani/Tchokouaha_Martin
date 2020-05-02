# Un objet "obj_mon_application" pour utiliser la classe Flask
# Pour les personnes qui veulent savoir ce que signifie __name__ une démonstration se trouve ici :
# https://www.studytonight.com/python/_name_-as-main-method-in-python
# C'est une chaîne de caractère qui permet de savoir si on exécute le code comme script principal
# appelé directement avec Python et pas importé.
import flask
from APP_FILMS.DATABASE import connect_db_context_manager


# Objet qui fait "exister" notre application
obj_mon_application = flask.Flask(__name__, template_folder="templates")
# Flask va pouvoir crypter les cookies
obj_mon_application.secret_key = '_vogonAmiral_)?^'


# Doit se trouver ici... soit après l'instanciation de la classe "Flask"
# OM 2020.03.25 Tout commence ici par "indiquer" les routes de l'application.
from APP_PERSONNES import routes
from APP_PERSONNES.PERSONNES import routes_gestion_personnes
from APP_PERSONNES.MAILS import routes_gestion_mails
from APP_PERSONNES.PERS_MAILS import routes_gestion_pers_mails