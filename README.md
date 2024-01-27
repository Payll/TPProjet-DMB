# Mini-Projet Spark 2022-2023
## Description du Projet
Ce mini-projet a été réalisé dans le cadre de la spécialité "Technologies de l’information option informatique" en 3ème année à l'ESIR. Le projet se concentre sur l'analyse de données à l'aide de Spark et explore un jeu de données spécifique.

## Jeu de Données
Pour ce projet, le jeu de données choisi est celui des "Avengers" qui contient diverses informations sur les personnages qui ont fait partis des Avengers. Ce jeu de données permet d'explorer plusieurs aspects intéressants via des requêtes Spark.

## Questions d'Analyse
Les questions analysées dans ce projet sont :

### Nombre d'Avengers Actuellement Actifs :
Traitement dans le Code :
- **Filtrage des Avengers Actifs** : Le DataFrame avengers est filtré pour ne garder que les lignes où la colonne "Current?" est égale à "YES". Cela permet d'identifier les personnages actuellement actifs.
- **Calcul du Nombre et du Pourcentage** : Le nombre total d'Avengers et le nombre d'Avengers actifs sont calculés. Le pourcentage d'Avengers actifs est ensuite dérivé en divisant le nombre d'Avengers actifs par le nombre total d'Avengers.

#### Analyse :
Cette analyse fournit un aperçu clair du nombre et de la proportion d'Avengers qui sont actuellement actifs dans l'univers des Avengers. Cela peut refléter des tendances dans l'écriture et la popularité des personnages au fil du temps.

### Avenger Avec le Plus Grand Nombre de Morts :
Traitement dans le Code :
- **Nettoyage et Transformation des Données** : Les colonnes représentant les morts (Death1, Death2, etc.) sont nettoyées pour remplacer les valeurs 'NULL' et 'NO' par '0' et 'YES' par '1'.
- **Calcul des Morts Totales** : Une nouvelle colonne 'TotalDeaths' est créée en sommant les colonnes de morts.
- **Tri et Sélection** : Les données sont triées par 'TotalDeaths' en ordre décroissant et les 10 premières lignes sont affichées pour identifier les Avengers avec le plus grand nombre de morts.
#### Analyse :
Cette analyse révèle les personnages qui ont subi le plus de morts, offrant un aperçu de la dynamique des personnages dans les récits. Cela peut indiquer des personnages particulièrement importants ou emblématiques qui ont souvent été au centre d'événements majeurs.

### Corrélation entre le Nombre de Morts et le Nombre d'Apparitions :
Traitement dans le Code :
- **Préparation des Données** : Les colonnes pertinentes sont sélectionnées et transformées si nécessaire pour garantir qu'elles soient numériques.
- **Calcul de la Matrice de Corrélation** : Une matrice de corrélation est calculée pour ces colonnes à l'aide de la méthode .corr() de Pandas.
- **Visualisation** : La matrice de corrélation est visualisée sous forme de heatmap pour faciliter l'interprétation des relations entre les variables.
#### Analyse :
Cette analyse vise à découvrir les relations potentielles entre plusieurs aspects des personnages des Avengers, y compris le nombre de morts, le nombre d'apparitions, les années depuis l'adhésion, le genre, et le statut actuel (actif ou non). La heatmap fournit un aperçu visuel des corrélations entre ces variables. Une corrélation forte indiquerait une relation significative entre deux variables. Dans notre cas, l'absence de fortes corrélations entre toutes les variables indique qu'aucune d'entre elles n'est directement liée de manière significative à une autre, suggérant que les événements dans les récits des Avengers, comme les morts ou les apparitions, ne dépendent pas simplement d'un seul de ces facteurs mais plutôt d'une combinaison plus complexe de circonstances et de choix narratifs.