# routes_gestion_genres.py
# OM 2020.04.06 Gestions des "routes" FLASK pour les genres.

from flask import render_template, flash, redirect, url_for, request
from APP_FILMS import obj_mon_application
from APP_FILMS.PERSONNES.data_gestion_genres import GestionGenres
from APP_FILMS.DATABASE.erreurs import *
# OM 2020.04.10 Pour utiliser les expressions régulières REGEX
import re


# ---------------------------------------------------------------------------------------------------
# OM 2020.04.07 Définition d'une "route" /genres_afficher
# cela va permettre de programmer les actions avant d'interagir
# avec le navigateur par la méthode "render_template"
# Pour tester http://127.0.0.1:5005/genres_afficher
# order_by : ASC : Ascendant, DESC : Descendant
# ---------------------------------------------------------------------------------------------------
@obj_mon_application.route("/genres_afficher/<string:order_by>/<int:id_genre_sel>", methods=['GET', 'POST'])
def genres_afficher(order_by,id_genre_sel):
    # OM 2020.04.09 Pour savoir si les données d'un formulaire sont un affichage
    # ou un envoi de donnée par des champs du formulaire HTML.
    if request.method == "GET":
        try:
            # OM 2020.04.09 Objet contenant toutes les méthodes pour gérer (CRUD) les données.
            obj_actions_genres = GestionGenres()
            # Récupère les données grâce à une requête MySql définie dans la classe GestionGenres()
            # Fichier data_gestion_genres.py
            # "order_by" permet de choisir l'ordre d'affichage des genres.
            data_genres = obj_actions_genres.genres_afficher_data(order_by,id_genre_sel)
            # DEBUG bon marché : Pour afficher un message dans la console.
            print(" data genres", data_genres, "type ", type(data_genres))

            # Différencier les messages si la table est vide.
            if not data_genres and id_genre_sel == 0:
                flash("""La table "t_genres" est vide. !!""", "warning")
            elif not data_genres and id_genre_sel > 0:
                # Si l'utilisateur change l'id_genre dans l'URL et que le genre n'existe pas,
                flash(f"Le genre demandé n'existe pas !!", "warning")
            else:
                # Dans tous les autres cas, c'est que la table "t_genres" est vide.
                # OM 2020.04.09 La ligne ci-dessous permet de donner un sentiment rassurant aux utilisateurs.
                flash(f"Données genres affichés !!", "success")


        except Exception as erreur:
            print(f"RGG Erreur générale.")
            # OM 2020.04.09 On dérive "Exception" par le "@obj_mon_application.errorhandler(404)" fichier "run_mon_app.py"
            # Ainsi on peut avoir un message d'erreur personnalisé.
            # flash(f"RGG Exception {erreur}")
            raise Exception(f"RGG Erreur générale. {erreur}")
            # raise MaBdErreurOperation(f"RGG Exception {msg_erreurs['ErreurNomBD']['message']} {erreur}")

    # OM 2020.04.07 Envoie la page "HTML" au serveur.
    return render_template("genres/genres_afficher.html", data=data_genres)


# ---------------------------------------------------------------------------------------------------
# OM 2020.04.07 Définition d'une "route" /genres_add ,
# cela va permettre de programmer quelles actions sont réalisées avant de l'envoyer
# au navigateur par la méthode "render_template"
# En cas d'erreur on affiche à nouveau la page "genres_add.html"
# Pour la tester http://127.0.0.1:5005/genres_add
# ---------------------------------------------------------------------------------------------------
@obj_mon_application.route("/genres_add", methods=['GET', 'POST'])
def genres_add ():
    # OM 2019.03.25 Pour savoir si les données d'un formulaire sont un affichage
    # ou un envoi de donnée par des champs utilisateurs.
    if request.method == "POST":
        try:
            # OM 2020.04.09 Objet contenant toutes les méthodes pour gérer (CRUD) les données.
            obj_actions_genres = GestionGenres()
            # OM 2020.04.09 Récupère le contenu du champ dans le formulaire HTML "genres_add.html"
            NomPerso = request.values['InputNom']
            PrenomPerson = request.values['InputPrenom']
            RSPerso = request.values['InputRS']
            NomRespo = request.values['InputNR']
            PrenomRespo = request.values['InputPR']


            # On ne doit pas accepter des valeurs vides, des valeurs avec des chiffres,
            # des valeurs avec des caractères qui ne sont pas des lettres.
            # Pour comprendre [A-Za-zÀ-ÖØ-öø-ÿ] il faut se reporter à la table ASCII https://www.ascii-code.com/
            # Accepte le trait d'union ou l'apostrophe, et l'espace entre deux mots, mais pas plus d'une occurence.
            if not re.match("^[a-zA-Zéèàùûêâôë]{1}[a-zA-Zéèàùûêâôë \'-]*[a-zA-Zéèàùûêâôë]$",
                            NomPerso):
                # OM 2019.03.28 Message humiliant à l'attention de l'utilisateur.
                flash(f"Une entrée...incorrecte !! Pas de chiffres, de caractères spéciaux, d'espace à double, "
                      f"de double apostrophe, de double trait union et ne doit pas être vide.", "danger")
                # On doit afficher à nouveau le formulaire "genres_add.html" à cause des erreurs de "claviotage"
                return render_template("genres/genres_add.html")
            else:

                # Constitution d'un dictionnaire et insertion dans la BD
                valeurs_insertion_dictionnaire = {'NomPerso': NomPerso, 'PrenomPerso': PrenomPerson,'RSPerso': RSPerso ,
                                 'NomRespo': NomRespo,'PrenomRespo': PrenomRespo}
                obj_actions_genres.add_genre_data(valeurs_insertion_dictionnaire)

                # OM 2019.03.25 Les 2 lignes ci-après permettent de donner un sentiment rassurant aux utilisateurs.
                flash(f"Données insérées !!", "success")
                print(f"Données insérées !!")
                # On va interpréter la "route" 'genres_afficher', car l'utilisateur
                # doit voir le nouveau genre qu'il vient d'insérer. Et on l'affiche de manière
                # à voir le dernier élément inséré.
                return redirect(url_for('genres_afficher', order_by = 'DESC', id_genre_sel=0))

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
    return render_template("genres/genres_add.html")


# ---------------------------------------------------------------------------------------------------
# OM 2020.04.07 Définition d'une "route" /genres_edit ,
# cela va permettre de programmer quelles actions sont réalisées avant de l'envoyer
# au navigateur par la méthode "render_template".
# On change la valeur d'un genre de films par la commande MySql "UPDATE"
# ---------------------------------------------------------------------------------------------------
@obj_mon_application.route('/genres_edit', methods=['POST', 'GET'])
def genres_edit ():
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
            obj_actions_genres = GestionGenres()

            # OM 2019.04.02 La commande MySql est envoyée à la BD
            data_id_genre = obj_actions_genres.edit_genre_data(valeur_select_dictionnaire)
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

    return render_template("genres/genres_edit.html", data=data_id_genre)


# ---------------------------------------------------------------------------------------------------
# OM 2020.04.07 Définition d'une "route" /genres_update , cela va permettre de programmer quelles actions sont réalisées avant de l'envoyer
# au navigateur par la méthode "render_template".
# On change la valeur d'un genre de films par la commande MySql "UPDATE"
# ---------------------------------------------------------------------------------------------------
@obj_mon_application.route('/genres_update', methods=['POST', 'GET'])
def genres_update ():
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
            id_genre_edit = request.values['id_genre_edit_html']

            # Récupère le contenu du champ "intitule_genre" dans le formulaire HTML "GenresEdit.html"
            NomPerso = request.values['nom_edit_intitule_genre_html']
            PrenomPerson = request.values['pernom_edit_intitule_genre_html']
            RSPerso = request.values['rS_edit_intitule_genre_html']
            NomRespo = request.values['NR_edit_intitule_genre_html']
            PrenomRespo = request.values['PR_edit_intitule_genre_html']
            valeur_edit_list = [{'id_genre': id_genre_edit, 'NomPerso': NomPerso, 'PrenomPerso': PrenomPerson,'RSPerso': RSPerso ,
                                 'NomRespo': NomRespo,'PrenomRespo': PrenomRespo}]
            # On ne doit pas accepter des valeurs vides, des valeurs avec des chiffres,
            # des valeurs avec des caractères qui ne sont pas des lettres.
            # Pour comprendre [A-Za-zÀ-ÖØ-öø-ÿ] il faut se reporter à la table ASCII https://www.ascii-code.com/
            # Accepte le trait d'union ou l'apostrophe, et l'espace entre deux mots, mais pas plus d'une occurence.
            if not re.match("^[a-zA-Zéèàùûêâôë]{1}[a-zA-Zéèàùûêâôë \'-]*[a-zA-Zéèàùûêâôë]$",
                            NomPerso):
                # En cas d'erreur, conserve la saisie fausse, afin que l'utilisateur constate sa misérable faute
                # Récupère le contenu du champ "intitule_genre" dans le formulaire HTML "GenresEdit.html"
                # name_genre = request.values['name_edit_intitule_genre_html']
                # Message humiliant à l'attention de l'utilisateur.
                flash(f"Une entrée...incorrecte !! Pas de chiffres, de caractères spéciaux, d'espace à double, "
                      f"de double apostrophe, de double trait union et ne doit pas être vide.", "danger")

                # On doit afficher à nouveau le formulaire "genres_edit.html" à cause des erreurs de "claviotage"
                # Constitution d'une liste pour que le formulaire d'édition "genres_edit.html" affiche à nouveau
                # la possibilité de modifier l'entrée
                # Exemple d'une liste : [{'id_genre': 13, 'intitule_genre': 'philosophique'}]
                valeur_edit_list = [{'id_genre': id_genre_edit, 'NomPerso': NomPerso, 'PrenomPerso': PrenomPerson,'RSPerso': RSPerso ,
                                 'NomRespo': NomRespo,'PrenomRespo': PrenomRespo}]

                # DEBUG bon marché :
                # Pour afficher le contenu et le type de valeurs passées au formulaire "genres_edit.html"
                print(valeur_edit_list, "type ..", type(valeur_edit_list))
                return render_template('genres/genres_edit.html', data=valeur_edit_list)
            else:
                # Constitution d'un dictionnaire et insertion dans la BD
                valeur_update_dictionnaire = {'id_genre': id_genre_edit, 'NomPerso': NomPerso, 'PrenomPerso': PrenomPerson,'RSPerso': RSPerso ,
                                 'NomRespo': NomRespo,'PrenomRespo': PrenomRespo}

                # OM 2020.04.09 Objet contenant toutes les méthodes pour gérer (CRUD) les données.
                obj_actions_genres = GestionGenres()

                # La commande MySql est envoyée à la BD
                data_id_genre = obj_actions_genres.update_genre_data(valeur_update_dictionnaire)
                # DEBUG bon marché :
                print("dataIdGenre ", data_id_genre, "type ", type(data_id_genre))
                # Message ci-après permettent de donner un sentiment rassurant aux utilisateurs.
                flash(f"Valeur genre modifiée. ", "success")
                # On affiche les genres avec celui qui vient d'être edité en tête de liste. (DESC)
                return redirect(url_for('genres_afficher', order_by="ASC", id_genre_sel=id_genre_edit))

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
    return render_template('genres/genres_edit.html', data=valeur_edit_list)


# ---------------------------------------------------------------------------------------------------
# OM 2020.04.07 Définition d'une "route" /genres_select_delete , cela va permettre de programmer quelles actions sont réalisées avant de l'envoyer
# au navigateur par la méthode "render_template".
# On change la valeur d'un genre de films par la commande MySql "UPDATE"
# ---------------------------------------------------------------------------------------------------
@obj_mon_application.route('/genres_select_delete', methods=['POST', 'GET'])
def genres_select_delete ():
    if request.method == 'GET':
        try:

            # OM 2020.04.09 Objet contenant toutes les méthodes pour gérer (CRUD) les données.
            obj_actions_genres = GestionGenres()
            # OM 2019.04.04 Récupère la valeur de "idGenreDeleteHTML" du formulaire html "GenresDelete.html"
            id_genre_delete = request.args.get('id_genre_delete_html')

            # Constitution d'un dictionnaire et insertion dans la BD
            valeur_delete_dictionnaire = {"value_id_genre": id_genre_delete}

            # OM 2019.04.02 La commande MySql est envoyée à la BD
            data_id_genre = obj_actions_genres.delete_select_genre_data(valeur_delete_dictionnaire)
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
    return render_template('genres/genres_delete.html', data=data_id_genre)


# ---------------------------------------------------------------------------------------------------
# OM 2019.04.02 Définition d'une "route" /genresUpdate , cela va permettre de programmer quelles actions sont réalisées avant de l'envoyer
# au navigateur par la méthode "render_template".
# Permettre à l'utilisateur de modifier un genre, et de filtrer son entrée grâce à des expressions régulières REGEXP
# ---------------------------------------------------------------------------------------------------
@obj_mon_application.route('/genres_delete', methods=['POST', 'GET'])
def genres_delete ():
    # OM 2019.04.02 Pour savoir si les données d'un formulaire sont un affichage ou un envoi de donnée par des champs utilisateurs.
    if request.method == 'POST':
        try:
            # OM 2020.04.09 Objet contenant toutes les méthodes pour gérer (CRUD) les données.
            obj_actions_genres = GestionGenres()
            # OM 2019.04.02 Récupère la valeur de "id_genre" du formulaire html "GenresAfficher.html"
            id_genre_delete = request.form['id_genre_delete_html']
            # Constitution d'un dictionnaire et insertion dans la BD
            valeur_delete_dictionnaire = {"value_id_genre": id_genre_delete}

            data_genres = obj_actions_genres.delete_genre_data(valeur_delete_dictionnaire)
            # OM 2019.04.02 On va afficher la liste des genres des films
            # OM 2019.04.02 Envoie la page "HTML" au serveur. On passe un message d'information dans "message_html"

            # On affiche les genres
            return redirect(url_for('genres_afficher',order_by="ASC",id_genre_sel=0))



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
                return redirect(url_for('genres_afficher', order_by="ASC", id_genre_sel=0))
            else:
                # Communiquer qu'une autre erreur que la 1062 est survenue.
                # DEBUG bon marché : Pour afficher un message dans la console.
                print(f"Erreur genres_delete {erreur.args[0], erreur.args[1]}")
                # C'est une erreur à signaler à l'utilisateur de cette application WEB.
                flash(f"Erreur genres_delete {erreur.args[0], erreur.args[1]}", "danger")

            # OM 2019.04.02 Envoie la page "HTML" au serveur.
    return render_template('genres/genres_afficher.html', data=data_genres)
