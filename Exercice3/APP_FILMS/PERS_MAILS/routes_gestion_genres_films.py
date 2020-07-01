# routes_gestion_genres_films.py
# OM 2020.04.16 Gestions des "routes" FLASK pour la table intermédiaire qui associe les films et les genres.

from flask import render_template, request, flash, session
from APP_FILMS.DATABASE.connect_db_context_manager import MaBaseDeDonnee
from APP_FILMS import obj_mon_application
from APP_FILMS.PERSONNES.data_gestion_genres import GestionGenres
from APP_FILMS.PERS_MAILS.data_gestion_genres_films import GestionGenresFilms

from flask import render_template, flash, redirect, url_for, request
from APP_FILMS import obj_mon_application
from APP_FILMS.PERSONNES.data_gestion_genres import GestionGenres
from APP_FILMS.DATABASE.erreurs import *
# OM 2020.04.10 Pour utiliser les expressions régulières REGEX
import re


# ---------------------------------------------------------------------------------------------------
# OM 2020.04.26 Définition d'une "route" /genres_films_afficher_concat
# Récupère la liste de tous les films et de tous les genres associés aux films.
# ---------------------------------------------------------------------------------------------------
@obj_mon_application.route("/genres_films_afficher_concat/<int:id_film_sel>", methods=['GET', 'POST'])
def genres_films_afficher_concat (id_film_sel):
    print("id_film_sel ", id_film_sel)
    if request.method == "GET":
        try:
            # OM 2020.04.09 Objet contenant toutes les méthodes pour gérer (CRUD) les données.
            obj_actions_genres = GestionGenresFilms()
            # Récupère les données grâce à une requête MySql définie dans la classe GestionGenres()
            # Fichier data_gestion_genres.py
            data_genres_films_afficher_concat = obj_actions_genres.genres_films_afficher_data_concat(id_film_sel)
            # DEBUG bon marché : Pour afficher le résultat et son type.
            print(" data genres", data_genres_films_afficher_concat, "type ", type(data_genres_films_afficher_concat))

            # Différencier les messages si la table est vide.
            if data_genres_films_afficher_concat:
                # OM 2020.04.09 La ligne ci-dessous permet de donner un sentiment rassurant aux utilisateurs.
                flash(f"Données genres affichés dans GenresFilms!!", "success")
            else:
                flash(f"""Le film demandé n'existe pas. Ou la table "t_genres_films" est vide. !!""", "warning")
        except Exception as erreur:
            print(f"RGGF Erreur générale.")
            # OM 2020.04.09 On dérive "Exception" par le "@obj_mon_application.errorhandler(404)" fichier "run_mon_app.py"
            # Ainsi on peut avoir un message d'erreur personnalisé.
            # flash(f"RGG Exception {erreur}")
            raise Exception(f"RGGF Erreur générale. {erreur}")
            # raise MaBdErreurOperation(f"RGG Exception {msg_erreurs['ErreurNomBD']['message']} {erreur}")

    # OM 2020.04.21 Envoie la page "HTML" au serveur.
    return render_template("genres_films/genres_films_afficher.html",
                           data=data_genres_films_afficher_concat)


# ---------------------------------------------------------------------------------------------------
# OM 2020.04.21 Définition d'une "route" /gf_edit_genre_film_selected
# Récupère la liste de tous les genres du film sélectionné.
# Nécessaire pour afficher tous les "TAGS" des genres, ainsi l'utilisateur voit les genres à disposition
# ---------------------------------------------------------------------------------------------------
@obj_mon_application.route("/gf_edit_genre_film_selected", methods=['GET', 'POST'])
def gf_edit_genre_film_selected ():
    if request.method == "GET":
        try:

            # OM 2020.04.09 Objet contenant toutes les méthodes pour gérer (CRUD) les données.
            obj_actions_genres = GestionGenres()
            # Récupère les données grâce à une requête MySql définie dans la classe GestionGenres()
            # Fichier data_gestion_genres.py
            # Pour savoir si la table "t_genres" est vide, ainsi on empêche l’affichage des tags
            # dans le render_template(genres_films_modifier_tags_dropbox.html)
            data_genres_all = obj_actions_genres.genres_afficher_data('ASC', 0)

            # OM 2020.04.09 Objet contenant toutes les méthodes pour gérer (CRUD) les données de la table intermédiaire.
            obj_actions_genres = GestionGenresFilms()

            # OM 2020.04.21 Récupère la valeur de "id_film" du formulaire html "genres_films_afficher.html"
            # l'utilisateur clique sur le lien "Modifier genres de ce film" et on récupère la valeur de "id_film" grâce à la variable "id_film_genres_edit_html"
            # <a href="{{ url_for('gf_edit_genre_film_selected', id_film_genres_edit_html=row.id_film) }}">Modifier les genres de ce film</a>
            id_personne = request.values['id_personne']
            id_email = request.values['id_email']

            # OM 2020.04.21 Mémorise l'id du film dans une variable de session
            # (ici la sécurité de l'application n'est pas engagée)
            # il faut éviter de stocker des données sensibles dans des variables de sessions.
            session['session_id_film_genres_edit'] = id_personne

            # Constitution d'un dictionnaire pour associer l'id du film sélectionné avec un nom de variable
            valeur_id_film_selected_dictionnaire = {"value_id_personne": id_personne}

            # Récupère les données grâce à 3 requêtes MySql définie dans la classe GestionGenresFilms()
            # 1) Sélection du film choisi
            # 2) Sélection des genres "déjà" attribués pour le film.
            # 3) Sélection des genres "pas encore" attribués pour le film choisi.
            # Fichier data_gestion_genres_films.py
            # ATTENTION à l'ordre d'assignation des variables retournées par la fonction "genres_films_afficher_data"
            selected_combo, other_addres, other_films = \
                obj_actions_genres.genres_films_afficher_data(id_personne, id_email)


            # OM 2020.04.09 La ligne ci-dessous permet de donner un sentiment rassurant aux utilisateurs.
            flash(f"Données genres affichées dans GenresFilms!!", "success")

        except Exception as erreur:
            print(f"RGGF Erreur générale.")
            # OM 2020.04.09 On dérive "Exception" par le "@obj_mon_application.errorhandler(404)"
            # fichier "run_mon_app.py"
            # Ainsi on peut avoir un message d'erreur personnalisé.
            # flash(f"RGG Exception {erreur}")
            raise Exception(f"RGGF Erreur générale. {erreur}")
            # raise MaBdErreurOperation(f"RGG Exception {msg_erreurs['ErreurNomBD']['message']} {erreur}")

    # OM 2020.04.21 Envoie la page "HTML" au serveur.
    return render_template("genres_films/genres_films_modifier_tags_dropbox.html",
                           datasourceselected_combo=selected_combo,
                           datasourceother_addres=other_addres,
                           datasourceother_films=other_films)


# ---------------------------------------------------------------------------------------------------
# OM 2020.04.26 Définition d'une "route" /gf_update_genre_film_selected
# Récupère la liste de tous les genres du film sélectionné.
# Nécessaire pour afficher tous les "TAGS" des genres, ainsi l'utilisateur voit les genres à disposition
# ---------------------------------------------------------------------------------------------------
@obj_mon_application.route("/gf_update_genre_film_selected", methods=['GET', 'POST'])
def gf_update_genre_film_selected ():
    if request.method == "POST":
        try:

            id_personne = request.values['newPersonne']
            id_mail = request.values['newEmail']
            id_Persomail = request.values['id_pers_mail']

            obj_actions_genres = GestionGenresFilms()
            obj_actions_genres.UpdatePersoMail(id_Persomail,id_personne, id_mail )

            flash(f"Données liaison modifiée!!", "success")

        except Exception as erreur:
            print(f"RGGF Erreur générale.")
            # OM 2020.04.09 On dérive "Exception" par le "@obj_mon_application.errorhandler(404)" fichier "run_mon_app.py"
            # Ainsi on peut avoir un message d'erreur personnalisé.
            # flash(f"RGG Exception {erreur}")
            raise Exception(f"RGGF Erreur générale. {erreur}")
            # raise MaBdErreurOperation(f"RGG Exception {msg_erreurs['ErreurNomBD']['message']} {erreur}")

    # Après cette mise à jour de la table intermédiaire "t_genres_films",
    # on affiche les films et le(urs) genre(s) associé(s).
    return redirect(url_for('genres_films_afficher_concat', id_film_sel = 0))
