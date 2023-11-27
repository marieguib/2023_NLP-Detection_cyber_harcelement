# Librairies importées
import pandas as pd 
import os

# Import de notre base de données
data = pd.read_csv("Womens Clothing E-Commerce Reviews.csv", sep = ",")
# print(data.columns)

# Affichage des 5 premières lignes des colonnes où on a la partie textuelle
# print(data[["Title", "Review Text"]].head())

# 1) Nettoyage des données
# On supprime les lignes où on a des valeurs manquantes pour Review Text
# 

# Choix de la problématique : 

