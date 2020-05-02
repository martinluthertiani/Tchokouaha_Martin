# routes_gestion_pers_mails.py
# Martin Luther 2020.04.16 Gestions des "routes" FLASK pour la table intermédiaire qui associe les personnes et les mails.
from flask import render_template
from APP_PERSONNES import obj_mon_application


# ---------------------------------------------------------------------------------------------------
# Martin Lurher 2020.04.07 Définition d'une "route" /pers_mails_afficher
# cela va permettre de programmer les actions avant d'interagir
# avec le navigateur par la méthode "render_template"
# Pour tester http://127.0.0.1:1234/pers_mails_afficher
# ---------------------------------------------------------------------------------------------------
@obj_mon_application.route("/genres_pers_afficher", methods=['GET', 'POST'])
def pers_mails_afficher():
    # # Martin Luther 2020.04.09 Pour savoir si les données d'un formulaire sont un affichage
    # # ou un envoi de donnée par des champs du formulaire HTML.
    # if request.method == "GET":
    #     try:
    #         # Martin Luther 2020.04.09 Objet contenant toutes les méthodes pour gérer (CRUD) les données.
    #         obj_actions_pers_mails = GestionFilmsGenres()
    #         # Récupére les données grâce à une requête MySql définie dans la classe GestionGenres()
    #         # Fichier data_gestion_mails.py
    #         data_pers_mails = obj_actions_genres_films.genres_afficher_data()
    #         # DEBUG bon marché : Pour afficher un message dans la console.
    #
    #         # Martin Luther 2020.04.09 La ligns ci-après permet de donner un sentiment rassurant aux utilisateurs.
    #         flash("Données genres de films affichées !!", "Success")
    #     except Exception as erreur:
    #         print(f"RGFG Erreur générale.")
    #         # OM 2020.04.09 On dérive "Exception" par le "@obj_mon_application.errorhandler(404)" fichier "run_mon_app.py"
    #         # Ainsi on peut avoir un message d'erreur personnalisé.
    #         # flash(f"RGG Exception {erreur}")
    #         raise Exception(f"RGFG Erreur générale. {erreur}")

    # OM 2020.04.07 Envoie la page "HTML" au serveur.
    return render_template("pers_mails/pers_mails_afficher.html")

