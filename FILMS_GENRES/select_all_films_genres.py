# select_all_films_genres.py
# OM 2020.03.26 le but est d'afficher tous les lignes de la table "t_genres_films" en MySql.

# Importer le fichier "select_table.py" dans lequel il y a quelques classes et méthodes en rapport avec l'affichage des données dans UNE SEULE table.
import json

from DATABASE.SELECT import select_table
#Bonjour Monsieur OM; ça marche!!
try:
    # OM 2020.03.26 Une instance "select_record" pour permettre l'utilisation des méthodes de la classe DbSelectOneTable
    select_record = select_table.DbSelectOneTable()
    # Pour l'affichage du contenu suite à une requête SELECT avec un tri sur la colonne id_genre
    # Cette requête provient du fichier à disposition dans mon gitlab "REQUETES_tiani_martin_gerbersytemsclients_1c_2020.sql"
    mysql_select_string = ("SELECT id_Pers, Nom_Pers , id_Mails, Nom_Mail FROM t_Pers_Mails AS T1\n"
                           "INNER JOIN t_Mails AS T2 ON T2.id_Mails = T1.fk_Mail\n"
                           "INNER JOIN t_Personnes AS T3 ON T3.id_Pers = T1.fk_Pers")
    # Les résultats de la requête se trouvent dans la variable "records_select" de type <class 'list'>
    records_select = select_record.select_rows(mysql_select_string)

    # Affiche différentes formes de "sortie" des données. Il y en a beaucoup d'autres, suivant l'utilisation finale (client WEB par ex.)
    print("Type de type records_select : ",type(records_select),"Tous les résultats ", records_select, "Type des résultats ")

    for row in records_select:
        print(row['Nom_Mail'],row['Nom_Pers'],)

    for row in records_select:
        output = "nom du Mail: {Nom_Mail}  Personne: {Nom_Pers}"
        print(output.format(**row))

    # Le meilleur pour la fin : le module pymysql intègre la conversion en JSON  avec "cursorclass=pymysql.cursors.DictCursor"
    # Pour vous prouver ceci, il faut importer le module JSON et vous comparer le résultat des print ci-dessous
    # Il faut absolument approcher le format JSON
    # https://developer.mozilla.org/fr/docs/Learn/JavaScript/Objects/JSON
    print("Tous les résultats déjà en JSON ", records_select)
    print(json.dumps(records_select))
    print(json.dumps(records_select, sort_keys=True, indent=4, separators=(',', ': '), default=str))

except Exception as erreur:
    # OM 2020.03.01 Message en cas d'échec du bon déroulement des commandes ci-dessus.
    print("error message: {0}".format(erreur))
