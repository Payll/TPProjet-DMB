# Importation des bibliothèques nécessaires
import pyspark
from pyspark.sql import functions as F
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Initialisation de la session Spark
spark = pyspark.sql.SparkSession.builder.appName("avengers").getOrCreate()

# Lecture du fichier CSV
avengers = spark.read.csv("avengers.csv", header=True, inferSchema=True)

# Affichage des premières lignes du DataFrame
avengers.show(5)

# Q1 (simple): Nombre d'Avengers actuellement actifs
num_active_avengers = avengers.filter(avengers["Current?"] == "YES").count()
total_avengers = avengers.count()
percentage_active = (num_active_avengers / total_avengers) * 100

print(f" === Q1: Combien de personnes sont actuellement actives dans les comics? ===")
print(f"{num_active_avengers} / {total_avengers} personnes ({percentage_active:.2f}% des personnes sont actuellement actives)")

# Q2 (moyen): Avenger avec le plus grand nombre de morts
death_cols = ['Death1', 'Death2', 'Death3', 'Death4', 'Death5']

# Remplacement des valeurs 'NULL' et 'NO' par '0' dans les colonnes de morts
for col in death_cols:
    avengers = avengers.withColumn(col, F.when(F.col(col) == 'YES', 1).otherwise(0))

# Recalcul de 'TotalDeaths' comme la somme des colonnes de morts
avengers = avengers.withColumn(
    'TotalDeaths',
    sum(F.col(col) for col in death_cols)
)

# Tri du DataFrame par le nombre de morts en ordre décroissant
avengers_sorted_by_deaths = avengers.sort(F.col('TotalDeaths').desc())

print(" === Q2: Qui a le plus de morts dans les comics? ===")
print("  = Top 10 des Avengers par nombre de morts enregistrés =")
avengers_sorted_by_deaths.select('Name/Alias', 'TotalDeaths').show(10, truncate=False)

# Q3 (difficile): Corrélation entre le nombre de morts et le nombre d'apparitions des Avengers

# Conversion des valeurs binaires dans les colonnes 'Gender' et 'Current?'
avengers = avengers.withColumn("Gender", F.when(F.col("Gender") == 'MALE', 1).otherwise(0))
avengers = avengers.withColumn("Current?", F.when(F.col("Current?") == 'YES', 1).otherwise(0))

# Sélection des colonnes numériques pour l'analyse
numerical_columns = ['TotalDeaths', 'Appearances', 'Years since joining', 'Gender', 'Current?']
avengers_numerical = avengers.select(numerical_columns)

# Calcul de la matrice de corrélation
correlation_matrix = avengers_numerical.toPandas().corr()

# Création d'une heatmap pour visualiser la matrice de corrélation
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', square=True)
plt.title('Carte de chaleur de corrélation du jeu de données Avengers')
plt.show()
