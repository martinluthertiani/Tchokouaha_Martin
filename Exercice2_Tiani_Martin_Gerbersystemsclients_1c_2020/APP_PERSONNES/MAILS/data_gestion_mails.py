# data_gestion_mails.py
# Martin Lurher 2020.04.09 Permet de gérer (CRUD) les données de la table t_mails
from APP_PERSONNES.DATABASE.erreurs import *
from flask import flash

from Exercice2_Tiani_Martin_Gerbersystemsclients_1c_2020.APP_PERSONNES.DATABASE.erreurs import MaBdErreurConnexion


class GestionGenres():
    def __init__(self):
        try:
            # DEBUG bon marché : Pour afficher un message dans la console.
            print("dans le try de gestions genres")
            # Martin Lurher 2020.04.11 La connexion à la base de données est-elle active ?
            # Renvoie une erreur si la connexion est perdue.
            Exercice2_Tiani_Martin_Gerbersystemsclients_1c_2020().connexion_bd.ping(False)
        except Exception as erreur:
            flash("Dans Gestion genres ...terrible erreur, il faut connecter une base de donnée", "Danger")
            # DEBUG bon marché : Pour afficher un message dans la console.
            print(f"Exception grave Classe constructeur GestionGenres {erreur.args[0]}")
            # Ainsi on peut avoir un message d'erreur personnalisé.
            raise MaBdErreurConnexion(f"{msg_erreurs['ErreurConnexionBD']['message']} {erreur.args[0]}")
        print("Classe constructeur GestionGenres ")

    def genres_afficher_data(self):
        try:
            # Martin Lurher 2020.04.07 C'EST LA QUE VOUS ALLEZ DEVOIR PLACER VOTRE PROPRE LOGIQUE MySql
            # la commande MySql classique est "SELECT * FROM t_mails"
            # Pour "lever"(raise) une erreur s'il y a des erreurs sur les noms d'attributs dans la table
            # donc, je précise les champs à afficher
            strsql_genres_afficher = """SELECT id_mails, nom_mail FROM t_mails ORDER BY id_mails ASC"""
            # Du fait de l'utilisation des "context managers" on accède au curseur grâce au "with".
            with Exercice2_Tiani_Martin_Gerbersystemsclients_1c_2020().connexion_bd.cursor() as mc_afficher:
                # Envoi de la commande MySql
                mc_afficher.execute(strsql_mails_afficher)
                # Récupère les données de la requête.
                data_mails = mc_afficher.fetchall()
                # Affichage dans la console
                print("data_genres ", data_mails, " Type : ", type(data_mails))
                # Retourne les données du "SELECT"
                return data_mails
        except pymysql.Error as erreur:
            print(f"DGG gad pymysql errror {erreur.args[0]} {erreur.args[1]}")
            raise  MaBdErreurPyMySl(f"DGG gad pymysql errror {msg_erreurs['ErreurPyMySql']['message']} {erreur.args[0]} {erreur.args[1]}")
        except Exception as erreur:
            print(f"DGG gad Exception {erreur.args}")
            raise MaBdErreurConnexion(f"DGG gad Exception {msg_erreurs['ErreurConnexionBD']['message']} {erreur.args}")
        except pymysql.err.IntegrityError as erreur:
            # Martin Lurher 2020.04.09 On dérive "pymysql.err.IntegrityError" dans le fichier "erreurs.py"
            # Ainsi on peut avoir un message d'erreur personnalisé.
            raise MaBdErreurConnexion(f"DGG gad pei {msg_erreurs['ErreurConnexionBD']['message']} {erreur.args[1]}")

    def add_mails_data(self, valeurs_insertion_dictionnaire):
        try:
            print(valeurs_insertion_dictionnaire)
            # OM 2020.04.07 C'EST LA QUE VOUS ALLEZ DEVOIR PLACER VOTRE PROPRE LOGIQUE MySql
            strsql_insert_mails = """INSERT INTO t_mails (id_mails,nom_mail) VALUES (NULL,%(value_nom_mail)s)"""
            # Du fait de l'utilisation des "context managers" on accède au curseur grâce au "with".
            # la subtilité consiste à avoir une méthode "mabd_execute" dans la classe "MaBaseDeDonnee"
            # ainsi quand elle aura terminé l'insertion des données le destructeur de la classe "MaBaseDeDonnee"
            # sera interprété, ainsi on fera automatiquement un commit
            with Exercice2_Tiani_Martin_Gerbersystemsclients_1c_2020() as mconn_bd:
                mconn_bd.mabd_execute(strsql_insert_mails, valeurs_insertion_dictionnaire)


        except pymysql.err.IntegrityError as erreur:
            # Martin Lurher 2020.04.09 On dérive "pymysql.err.IntegrityError" dans "MaBdErreurDoublon" fichier "erreurs.py"
            # Ainsi on peut avoir un message d'erreur personnalisé.
            raise MaBdErreurDoublon(f"DGG pei erreur doublon {msg_erreurs['ErreurDoublonValue']['message']} et son status {msg_erreurs['ErreurDoublonValue']['status']}")



    def edit_mails_data(self, valeur_id_dictionnaire):
        try:
            print(valeur_id_dictionnaire)
            # Martin Lurher 2020.04.07 C'EST LA QUE VOUS ALLEZ DEVOIR PLACER VOTRE PROPRE LOGIQUE MySql
            # Commande MySql pour afficher le genre sélectionné dans le tableau dans le formulaire HTML
            str_sql_id_mails = "SELECT id_mails, nom_mail FROM t_mails WHERE id_mails = %(value_id_mails)s"

            # Du fait de l'utilisation des "context managers" on accède au curseur grâce au "with".
            # la subtilité consiste à avoir une méthode "mabd_execute" dans la classe "MaBaseDeDonnee"
            # ainsi quand elle aura terminé l'insertion des données le destructeur de la classe "MaBaseDeDonnee"
            # sera interprété, ainsi on fera automatiquement un commit
            with Exercice2_Tiani_Martin_Gerbersystemsclients_1c_2020().connexion_bd as mconn_bd:
                with mconn_bd as mc_cur:
                    mc_cur.execute(str_sql_id_mails, valeur_id_dictionnaire)
                    data_one = mc_cur.fetchall()
                    print("valeur_id_dictionnaire...", data_one)
                    return data_one

        except Exception as erreur:
            # Martin Lurher 2020.03.01 Message en cas d'échec du bon déroulement des commandes ci-dessus.
            print(f"Problème edit_genre_data Data Gestions Genres numéro de l'erreur : {erreur}")
            # flash(f"Flash. Problèmes Data Gestions Genres numéro de l'erreur : {erreur}", "danger")
            # Martin Lurher 2020.04.09 On dérive "Exception" par le "@obj_mon_application.errorhandler(404)" fichier "run_mon_app.py"
            # Ainsi on peut avoir un message d'erreur personnalisé.
            raise Exception(
                "Raise exception... Problème edit_genre_data d'un genre Data Gestions Genres {erreur}")

    def update_mails_data(self, valeur_update_dictionnaire):
        try:
            print(valeur_update_dictionnaire)
            # Martin Lurher 2019.04.02 Commande MySql pour la MODIFICATION de la valeur "CLAVIOTTEE" dans le champ "nameEditIntituleGenreHTML" du form HTML "GenresEdit.html"
            # le "%s" permet d'éviter des injections SQL "simples"
            # <td><input type = "text" name = "nameEditNomMailHTML" value="{{ row.nom_mail }}"/></td>
            str_sql_update_NomMail = "UPDATE t_mails SET nom_mail = %(value_name_mails)s WHERE id_mails = %(value_id_mails)s"

            # Du fait de l'utilisation des "context managers" on accède au curseur grâce au "with".
            # la subtilité consiste à avoir une méthode "mabd_execute" dans la classe "MaBaseDeDonnee"
            # ainsi quand elle aura terminé l'insertion des données le destructeur de la classe "MaBaseDeDonnee"
            # sera interprété, ainsi on fera automatiquement un commit
            with Exercice2_Tiani_Martin_Gerbersystemsclients_1c_2020().connexion_bd as mconn_bd:
                with mconn_bd as mc_cur:
                    mc_cur.execute(str_sql_update_intitulegenre, valeur_update_dictionnaire)

        except (Exception,
                pymysql.err.OperationalError,
                pymysql.ProgrammingError,
                pymysql.InternalError,
                pymysql.IntegrityError,
                TypeError) as erreur:
            # OM 2020.03.01 Message en cas d'échec du bon déroulement des commandes ci-dessus.
            print(f"Problème update_genre_data Data Gestions Genres numéro de l'erreur : {erreur}")
            # flash(f"Flash. Problèmes Data Gestions Genres numéro de l'erreur : {erreur}", "danger")
            # raise Exception('Raise exception... Problème update_genre_data d\'un genre Data Gestions Genres {}'.format(str(erreur)))
            if erreur.args[0] == 1062:
                flash(f"Flash. Cette valeur existe déjà : {erreur}", "danger")
                # Deux façons de communiquer une erreur causée par l'insertion d'une valeur à double.
                flash('Doublon !!! Introduire une valeur différente')
                # Message en cas d'échec du bon déroulement des commandes ci-dessus.
                print(f"Problème update_genre_data Data Gestions Genres numéro de l'erreur : {erreur}")

                raise Exception("Raise exception... Problème update_genre_data d'un genre DataGestionsGenres {erreur}")

    def delete_select_genre_data(self, valeur_delete_dictionnaire):
        try:
            print(valeur_delete_dictionnaire)
            # Martin Lurher 2019.04.02 Commande MySql pour la MODIFICATION de la valeur "CLAVIOTTEE" dans le champ "nameEditNomMailHTML" du form HTML "GenresEdit.html"
            # le "%s" permet d'éviter des injections SQL "simples"
            # <td><input type = "text" name = "nameEditNomMailHTML" value="{{ row.nom_mail }}"/></td>

            # Martin Lurher 2020.04.07 C'EST LA QUE VOUS ALLEZ DEVOIR PLACER VOTRE PROPRE LOGIQUE MySql
            # Commande MySql pour afficher le genre sélectionné dans le tableau dans le formulaire HTML
            str_sql_select_id_mails = "SELECT id_mails, nom_mail FROM t_mails WHERE id_mails = %(value_id_mails)s"

            # Du fait de l'utilisation des "context managers" on accède au curseur grâce au "with".
            # la subtilité consiste à avoir une gméthode "mabd_execute" dans la classe "MaBaseDeDonnee"
            # ainsi quand elle aura terminé l'insertion des données le destructeur de la classe "MaBaseDeDonnee"
            # sera interprété, ainsi on fera automatiquement un commit
            with Exercice2_Tiani_Martin_Gerbersystemsclients_1c_2020().connexion_bd as mconn_bd:
                with mconn_bd as mc_cur:
                    mc_cur.execute(str_sql_select_id_genre, valeur_delete_dictionnaire)
                    data_one = mc_cur.fetchall()
                    print("valeur_id_dictionnaire...", data_one)
                    return data_one

        except (Exception,
                pymysql.err.OperationalError,
                pymysql.ProgrammingError,
                pymysql.InternalError,
                pymysql.IntegrityError,
                TypeError) as erreur:
            # DEBUG bon marché : Pour afficher un message dans la console.
            print(f"Problème delete_select_genre_data Gestions Genres numéro de l'erreur : {erreur}")
            # C'est une erreur à signaler à l'utilisateur de cette application WEB.
            flash(f"Flash. Problème delete_select_genre_data numéro de l'erreur : {erreur}", "danger")
            raise Exception("Raise exception... Problème delete_select_genre_data d\'un genre Data Gestions Genres {erreur}")


    def delete_genre_data(self, valeur_delete_dictionnaire):
        try:
            print(valeur_delete_dictionnaire)
            # OM 2019.04.02 Commande MySql pour EFFACER la valeur sélectionnée par le "bouton" du form HTML "GenresEdit.html"
            # le "%s" permet d'éviter des injections SQL "simples"
            # <td><input type = "text" name = "nameEditIntituleGenreHTML" value="{{ row.intitule_genre }}"/></td>
            str_sql_delete_nommail = "DELETE FROM t_mails WHERE id_mails = %(value_id_mails)s"

            # Du fait de l'utilisation des "context managers" on accède au curseur grâce au "with".
            # la subtilité consiste à avoir une méthode "mabd_execute" dans la classe "MaBaseDeDonnee"
            # ainsi quand elle aura terminé l'insertion des données le destructeur de la classe "MaBaseDeDonnee"
            # sera interprété, ainsi on fera automatiquement un commit
            with Exercice2_Tiani_Martin_Gerbersystemsclients_1c_2020().connexion_bd as mconn_bd:
                with mconn_bd as mc_cur:
                    mc_cur.execute(str_sql_delete_intitulegenre, valeur_delete_dictionnaire)
                    data_one = mc_cur.fetchall()
                    print("valeur_id_dictionnaire...",data_one)
                    return data_one
        except (Exception,
                pymysql.err.OperationalError,
                pymysql.ProgrammingError,
                pymysql.InternalError,
                pymysql.IntegrityError,
                TypeError) as erreur:
            # DEBUG bon marché : Pour afficher un message dans la console.
            print(f"Problème delete_genre_data Data Gestions Genres numéro de l'erreur : {erreur}")
            # flash(f"Flash. Problèmes Data Gestions Genres numéro de l'erreur : {erreur}", "danger")
            if erreur.args[0] == 1451:
                # Martin Lurher 2020.04.09 Traitement spécifique de l'erreur 1451 Cannot delete or update a parent row: a foreign key constraint fails
                # en MySql le moteur INNODB empêche d'effacer un genre qui est associé à un film dans la table intermédiaire "t_genres_films"
                # il y a une contrainte sur les FK de la table intermédiaire "t_genres_films"
                # C'est une erreur à signaler à l'utilisateur de cette application WEB.
                # flash(f"Flash. IMPOSSIBLE d'effacer !!! Ce genre est associé à des films dans la t_genres_films !!! : {erreur}", "danger")
                # DEBUG bon marché : Pour afficher un message dans la console.
                print(f"IMPOSSIBLE d'effacer !!! Ce genre est associé à des films dans la t_genres_films !!! : {erreur}")
            raise MaBdErreurDelete(f"DGG Exception {msg_erreurs['ErreurDeleteContrainte']['message']} {erreur}")