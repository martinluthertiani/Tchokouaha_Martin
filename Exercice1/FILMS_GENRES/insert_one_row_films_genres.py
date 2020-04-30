# insert_one_row_films_genres.py
# OM 2698.03.27 Permet d'insérer des valeurs dans la table "t_genres_films"

# Importer le fichier "InsertOneTable" dans lequel il y a quelques classes et méthodes en rapport avec le sujet d'insertion dans UNE SEULE table.
from DATABASE.INSERT import insert_one_table
#ABCDEMACCAUD
try:
    # OM 2020.01.28 Une instance "insert_records" pour permettre l'utilisation des méthodes de la classe DbInsertOneTable
    insert_records = insert_one_table.DbInsertOneTable()

    valeur_ins_fkPers = 1
    valeur_ins_fkTeleph = 3
    # Afficher les valeurs dans la console...c'est tout, vraiment tout !
    print("valeur_fkPers ",valeur_ins_fkPers, "valeur_fkTeleph ",valeur_ins_fkTeleph)

    # Définitions d'un dictionnaire pour passer les valeurs en paramètres de façon un "peu" sécurisée dans la BD
    valeurs_insertion_dictionnaire = {'value_fkPers': valeur_ins_fkPers, 'value_fkTeleph': valeur_ins_fkTeleph}

    # OM 2020.01.28 Pour éviter les injections SQL, il est possible de passer les valeurs à insérer sous forme "paramètrée" (avec le %(...)s au lieu de %s)
    # Pour les vrais geeks et geeketes consulter le site ci-dessous.
    # L'insertion de données est vraiment TROP inspirée du site suivant MERCI !!! https://realpython.com/prevent-python-sql-injection/

    # Une longue chaîne de caractères (format PEP8 selon proposition de PyCharm)
    # Je décide d'insèrer 2 on voit ainsi la correspondance des positions entre les attributs
    # de la BD et les variables Python définies juste en dessus.
    mysql_insert_string = "INSERT INTO t_Pers_Teleph (id_Pers_Teleph, fk_Pers, fk_Teleph, DateEnreg_Teleph) VALUES " \
                          "(NULL, %(value_fkPers)s, %(value_fkTeleph)s, CURRENT_TIMESTAMP) "
    # Insertion des valeurs définie dans la variable dictionnaire "valeurs_insertion_dictionnaire"
    # dans la table "t_Pers_Teleph"
    insert_records.insert_one_record_many_values_one_table(mysql_insert_string,
                                                           valeurs_insertion_dictionnaire)

except Exception as erreur:
    # OM 2020.04.03 Message en cas d'échec du bon déroulement des commandes ci-dessus.
    print("error message: {0}".format(erreur))