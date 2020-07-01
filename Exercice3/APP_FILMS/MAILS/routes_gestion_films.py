# routes_gestion_films.py
# OM 2020.04.06 Gestions des "routes" FLASK pour les films.

import pymysql

from flask import render_template, flash, redirect, url_for, request
from APP_FILMS import obj_mon_application
from APP_FILMS.MAILS.data_gestion_films import GestionFilms
from APP_FILMS.DATABASE.erreurs import *
# OM 2020.04.10 Pour utiliser les expressions régulières REGEX
import re

# OM 2020.04.16 Afficher un avertissement sympa...mais contraignant
# Pour la tester http://127.0.0.1:5005/avertissement_sympa_pour_geeks
@obj_mon_application.route("/avertissement_sympa_pour_geeks")
def avertissement_sympa_pour_geeks():
    # OM 2020.04.07 Envoie la page "HTML" au serveur.
    return render_template("films/AVERTISSEMENT_SYMPA_POUR_LES_GEEKS_films.html")




# OM 2020.04.16 Afficher les films
# Pour la tester http://127.0.0.1:5005/films_afficher
@obj_mon_application.route("/films_afficher", methods=['GET', 'POST'])
def films_afficher():
    # OM 2020.04.09 Pour savoir si les données d'un formulaire sont un affichage
    # ou un envoi de donnée par des champs du formulaire HTML.
    if request.method == "GET":
        try:
            # OM 2020.04.09 Objet contenant toutes les méthodes pour gérer (CRUD) les données.
            obj_actions_films = GestionFilms()
            # Récupère les données grâce à une requête MySql définie dans la classe GestionFilms()
            # Fichier data_gestion_films.py
            data_films = obj_actions_films.films_afficher_data()
            # DEBUG bon marché : Pour afficher un message dans la console.
            print(" data films", data_films, "type ", type(data_films))
            # Différencier les messages si la table est vide.
            if data_films:
                # OM 2020.04.09 La ligne ci-dessous permet de donner un sentiment rassurant aux utilisateurs.
                flash("Données films affichées !!", "success")
            else:
                flash("""La table "t_films" est vide. !!""", "warning")
        except Exception as erreur:
            print(f"RGF Erreur générale.")
            # OM 2020.04.09 On dérive "Exception" par le "@obj_mon_application.errorhandler(404)" fichier "run_mon_app.py"
            # Ainsi on peut avoir un message d'erreur personnalisé.
            # flash(f"RGG Exception {erreur}")
            raise Exception(f"RGF Erreur générale. {erreur}","danger")

    # OM 2020.04.07 Envoie la page "HTML" au serveur.
    return render_template("films/films_afficher.html", data=data_films)


# OM 2020.04.06 Pour une simple démo. On insère deux fois des valeurs dans la table films
# Une fois de manière fixe, vous devez changer les valeurs pour voir le résultat dans la table "t_films"
# La 2ème il faut entrer la valeur du titre du film par le clavier, il ne doit pas être vide.
# Pour les autres valeurs elles doivent être changées ci-dessous.
# Une des valeurs est "None" ce qui en MySql donne "NULL" pour l'attribut "t_films.cover_link_film"
# Pour la tester http://127.0.0.1:5005/films_add
@obj_mon_application.route("/films_add", methods=['GET', 'POST'])
def films_add():
    # OM 2019.03.25 Pour savoir si les données d'un formulaire sont un affichage
    # ou un envoi de donnée par des champs utilisateurs.
    if request.method == "POST":
        try:
            # OM 2020.04.09 Objet contenant toutes les méthodes pour gérer (CRUD) les données.
            obj_actions_genres = GestionFilms()
            # OM 2020.04.09 Récupère le contenu du champ dans le formulaire HTML "genres_add.html"
            InputMail = request.values['InputMail']

            # On ne doit pas accepter des valeurs vides, des valeurs avec des chiffres,
            # des valeurs avec des caractères qui ne sont pas des lettres.
            # Pour comprendre [A-Za-zÀ-ÖØ-öø-ÿ] il faut se reporter à la table ASCII https://www.ascii-code.com/
            # Accepte le trait d'union ou l'apostrophe, et l'espace entre deux mots, mais pas plus d'une occurence.
            if not re.match("^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$",
                            InputMail):
                # OM 2019.03.28 Message humiliant à l'attention de l'utilisateur.
                flash(f"Une entrée...incorrecte !! Merci de mettre un @ dans votre mail, "
                      , "danger")
                # On doit afficher à nouveau le formulaire "genres_add.html" à cause des erreurs de "claviotage"
                return render_template("films/films_add.html")
            else:

                # Constitution d'un dictionnaire et insertion dans la BD
                valeurs_insertion_dictionnaire = {'InputMail': InputMail}
                obj_actions_genres.add_films_data(valeurs_insertion_dictionnaire)

                # OM 2019.03.25 Les 2 lignes ci-après permettent de donner un sentiment rassurant aux utilisateurs.
                flash(f"Données insérées !!", "success")
                print(f"Données insérées !!")
                # On va interpréter la "route" 'genres_afficher', car l'utilisateur
                # doit voir le nouveau genre qu'il vient d'insérer. Et on l'affiche de manière
                # à voir le dernier élément inséré.
                return redirect(url_for('films_afficher'))

        # OM 2020.04.16 ATTENTION à l'ordre des excepts, il est très important de respecter l'ordre.
        except pymysql.err.IntegrityError as erreur:
            # OM 2020.04.09 On dérive "pymysql.err.IntegrityError" dans "MaBdErreurDoublon" fichier "erreurs.py"
            # Ainsi on peut avoir un message d'erreur personnalisé.
            raise MaBdErreurDoublon(
                f"RGG pei {msg_erreurs['ErreurDoublonValue']['message']} et son status {msg_erreurs['ErreurDoublonValue']['status']}")

        # OM 2020.04.16 ATTENTION à l'ordre des excepts, il est très important de respecter l'ordre.
        except (pymysql.err.OperationalError,
                pymysql.ProgrammingError,
                pymysql.InternalError,
                TypeError) as erreur:
            flash(f"Autre erreur {erreur}", "danger")
            raise MonErreur(f"Autre erreur")

        # OM 2020.04.16 ATTENTION à l'ordre des excepts, il est très important de respecter l'ordre.
        except Exception as erreur:
            # OM 2020.04.09 On dérive "Exception" dans "MaBdErreurConnexion" fichier "erreurs.py"
            # Ainsi on peut avoir un message d'erreur personnalisé.
            raise MaBdErreurConnexion(
                f"RGG Exception {msg_erreurs['ErreurConnexionBD']['message']} et son status {msg_erreurs['ErreurConnexionBD']['status']}")
    # OM 2020.04.07 Envoie la page "HTML" au serveur.
    return render_template("films/films_add.html")


@obj_mon_application.route('/films_edit', methods=['POST', 'GET'])
def films_edit ():
    # OM 2020.04.07 Les données sont affichées dans un formulaire, l'affichage de la sélection
    # d'une seule ligne choisie par le bouton "edit" dans le formulaire "genres_afficher.html"
    if request.method == 'GET':
        try:
            # Récupère la valeur de "id_genre" du formulaire html "genres_afficher.html"
            # l'utilisateur clique sur le lien "edit" et on récupère la valeur de "id_genre"
            # grâce à la variable "id_genre_edit_html"
            # <a href="{{ url_for('genres_edit', id_genre_edit_html=row.id_genre) }}">Edit</a>
            id_genre_edit = request.values['id_genre_edit_html']

            # Pour afficher dans la console la valeur de "id_genre_edit", une façon simple de se rassurer,
            # sans utiliser le DEBUGGER
            print(id_genre_edit)

            # Constitution d'un dictionnaire et insertion dans la BD
            valeur_select_dictionnaire = {"value_id_genre": id_genre_edit}

            # OM 2020.04.09 Objet contenant toutes les méthodes pour gérer (CRUD) les données.
            obj_actions_genres = GestionFilms()

            # OM 2019.04.02 La commande MySql est envoyée à la BD
            data_id_genre = obj_actions_genres.edit_films_data(valeur_select_dictionnaire)
            print("dataIdGenre ", data_id_genre, "type ", type(data_id_genre))
            # Message ci-après permettent de donner un sentiment rassurant aux utilisateurs.
            flash(f"Editer le genre d'un film !!!", "success")

        except (Exception,
                pymysql.err.OperationalError,
                pymysql.ProgrammingError,
                pymysql.InternalError,
                pymysql.IntegrityError,
                TypeError) as erreur:

            # On indique un problème, mais on ne dit rien en ce qui concerne la résolution.
            print("Problème avec la BD ! : %s", erreur)
            # OM 2020.04.09 On dérive "Exception" dans "MaBdErreurConnexion" fichier "erreurs.py"
            # Ainsi on peut avoir un message d'erreur personnalisé.
            raise MaBdErreurConnexion(f"RGG Exception {msg_erreurs['ErreurConnexionBD']['message']}"
                                      f"et son status {msg_erreurs['ErreurConnexionBD']['status']}")

    return render_template("films/films_edit.html", data=data_id_genre)

@obj_mon_application.route('/films_update', methods=['POST', 'GET'])
def films_update ():
    # DEBUG bon marché : Pour afficher les méthodes et autres de la classe "flask.request"
    print(dir(request))
    # OM 2020.04.07 Les données sont affichées dans un formulaire, l'affichage de la sélection
    # d'une seule ligne choisie par le bouton "edit" dans le formulaire "genres_afficher.html"
    # Une fois que l'utilisateur à modifié la valeur du genre alors il va appuyer sur le bouton "UPDATE"
    # donc en "POST"
    if request.method == 'POST':
        try:
            # DEBUG bon marché : Pour afficher les valeurs contenues dans le formulaire
            print("request.values ", request.values)

            # Récupère la valeur de "id_genre" du formulaire html "genres_edit.html"
            # l'utilisateur clique sur le lien "edit" et on récupère la valeur de "id_genre"
            # grâce à la variable "id_genre_edit_html"
            # <a href="{{ url_for('genres_edit', id_genre_edit_html=row.id_genre) }}">Edit</a>
            id_genre_edit = request.values['id_email_edit_html']

            # Récupère le contenu du champ "intitule_genre" dans le formulaire HTML "GenresEdit.html"
            NewEmail = request.values['UpdatedEmail']
            valeur_edit_list = [{'NewEmail': NewEmail}]
            # On ne doit pas accepter des valeurs vides, des valeurs avec des chiffres,
            # des valeurs avec des caractères qui ne sont pas des lettres.
            # Pour comprendre [A-Za-zÀ-ÖØ-öø-ÿ] il faut se reporter à la table ASCII https://www.ascii-code.com/
            # Accepte le trait d'union ou l'apostrophe, et l'espace entre deux mots, mais pas plus d'une occurence.
            if not re.match("^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$",
                            NewEmail):
                # En cas d'erreur, conserve la saisie fausse, afin que l'utilisateur constate sa misérable faute
                # Récupère le contenu du champ "intitule_genre" dans le formulaire HTML "GenresEdit.html"
                # name_genre = request.values['name_edit_intitule_genre_html']
                # Message humiliant à l'attention de l'utilisateur.
                flash(f"Une entrée...incorrecte !! Merci de mettre un @ dans votre mail, "
                      , "danger")

                # On doit afficher à nouveau le formulaire "genres_edit.html" à cause des erreurs de "claviotage"
                # Constitution d'une liste pour que le formulaire d'édition "genres_edit.html" affiche à nouveau
                # la possibilité de modifier l'entrée
                # Exemple d'une liste : [{'id_genre': 13, 'intitule_genre': 'philosophique'}]
                valeur_edit_list = [{'id_Mails': id_genre_edit, 'Nom_Mail': NewEmail}]

                # DEBUG bon marché :
                # Pour afficher le contenu et le type de valeurs passées au formulaire "genres_edit.html"
                print(valeur_edit_list, "type ..", type(valeur_edit_list))
                return render_template('films/films_edit.html', data=valeur_edit_list)
            else:
                # Constitution d'un dictionnaire et insertion dans la BD
                valeur_update_dictionnaire = {'idMail': id_genre_edit, 'NewEmail': NewEmail}

                # OM 2020.04.09 Objet contenant toutes les méthodes pour gérer (CRUD) les données.
                obj_actions_genres = GestionFilms()

                # La commande MySql est envoyée à la BD
                data_id_genre = obj_actions_genres.update_films_data(valeur_update_dictionnaire)
                # DEBUG bon marché :
                print("dataIdGenre ", data_id_genre, "type ", type(data_id_genre))
                # Message ci-après permettent de donner un sentiment rassurant aux utilisateurs.
                flash(f"Valeur genre modifiée. ", "success")
                # On affiche les genres avec celui qui vient d'être edité en tête de liste. (DESC)
                return redirect(url_for('films_afficher'))

        except (Exception,
                # pymysql.err.OperationalError,
                # pymysql.ProgrammingError,
                # pymysql.InternalError,
                # pymysql.IntegrityError,
                TypeError) as erreur:
            print(erreur.args[0])
            flash(f"problème genres ____lllupdate{erreur.args[0]}", "danger")
            # En cas de problème, mais surtout en cas de non respect
            # des régles "REGEX" dans le champ "name_edit_intitule_genre_html" alors on renvoie le formulaire "EDIT"
    return render_template('films/films_edit.html', data=valeur_edit_list)

@obj_mon_application.route('/films_select_delete', methods=['POST', 'GET'])
def films_select_delete ():
    if request.method == 'GET':
        try:

            # OM 2020.04.09 Objet contenant toutes les méthodes pour gérer (CRUD) les données.
            obj_actions_genres = GestionFilms()
            # OM 2019.04.04 Récupère la valeur de "idGenreDeleteHTML" du formulaire html "GenresDelete.html"
            id_genre_delete = request.args.get('id_genre_delete_html')

            # Constitution d'un dictionnaire et insertion dans la BD
            valeur_delete_dictionnaire = {"value_id_genre": id_genre_delete}

            # OM 2019.04.02 La commande MySql est envoyée à la BD
            data_id_genre = obj_actions_genres.delete_select_films_data(valeur_delete_dictionnaire)
            flash(f"EFFACER et c'est terminé pour cette \"POV\" valeur !!!", "warning")

        except (Exception,
                pymysql.err.OperationalError,
                pymysql.ProgrammingError,
                pymysql.InternalError,
                pymysql.IntegrityError,
                TypeError) as erreur:
            # Communiquer qu'une erreur est survenue.
            # DEBUG bon marché : Pour afficher un message dans la console.
            print(f"Erreur genres_delete {erreur.args[0], erreur.args[1]}")
            # C'est une erreur à signaler à l'utilisateur de cette application WEB.
            flash(f"Erreur genres_delete {erreur.args[0], erreur.args[1]}", "danger")

    # Envoie la page "HTML" au serveur.
    return render_template('films/films_delete.html', data=data_id_genre)


@obj_mon_application.route('/films_delete', methods=['POST', 'GET'])
def films_delete ():
    # OM 2019.04.02 Pour savoir si les données d'un formulaire sont un affichage ou un envoi de donnée par des champs utilisateurs.
    if request.method == 'POST':
        try:
            # OM 2020.04.09 Objet contenant toutes les méthodes pour gérer (CRUD) les données.
            obj_actions_genres = GestionFilms()
            # OM 2019.04.02 Récupère la valeur de "id_genre" du formulaire html "GenresAfficher.html"
            id_genre_delete = request.form['id_genre_delete_html']
            # Constitution d'un dictionnaire et insertion dans la BD
            valeur_delete_dictionnaire = {"value_id_genre": id_genre_delete}

            data_genres = obj_actions_genres.delete_films_data(valeur_delete_dictionnaire)
            # OM 2019.04.02 On va afficher la liste des genres des films
            # OM 2019.04.02 Envoie la page "HTML" au serveur. On passe un message d'information dans "message_html"

            # On affiche les genres
            return redirect(url_for('films_afficher'))



        except (pymysql.err.OperationalError, pymysql.ProgrammingError, pymysql.InternalError, pymysql.IntegrityError,
                TypeError) as erreur:
            # OM 2020.04.09 Traiter spécifiquement l'erreur MySql 1451
            # Cette erreur 1451, signifie qu'on veut effacer un "genre" de films qui est associé dans "t_genres_films".
            if erreur.args[0] == 1451:
                # C'est une erreur à signaler à l'utilisateur de cette application WEB.
                flash('IMPOSSIBLE d\'effacer !!! Cette valeur est associée à des films !', "warning")
                # DEBUG bon marché : Pour afficher un message dans la console.
                print(f"IMPOSSIBLE d'effacer !! Ce genre est associé à des films dans la t_genres_films !!! : {erreur}")
                # Afficher la liste des genres des films
                return redirect(url_for('films_afficher'))
            else:
                # Communiquer qu'une autre erreur que la 1062 est survenue.
                # DEBUG bon marché : Pour afficher un message dans la console.
                print(f"Erreur genres_delete {erreur.args[0], erreur.args[1]}")
                # C'est une erreur à signaler à l'utilisateur de cette application WEB.
                flash(f"Erreur genres_delete {erreur.args[0], erreur.args[1]}", "danger")

            # OM 2019.04.02 Envoie la page "HTML" au serveur.
    return render_template('films/films_afficher.html', data=data_genres)

