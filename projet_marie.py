# Librairies importées
import pandas as pd 
import os

data = pd.read_csv("Womens Clothing E-Commerce Reviews.csv", sep = ",")
data.head()

nb_dpt = data.groupby("Department Name").count()
nb_dpt

# On récupère les reviews
avis = data["Review Text"]

# Découper les reviews en mots
avis_clean = avis.str.split()
avis_clean 

# Tockenisation
from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer('\w+')
avis_clean = avis_clean.apply(lambda x: tokenizer.tokenize(str(x)))
# print(avis_clean)

# Traitement des formes élidés


# Suppression de la ponctuation
import string
punct = string.punctuation
print(punct)
for pun in punct:
    avis_clean = avis_clean.replace(pun, ' ')
print(avis_clean)

# Supprimer la ponctuation
# import string
# punct = string.punctuation
# # print(punct)
# for pun in punct:
#     reviews_clean = reviews.replace(pun, ' ')
# print(reviews_clean)


# print(reviews.head())




# # tockenisation
# from nltk.tokenize import RegexpTokenizer
# #Tockenisation avec Reg Exp
# tokenizer = RegexpTokenizer('\w+')
# tokenizer.tokenize('je suis ici.')

# # suppression de la ponctuation
# import string
# punct = string.punctuation.replace('!', '')
# for pun in punct:
#     texte = texte.replace(pun, ' ')
# texte

# # suppression des caractères spéciaux
# import re
# texte = re.sub(r'\W', ' ', texte)
# texte

# # suppression des stopwords
# import nltk
# nltk.download('stopwords')
# from nltk.corpus import stopwords
# stopwords = stopwords.words('english')