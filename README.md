# Analyse Exploratoire des Achats en Supermarché

Ce projet présente une analyse exploratoire des données de vente d'un supermarché, centrée sur le comportement des clients, la performance des rayons et le calendrier des commandes.

## Sommaire

- [Objectif](#objectif)
- [Contenu du projet](#contenu-du-projet)
- [Sommaire détaillé du notebook](#sommaire-détaillé-du-notebook)
- [Prérequis](#prérequis)
- [Installation et exécution](#installation-et-exécution)
- [Données et sorties](#données-et-sorties)
- [Résultats clés](#résultats-clés)
- [Points forts](#points-forts)

## Objectif

L'objectif est de transformer un dataset de ventes en insights exploitables pour le merchandising et la planification des stocks :

- identifier les produits les plus vendus
- détecter les articles ajoutés en premier dans le panier
- analyser les produits les plus réachetés
- comprendre les habitudes de commande par jour et par heure
- évaluer les rayons et départements les plus rentables
- mesurer la taille des paniers
- vérifier l'impact du délai entre commandes sur le réachat

## Contenu du projet

- `index.ipynb` : notebook principal d'analyse EDA.
- `requirement.txt` : dépendances Python nécessaires.
- `output/` : fichiers CSV générés par l'analyse.
- `exploratory-data-analysis-CA.pdf` : Cahier de charge.

## Sommaire détaillé du notebook

Le notebook `index.ipynb` couvre les sections suivantes :

1. **Chargement des données**
   - import des fichiers `aisles.csv`, `departments.csv`, `products.csv`, `orders.csv` et `order_products.csv`.

2. **Produits les plus vendus**
   - calcul du top 20 des produits par nombre de ventes.
   - visualisation par produit et rayon.

3. **Produits ajoutés premiers au panier**
   - analyse des articles classés `add_to_cart_order == 1`.
   - identification des produits les plus souvent choisis en premier.

4. **Produits les plus réachetés**
   - analyse du champ `reordered` pour trouver les produits à forte fidélité.

5. **Analyse temporelle des commandes**
   - volume de commandes par jour de la semaine.
   - volume de commandes par heure de la journée.

6. **Rayons et départements les plus rentables**
   - performance des rayons (`aisle`) et des départements (`department`).

7. **Taille du panier**
   - distribution du nombre d'articles par commande.
   - calcul des valeurs minimale, moyenne et maximale.

8. **Impact du délai de commande sur le réachat**
   - comparaison des délais moyens entre réachat et non-réachat.

## Prérequis

- Python 3.8+
- Jupyter Notebook ou VS Code
- Les bibliothèques listées dans `requirement.txt`

## Installation et exécution

1. Crée un environnement Python.
2. Installe les dépendances :

```bash
pip install -r requirement.txt
```

3. Ouvre `index.ipynb` dans Jupyter Notebook ou VS Code.
4. Exécute les cellules du notebook dans l'ordre.

## Données et sorties

Le notebook utilise les fichiers sources du dossier `data/` et produit des fichiers dans `output/` :

- `les_produit_les_plus_vendus.csv`
- `Top_20_des_produits_ajoutes_en premier_dans_le_panier.csv`
- `Top_20_des_produits_les_plus_rachetés.csv`
- `Nombres_de vente_par_heure.csv`
- `Nombres_de_ventes_par_jour.csv`
- `les_rayons_les_plus_rentables.csv`
- `les_departements_les_plus_popuaire.csv`
- `taille_du_panier_moyen.csv`

## Résultats clés

- Le top des ventes est dominé par des produits frais, notamment les fruits et les légumes emballés.
- Les mêmes produits se retrouvent souvent en tête des listes des articles ajoutés en premier et des articles les plus réachetés.
- Les commandes sont majoritairement passées en début de semaine, avec un pic le lundi et le mardi.
- La plage horaire la plus active est entre 10h et 16h.
- Le rayon "Produce" apparaît comme l'un des plus rentables.
- La taille moyenne du panier est proche de 10 articles, avec des pics importants pour les commandes groupées.
- Les clients rachetant un produit reviennent généralement plus rapidement que ceux qui ne le rachètent pas.

## Points forts

- analyse descriptive claire
- visualisations prêtes à être présentées
- insights actionnables pour le merchandising et la gestion des stocks
- segmentation temporelle utile pour optimiser les promotions et livraisons


